# GitHub Followers API

This is a Flask application that interacts with the GitHub API to manage your followers and following lists. It provides endpoints to check your followers, see who you are following but not followed back by, and unfollow users.

## Features

- Display a welcome message at the root endpoint.
- Check the status of your GitHub relationships.
- Unfollow all users who do not follow you back.
- Unfollow a specific user.

## Requirements

- Python 3.x
- Flask
- Flask-CORS
- python-dotenv
- requests

## Setup

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd GitHub_Followers_Api
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your GitHub username and access token:
   ```env
   USER_NAME=your_github_username
   ACCESS_TOKEN=your_github_access_token
   ```

## Running the Application

1. Run the Flask application:

   ```sh
   python app.py
   ```

2. The application will be available at `http://127.0.0.1:5000`.

## Endpoints

- **GET /**: Displays a welcome message.
- **GET /status**: Checks your GitHub relationships and returns users who do not follow you back.
- **GET /unfollow_all_non_followers**: Unfollows all users who do not follow you back.
- **GET /unfollow/<username>**: Unfollows a specific user.

## Example Usage

- To check your GitHub relationships, navigate to:

  ```
  http://127.0.0.1:5000/status
  ```

- To unfollow all users who do not follow you back, navigate to:

  ```
  http://127.0.0.1:5000/unfollow_all_non_followers
  ```

- To unfollow a specific user, navigate to:
  ```
  http://127.0.0.1:5000/unfollow/<username>
  ```

Replace `<username>` with the GitHub username of the user you want to unfollow.

## License

This project is licensed under the MIT License.
