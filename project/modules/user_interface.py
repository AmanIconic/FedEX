def get_user_input():
    vehicle_details = {
        "fuel_type": input("Enter fuel type (petrol/diesel/electric): "),
        "fuel_efficiency": float(input("Enter fuel efficiency (km per liter): "))
    }
    trip_details = {
        "start_point": input("Enter start point: "),
        "destination": input("Enter destination: "),
        "waypoints": input("Enter waypoints (comma-separated, optional): ").split(",")
    }
    return vehicle_details, trip_details

def display_results(routes):
    print("\nOptimal Routes:")
    for idx, route in enumerate(routes, 1):
        print(f"Route {idx}:")
        print(f"  Distance: {route['route']['distance']} km")
        print(f"  Time: {route['route']['time']} minutes")
        print(f"  Emissions: {route['emissions']} kg CO2")
