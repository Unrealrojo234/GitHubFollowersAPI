from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)
CORS(app)

#Loading Environment Variables
username = os.getenv('USER_NAME')
access_token = os.getenv('ACCESS_TOKEN')


def get_all_pages(url, token):
    result = []
    while url:
        response = requests.get(url, headers={"Authorization": f"token {token}"})
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
        result += response.json()
        url = response.links.get("next", {}).get("url")
    return result

@app.route('/')
def root():
    return '<h1 style="text-align:center;color:rebeccapurple;">GitHub Followers Api</h1>'

@app.route('/status')
def check_github_relationships():
    try:
        followers_url = f"https://api.github.com/users/{username}/followers?per_page=100"
        followers = get_all_pages(followers_url, access_token)

        following_url = f"https://api.github.com/users/{username}/following?per_page=100"
        following = get_all_pages(following_url, access_token)

        not_followed_back = [user for user in following if user["login"] not in [follower["login"] for follower in followers]]
        return {"not_followed_back": not_followed_back, "followers": followers, "following": following}
    except Exception as e:
        return f"Error checking GitHub relationships {e}"

@app.route('/unfollow_all_non_followers')
def unfollow_non_followers():
    try:
        followers_url = f"https://api.github.com/users/{username}/followers?per_page=100"
        followers = get_all_pages(followers_url, access_token)

        following_url = f"https://api.github.com/users/{username}/following?per_page=100"
        following = get_all_pages(following_url, access_token)

        not_followed_back = [user for user in following if user["login"] not in [follower["login"] for follower in followers]]
        if not not_followed_back:
            return "No one to unfollow."
        else:
            for user in not_followed_back:
                user_to_unfollow = user["login"]
                requests.delete(f"https://api.github.com/user/following/{user_to_unfollow}", headers={"Authorization": f"token {access_token}"})
                return f"Unfollowed {user_to_unfollow}"
    except Exception as e:
        return f"Error unfollowing non-followers: {e}"    


@app.route("/unfollow/<username>")
def unfollow_user(username):
    try:
        requests.delete(f"https://api.github.com/user/following/{username}", headers={"authorization": f"token {access_token}"})
        return f"Unfollowed {username}"
    except Exception as e:
        return f"Error unfollowing {username}: {e}"
    

if __name__ == '__main__':
    app.run(debug=True)