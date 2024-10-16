import requests

# Nominatim API URL for geocoding
NOMINATIM_API_URL = "https://nominatim.openstreetmap.org/search"
# OSRM API URL for route distance calculation
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
    Calculate the driving distance between two cities using OSRM API.
    
    Args:
    origin (str): Starting city.
    destination (str): Destination city.

    Returns:
    float: Distance between the two cities in kilometers.
    """
    origin_coords = get_coordinates(origin)
    destination_coords = get_coordinates(destination)
    
    if origin_coords and destination_coords:
        origin_str = f"{origin_coords[1]},{origin_coords[0]}"  # lon,lat
        destination_str = f"{destination_coords[1]},{destination_coords[0]}"  # lon,lat

        try:
            # Send a request to OSRM API for the distance
            response = requests.get(f"{OSRM_API_URL}/{origin_str};{destination_str}", params={'overview': 'false'})
            data = response.json()

            if 'routes' in data and len(data['routes']) > 0:
                distance_meters = data['routes'][0]['distance']
                distance_km = distance_meters / 1000  # Convert meters to kilometers
                return distance_km
            else:
                return None
        except Exception as e:
            print(f"Error in calculating distance: {e}")
            return None
    else:
        return None

# Example usage (you can test this independently)
if __name__ == "__main__":
    origin_city = "Mumbai"
    destination_city = "Delhi"
    
    distance = get_distance(origin_city, destination_city)
    print(f"Distance between {origin_city} and {destination_city}: {distance} km")
