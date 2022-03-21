from dotenv import load_dotenv
import os
import requests
import json
import schedule
from datetime import datetime
import time


def get_sites_from_api():
    """Return list of all existing sites."""
    load_dotenv()
    json_data = requests.get(
        "https://te-data-test.herokuapp.com/api/sites?token="+os.environ.get("api-token")).json()
    sites = json_data["sites"]
    return sites


def get_signals_from_api(site):
    """Return site signal data."""
    load_dotenv()
    json_data = requests.get(
        "https://te-data-test.herokuapp.com/api/signals?token="+os.environ.get("api-token")+f"&site={site}").json()
    return json_data


def main():
    """Write signal data to local file system in json format every minute. """
    sites = get_sites_from_api()
    site_data = []
    timestamp_now = datetime.now()
    timestamp_file_name = f"signal-{timestamp_now.year}-{timestamp_now.month}-{timestamp_now.day}-{timestamp_now.hour}-{timestamp_now.minute}-{timestamp_now.second}.json"
    for site in sites:
        try:
            site_data.append(get_signals_from_api(site))
        except:
            error_data = {
                'signals': {'SITE_SM_batteryInstPower': None, 'SITE_SM_siteInstPower': None, 'SITE_SM_solarInstPower': None},
                'site': site, 'timestamp': None}
            site_data.append(error_data)

        with open(f"data/{timestamp_file_name}", 'w') as f:
            json.dump(site_data, f)
    return 'success'


schedule.every(30).seconds.do(main)

while(True):
    schedule.run_pending()
    time.sleep(50)
