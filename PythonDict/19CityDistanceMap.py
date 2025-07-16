# Initial city distance data
distances = {
    "Chennai": {"Bangalore": 350, "Delhi": 2200},
    "Bangalore": {"Chennai": 350, "Hyderabad": 575},
    "Delhi": {"Chennai": 2200}
}

# 1. Query distance between two cities
def get_distance(city1, city2):
    dist = distances.get(city1, {}).get(city2)
    if dist is not None:
        print(f"Distance from {city1} to {city2} is {dist} km.")
    else:
        print(f"No direct route from {city1} to {city2}.")

# 2. Update distance
def update_distance(city1, city2, new_dist):
    distances.setdefault(city1, {})[city2] = new_dist
    print(f"Distance from {city1} to {city2} updated to {new_dist} km.")

# 3. Find shortest route from a city
def shortest_route(city):
    city_routes = distances.get(city, {})
    if city_routes:
        shortest = min(city_routes.items(), key=lambda x: x[1])
        print(f"Shortest route from {city} is to {shortest[0]}: {shortest[1]} km")
    else:
        print(f"No outgoing routes from {city}.")

# Operations
get_distance("Chennai", "Delhi")
update_distance("Chennai", "Hyderabad", 630)
shortest_route("Chennai")
