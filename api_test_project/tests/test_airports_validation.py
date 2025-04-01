import pytest
from api_test_project.api.airportgap_api_client import AirportGapAPIClient
from api_test_project.helper.airportgap_config import VALIDATION_TEST_DATA
from api_test_project.helper.airportgap_helper import AirportGapHelper


@pytest.fixture(scope="module")
def api_client():
    return AirportGapAPIClient()

@pytest.fixture(scope="module")
def airport_helper(api_client):
    return AirportGapHelper(api_client)

def test_airport_count(api_client):
    airports_amount = VALIDATION_TEST_DATA["airports_amount"]
    response = api_client.get_airports()
    json_response = response.json()
    airports_list = json_response["data"]
    assert len(airports_list) == airports_amount, f"Expected {airports_amount} airports, but got {len(airports_list)}"

def test_specific_airports_exists(airport_helper):
    airports_name_list = VALIDATION_TEST_DATA["expected_airports_name_list"]
    name_not_found = airport_helper.verify_airport_names_exist(airports_name_list)
    assert not name_not_found ,f"Failed - {name_not_found} airport names is not on airports list"


def test_airport_distance(airport_helper):
    airports = VALIDATION_TEST_DATA["airports_couple"]
    distance = airport_helper.get_distance_in_km(airports["from"], airports["to"])
    assert distance > 400, "distance in km not bigger than 400 as expected"