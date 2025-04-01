from api_test_project.api.airportgap_api_client import AirportGapAPIClient

class AirportGapHelper():
    
    def __init__(self, api_client: AirportGapAPIClient):
        self.api_client = api_client
    
    def get_airports_as_json(self):
        """
        Fetches the list of airports and returns the data in JSON format and return as list
        """
        response = self.api_client.get_airports()
        json_response = response.json()
        airports_list = json_response["data"]
        return airports_list
        
    def get_current_airports_name(self):
        """
        Extracts and returns as set the names of all airports in the current dataset.
        """
        airports_list = self.get_airports_as_json()
        return {airport['attributes']['name'] for airport in airports_list}
    
    def verify_airport_names_exist(self,name_list):
        """
        Verifies if the given list of airport names exist in the current dataset.
        """
        missing_names = []
        all_airports_names = self.get_current_airports_name()
        for name in name_list:
            if name not in all_airports_names:
                missing_names.append(name)
        return missing_names

    def get_distance_in_km(self,from_airport,to_airport):
        """
        Fetches the distance in kilometers between two airports.
        """
        response = self.api_client.get_airport_distance(from_airport,to_airport)
        json_response = response.json()
        try:
            data = json_response["data"]
            attribute = data["attributes"]
            return attribute["kilometers"]
        except Exception as e:
            raise SystemExit(f"Failed to extract data content attributes as expected: {e}")



