import requests as req
import json
import pprint as pr

HOST = 'http://127.0.0.1:8000'


class Session(object):

    def __init__(self):
        self.client_id = 'aMsyBZha5VjeXJbP4yeMHjLPWsfPIvQprQWIGG9N'
        self.client_secret = 'cQ9tPD5CyMVM55c4CgeR1CgV2ygIlgq7V5CbJhMJRFU' \
                        '5iUgA2CK5RtgjZayv2wXnw0G9bCY1Fy9OTQe9zATXF2n0Z' \
                        'O67QQoo3G9nyOANJNeAMhJbNFWEnXNAfH797hoK'
        self.json_header = 'Content-Type: application/json'
        self.token_url = 'http://127.0.0.1:8000/api/users/o/token/'
        self.access_token = 'none'
        self.refresh_token = 'none'

    def append_oauth_header(self, headers):
        auth_header = {'Authorization': 'Bearer ' + self.access_token}
        headers.update(auth_header)
        return headers

    def get_credentials(self, username, password):
        # step A, B - single call with client credentials as the basic auth header - will return access_token
        data = {'grant_type': 'password',
                'username': username,
                'password': password}
        access_token_response = req.post(self.token_url, data=data,
                                              verify=False, allow_redirects=False,
                                              auth=(self.client_id, self.client_secret))

        data = json.loads(access_token_response.text)
        self.access_token = data['access_token']
        self.refresh_token = data['refresh_token']

    def set_credentials(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = refresh_token


def pbody(response):
    if response.status_code < 400:
        return json.loads(response.text)
    else:
        return {'error': "could not parse message "
                         "because there wasn't a valid request"}


def get(session, url, params={}):
    response = req.get(url, headers=session.append_oauth_header({}), params=params)
    return response


def post(session, url, data={}):
    headers = {'Content-Type': 'application/json'}
    headers = session.append_oauth_header(headers)
    response = req.post(url, headers=headers, data=data)
    print(response.status_code)
    return response


def get_users_profile(session):
    url = f'{HOST}/api/users/myprofile/'
    response = get(session, url)
    return pbody(response), response


def get_user_post(session, post_id):
    url = f'{HOST}/api/posts/post/'
    response = get(session, url, params={'post': post_id})
    return pbody(response), response


def get_user_post_list(session, username):
    url = f'{HOST}/api/posts/list/{username}/'
    response = get(session, url)
    return pbody(response), response


def post_profile(session, data):
    url = f'{HOST}/api/users/myprofile/'
    response = post(session, url, data=json.dumps(data))
    return pbody(response), response


def post_post(session, data):
    url=f'{HOST}/api/posts/post/'
    response = post(session, url, data=json.dumps(data))
    return pbody(response), response


if __name__ == '__main__':
    print(HOST)

    # AUTHENTICATION AND SESSION
    ######################################
    username = 'bob'
    password = 'pass'
    session = Session()
    #session.get_credentials(username, password)
    session.set_credentials('gsNFf7qppOpSFc6VGd3CPCQNHw2PTD'
                            , 'njwF3S3xJ9Qubhxstbm5EawjSOPSI3')
    print('access_token: ', session.access_token)
    print('refresh_token: ', session.refresh_token)
    print('--------------------------------------')

    # PROFILE
    ######################################
    print("-| The user's profile")
    profile, _ = get_users_profile(session)
    pr.pprint(profile, indent=5)
    print("")

    print("-| Updated the users profile")
    profile = {"bio": "hello there again...",
               "firstName": "bobby123",
               "lastName": "mobby123"}
    updated_profile, _ = post_profile(session, profile)
    pr.pprint(updated_profile, indent=5)
    print("")