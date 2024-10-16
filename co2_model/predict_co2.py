from map_api import get_distance


aircraft_emission_factors = {
    'Boeing_747': 0.18,   # CO2 per kilometer
    'Airbus_A380': 0.2    # CO2 per kilometer
}

def predict_co2(aircraft_type, origin, destination):
    """
    Predict CO2 emissions based on aircraft type and distance between origin and destination.

    Args:
    aircraft_type (str): The model/type of the aircraft (e.g., "Boeing_747").
    origin (str): Starting city (e.g., "Mumbai").
    destination (str): Destination city (e.g., "Delhi").

    Returns:
    float: Predicted CO2 emissions.
    """
    
    distance_km = get_distance(origin, destination)
    if distance_km is None:
        return "Error in distance calculation."

    
    emission_factor = aircraft_emission_factors.get(aircraft_type, None)
    if emission_factor is None:
        return "Invalid aircraft type."

    
    predicted_emission = distance_km * emission_factor
    
    return predicted_emission


if __name__ == "__main__":
    aircraft = "Boeing_747"
    origin_city = "Mumbai"
    destination_city = "Delhi"
    
    co2_emission = predict_co2(aircraft, origin_city, destination_city)
    print(f"Predicted CO2 emission: {co2_emission} tons")
