def calculate_emissions(route, vehicle_details):
    distance = route['distance']  # in km
    fuel_efficiency = vehicle_details['fuel_efficiency']  # km per liter
    fuel_type = vehicle_details['fuel_type']

    # Emission factors (example values, vary by fuel type)
    emission_factors = {
        "petrol": 2.31,  # kg CO2 per liter
        "diesel": 2.68,  # kg CO2 per liter
        "electric": 0.0  # Assuming no direct emissions
    }

    emissions = (distance / fuel_efficiency) * emission_factors[fuel_type]
    return emissions
