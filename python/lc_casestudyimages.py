import requests

def get_image_urls(url, items=[]):
    params = {"fo": "json", "c": 100, "at": "results,pagination"}
    call = requests.get(url, params=params)
    data = call.json()
    results = data["results"]
    for result in results:
        if "collection" not in result.get("original_format") and "webpage" not in result.get("original_format"):
            if result.get("image_url"):
                    item = result.get("image_url")[-1]
                    items.append(item)

    if data["pagination"]["next"] is not None:
        next_url = data["pagination"]["next"]
        print("getting next page: {0}".format(next_url))
        get_image_urls(next_url, items)

    return items

image_urls = get_image_urls("https://www.loc.gov/search/?in=&q=everyman&new=true", items=[])

#print(len(image_urls))

#print(image_urls[:5])

#import json
#r = requests.get("https://www.loc.gov/item/ihas.200216876/?fo=json")
#r_data = r.json()

#print(json.dumps(r_data["item"]["rights_information"], indent=2))
#print(json.dumps(r_data["item"]["rights_advisory"], indent=2))
#print(json.dumps(r_data["item"]["rights"], indent=2))
#print(json.dumps(r_data["item"]["restriction"], indent=2))

import os

def get_image_files(image_urls_list, path):
    for count, url in enumerate(image_urls_list):
        if count % 100 == 0:
            print("at item {0}".format(count))
        try:
            filename = url.split('/')[-1]
            filename = os.path.join(path, filename)
