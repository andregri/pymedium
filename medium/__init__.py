import requests

class Client:
    def __init__(self, token: str):
        self.token = token
        self.user_id = ''
        self.get_requests_header = {
            'Authorization': 'Bearer ' + self.token,
            'Accept': 'application/json',
            'Accept-Charset': 'utf-8'
        }


    def authenticate(self):
        """
        GET https://api.medium.com/v1/me
        """
        h = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Accept-Charset': 'utf-8'
        }
        r = requests.get('https://api.medium.com/v1/me', headers=h)

        response = r.json()

        if r.status_code == 200:
            self.user_id = response['data']['id']
            return response['data']
        else:
            raise RuntimeError(response['errors'][0]['message'])


    def get_pubblications(self):
        """
        GET https://api.medium.com/v1/users/{{userId}}/publications
        """
        r = requests.get('https://api.medium.com/v1/users/' + self.user_id + '/publications',
            headers=self.get_requests_header)
        
        response = r.json()

        if r.status_code == 200:
            return response['data']
        else:
            raise RuntimeError(response['errors'][0]['message'])


    def get_contributors(self, pubblication_id):
        """
        GET https://api.medium.com/v1/publications/{{publicationId}}/contributors
        """
        r = requests.get('https://api.medium.com/v1/publications/' + pubblication_id + '/contributors',
            headers=self.get_requests_header)

        response = r.json()

        if r.status_code == 200:
            return response['data']
        else:
            raise RuntimeError(response['errors'][0]['message'])