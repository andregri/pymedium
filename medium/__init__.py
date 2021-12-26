import requests

class Client:

    def __init__(self, integration_token: str):
        self.integration_token = integration_token

        payload = {
        'Authorization': 'Bearer ' + self.integration_token,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8'
        }
        r = requests.get('https://api.medium.com/v1/me', headers=payload)

        response_json = r.json()["data"]

        self.user_id = response_json["id"]
        self.username = response_json["username"]
        self.name = response_json["name"]
        self.user_url = response_json["url"]
        self.user_img_url = response_json["imageUrl"]

        print(self.__dict__)