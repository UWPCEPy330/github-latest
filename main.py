import sys
import json
from urllib import response

import requests

if __name__ == "__main__":
    username = input("Enter a Github username: ")

    response = requests.get(f"https://api.github.com/users/{username}/events")

    events = json.loads(response.content)

    print(events[0]['created_at'])
