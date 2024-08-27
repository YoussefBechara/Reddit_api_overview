# Reddit API Overview

## Description

This project demonstrates how to interact with the Reddit API using Python. It includes a script to fetch various facts and data from Reddit, showcasing the capabilities of the Reddit API.

## Prerequisites

- Python 3.x
- `praw` library

## Installation

1. Clone the repository:

git clone https://github.com/YoussefBechara/Reddit_api_overview.git


2. Navigate to the project directory:

cd Reddit_api_overview


3. Install the required dependencies:

pip install praw
sql_more


## Getting Reddit API Credentials

To use this script, you need to obtain Reddit API credentials. Follow these steps:

1. Go to https://www.reddit.com/prefs/apps
2. Click on "Create App" or "Create Another App" at the bottom
3. Fill in the details:
- Name: Your app name
- App type: Choose "script"
- Description: Brief description of your app
- About URL: Optional
- Redirect URI: http://localhost:8080 (This is required but not used in our script)
4. Click "Create app"
5. You'll now see your app details. Note down the following:
- client_id: The string under "personal use script"
- client_secret: The "secret" field
- user_agent: A unique identifier for your app, typically in the format: 
  `<platform>:<app ID>:<version string> (by /u/<Reddit username>)`

## Configuration

In the `get_reddit_facts.py` file, replace the placeholder values with your actual Reddit API credentials:

```python
client_id='your client id'
client_secret='your client secret'
user_agent='your user agent'

Usage

Run the script:

python get_reddit_facts.py

This will execute the script and display various facts fetched from Reddit using the API.
Features

    Fetches top posts from specified subreddits
    Retrieves user information
    Demonstrates basic Reddit API functionality
