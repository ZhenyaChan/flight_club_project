import requests

SHEETY_ENDPOINT = "https://api.sheety.co/34e0ae8668980fd4b0dc81f1a66bac18/flightDeals/prices"
TOKEN = "hd3h198dh18dh83d193dfr90jg95kg-2jd92g9"
SHEET_USERS_ENDPOINT = "https://api.sheety.co/34e0ae8668980fd4b0dc81f1a66bac18/flightDeals/users"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination(self):
        response = requests.get(SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            response.raise_for_status()

    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
