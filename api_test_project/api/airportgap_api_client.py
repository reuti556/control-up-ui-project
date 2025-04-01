import requests
from api_test_project.helper.logger import logger  

from api_test_project.api.auth import Auth
from api_test_project.helper.airportgap_config import BASE_URL,CREDENTIALS

class AirportGapAPIClient():
    def __init__(self):
            self.auth = Auth(CREDENTIALS["email"],CREDENTIALS["password"])

    def _get_headers(self):
        token = self.auth.get_token()
        return {"Authorization": f"Bearer {token}"}

    def get_airports(self):
        logger.info(f"Going to perform GET request to get all airports")
        url = f"{BASE_URL}/airports"
        headers = self._get_headers()
        try:
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                    raise
            return response
        except requests.exceptions.RequestException as e:
            logger.info(f"An error occurred while making the request: {e}")
            return None

    def get_airport_distance(self, from_airport: str, to_airport: str):
        logger.info(f"Going to perform POST request to get all airports")
        url = f"{BASE_URL}/airports/distance"
        payload = {"from": from_airport, "to": to_airport}
        headers = self._get_headers()
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code != 200:
                    raise
            return response
        except requests.exceptions.RequestException as e:
            logger.info(f"An error occurred while making the request: {e}")
            return None
