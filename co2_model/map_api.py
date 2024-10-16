import requests


NOMINATIM_API_URL = "https://nominatim.openstreetmap.org/search"

OSRM_API_URL = "http://router.project-osrm.org/route/v1/driving"

def get_coordinates(city_name):
    """
    Get the latitude and longitude of a city using Nominatim API.
    
    Args:
    city_name (str): Name of the city.

    Returns:
    tuple: Latitude and Longitude of the city.
    """
    try:
        params = {
            'q': city_name,
            'format': 'json',
            'limit': 1
        }
        response = requests.get(NOMINATIM_API_URL, params=params)
        data = response.json()

        if len(data) > 0:
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            return float(latitude), float(longitude)
        else:
            return None
    except Exception as e:
        print(f"Error in fetching coordinates: {e}")
        return None

def get_distance(origin, destination):
    """
    Calculate the distance between two cities using the OSRM API.
    
    Args:
    origin (str): Starting city.
    destination (str): Destination city.

    Returns:
    float: Distance between the two cities in kilometers or None if an error occurred.
    """
    
    origin_coords = get_coordinates(origin)
    destination_coords = get_coordinates(destination)
    
    print(f"Origin coordinates: {origin_coords}")  
    print(f"Destination coordinates: {destination_coords}")  
    
    
    if origin_coords is None:
        print(f"Error: Unable to find coordinates for origin: {origin}")
        return None
    if destination_coords is None:
        print(f"Error: Unable to find coordinates for destination: {destination}")
        return None

    
    origin_str = f"{origin_coords[1]},{origin_coords[0]}"  
    destination_str = f"{destination_coords[1]},{destination_coords[0]}"  

    try:
        
        response = requests.get(f"{OSRM_API_URL}/{origin_str};{destination_str}", params={'overview': 'false'})
        print(f"Response from OSRM API: {response.text}") 

        if response.status_code == 200:
            data = response.json()
            if 'routes' in data and len(data['routes']) > 0:
                distance_meters = data['routes'][0]['distance']
                distance_km = distance_meters / 1000  
                return distance_km
            else:
                print("No routes found in the response.")
                return None
        else:
            print(f"Error fetching data from OSRM: HTTP {response.status_code}")
            return None
    except Exception as e:
        print(f"Error in calculating distance: {e}")
        return None


# # Example usage (you can test this independently)
# if __name__ == "__main__":
#     origin_city = "Mumbai"
#     destination_city = "Delhi"
    
#     distance = get_distance(origin_city, destination_city)
#     print(f"Distance between {origin_city} and {destination_city}: {distance} km")
