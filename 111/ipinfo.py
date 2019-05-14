import json

import requests

IPINFO_URL = 'http://ipinfo.io/{}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    useableUrl = IPINFO_URL.format(ip_address)
    ipInfoGetRequest = requests.get(useableUrl)
    json_dict = ipInfoGetRequest.json()
    for k, v in json_dict.items():
        if k == 'country':
            return v
