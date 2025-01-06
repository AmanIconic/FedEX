import requests
from modules.api_integration import fetch_data
from modules.route_optimizer import optimize_routes
from modules.emissions_calculator import calculate_emissions
from modules.user_interface import get_user_input, display_results

def main():
    # Get user input
    vehicle_details, trip_details = get_user_input()

    # Fetch real-time data
    api_data = fetch_data(trip_details)

    # Optimize routes
    optimal_routes = optimize_routes(api_data, vehicle_details)

    # Calculate emissions
    for route in optimal_routes:
        route['emissions'] = calculate_emissions(route, vehicle_details)

    # Display results
    display_results(optimal_routes)

if __name__ == "__main__":
    main()
