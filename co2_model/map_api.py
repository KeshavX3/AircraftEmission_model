import googlemaps


gmaps = googlemaps.Client(key='YOUR_API_KEY')

def get_distance(origin, destination):
    """
    Calculate the driving distance between two locations using Google Maps API.

    Args:
    origin (str): The starting location (e.g., "Mumbai").
    destination (str): The destination location (e.g., "Delhi").

    Returns:
    float: The distance in kilometers.
    """
    try:
        result = gmaps.distance_matrix(origins=origin, destinations=destination, mode='driving')
        distance_km = result['rows'][0]['elements'][0]['distance']['value'] / 1000  
        return distance_km
    except Exception as e:
        print(f"Error fetching distance: {e}")
        return None
