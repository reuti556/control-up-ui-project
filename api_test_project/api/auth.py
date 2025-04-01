import requests
from api_test_project.helper.airportgap_config import BASE_URL

class Auth():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.token = None

    def _generate_token(self):
        url = f"{BASE_URL}/tokens"
        data = {
            "email": self.email,
            "password": self.password
        }
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            response_data = response.json()
            self.token = response_data.get('token')

            if not self.token:
                raise ValueError("Token not found in response")

            print("Token successfully generated")
            return self.token
        except requests.exceptions.RequestException as e:
            raise SystemExit(f"Request failed: {e}")

    def get_token(self):
        if not self.token:
            return self._generate_token()
        return self.token
