import requests

def getcoors(street_address):
    
    parameters = {"address": street_address}
    response = requests.get("https://maps.googleapis.com/maps/api/geocode/json", params = parameters)
    data=response.json()
    
    ans = parse_content(data)
    
    return ans

def parse_content(data):
    
    ans = {}
    
    main_data = data['results']
    main_data = main_data[0]
    geometry_dict = main_data['geometry']
    location_dict = geometry_dict['location']
    for key, value in location_dict.items():
        ans.setdefault( key, value )
    
    return ans

print(getcoors("hunter college, new york, ny"))
