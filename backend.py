import requests
import P_info

API_key = P_info.get_apikey()

def get_data(place,days=None,selection=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"

    response = requests.get(url)
    content = response.json()

    filtered_data = content["list"]

    no_of_values = 8*days

    filtered_data = filtered_data[:no_of_values]
    #8 values for 24 hours

    return filtered_data

if __name__ == "__main__":
    print(get_data("Tokyo",2,"Temperature"))