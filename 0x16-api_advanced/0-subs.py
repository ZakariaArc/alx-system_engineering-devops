import requests

CLIENT_ID = 'cCm22L_jt57JGXZQH8sw3g'
CLIENT_SECRET = 'pETXZ9frk_FBk2bnIf32IgHhFlnaWw'
USERNAME = 'KLRthegoat'
PASSWORD = 'zikoSAFAE123@'

def authenticate():
    data = {
        'grant_type': 'password',
        'username': USERNAME,
        'password': PASSWORD
    }
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    response = requests.post('https://www.reddit.com/api/v1/access_token', data=data, auth=auth)
    return response.json().get('access_token')

def number_of_subscribers(subreddit):
    access_token = authenticate()
    headers = {
        'User-Agent': 'Your script description',
        'Authorization': f'Bearer {access_token}'
    }
    url = f"https://oauth.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            return data.get('subscribers', 0)
    return 0

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
