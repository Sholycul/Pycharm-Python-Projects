#!/usr/bin/python

import requests
from sys import argv



repo_name = argv[1]
user_name = argv[2]

headers = {
    "accept": "application/vnd.github+json",
}

url = f"https://api.github.com/repos/{user_name}/{repo_name}/commits"

response = requests.get(url)
print(response.json())
