import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    api_url = 'https://api.github.com'
    try:
        username = sys.argv[1]
    except IndexError:
        print("Requires a username as the first argument")
        raise

    events = requests.get('/'.join([api_url, 'users', username, 'events']))
    print(events.json()[0]['created_at'])
