from dotenv import load_dotenv
import os
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize


def get_sites_from_api():
    """Return a list"""
    load_dotenv()
    json_data = requests.get(
        "https://te-data-test.herokuapp.com/api/sites?token="+os.environ.get("api-token")).json()
    print("Getting current weather data from OpenWeatherMap.org..........")
    return json_data


def write_weather_data_in_json_file(json_data):
    """ Save current weather data to a json file.
        Name the file by the Unix Timestamp.
    """
    name = 'data'  ## + str(json_data['timestamp'])
    filename = r"data_cache/%s.json" % name
    with open(filename, 'w') as f:
        json.dump(json_data, f)
    return filename


def convert_json_to_dict(filename):
    """ Convert json file to python dictionary
    """
    with open(filename, 'r') as JSON:
        json_dict = json.load(JSON)
    return json_dict


def convert_dict_to_df(filename):
    """ Convert python dictionary to pandas dataframe
    """
    return json_normalize(convert_json_to_dict(filename))


def main():
    json_data = get_sites_from_api()
    file_name = write_weather_data_in_json_file(json_data)
    df = convert_dict_to_df(file_name)
    return df


if __name__ == "__main__":
    main()
