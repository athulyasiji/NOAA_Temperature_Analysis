import folium
import os

def create_map(stations, output_path="outputs/map.html"):
    """ Create an interactive map of weather stations. """

    # Ensure the outputs directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Create a folium map centered at Ann Arbor, Michigan
    m = folium.Map(location=[42.2808, -83.7430], zoom_start=10)

    # Add markers for each station
    for name, coord in stations.items():
        folium.Marker(coord, popup=name).add_to(m)

    # Save the map
    m.save(output_path)
    print(f"Map saved as '{output_path}'")

# Example station locations near Ann Arbor, Michigan
stations = {
    "Ann Arbor": [42.2808, -83.7430],
    "Nearby Station 1": [42.3, -83.7],
    "Nearby Station 2": [42.2, -83.6]
}

# Call the function to create and save the map
if __name__ == "__main__":
    create_map(stations)
