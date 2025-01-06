def optimize_routes(api_data, vehicle_details):
    routes = api_data['routes']
    traffic = api_data['traffic']
    weather = api_data['weather']

    # Evaluate routes based on a custom cost function
    optimized_routes = []
    for route in routes:
        route_score = calculate_route_score(route, traffic, weather, vehicle_details)
        optimized_routes.append({
            "route": route,
            "score": route_score
        })

    return sorted(optimized_routes, key=lambda x: x['score'])

def calculate_route_score(route, traffic, weather, vehicle_details):
    # Custom scoring function for routes
    return route['distance'] / (1 + traffic['congestion']) + weather['impact']
