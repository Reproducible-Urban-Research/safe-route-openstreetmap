from route import get_top_routes
import folium
from folium.plugins import PolyLineTextPath

def get_map(source, destination):
    # Get top routes based on crime probability
    top_routes = get_top_routes(source, destination)

    if len(top_routes) < 3:
        raise ValueError("Expected at least 3 route options. Found fewer.")

    # Create map with light base layer
    nyc_map = folium.Map(
        location=[40.730610, -73.935242],  # Centered at NYC
        zoom_start=12,
        tiles="cartodbpositron",
        attr="Map tiles by CartoDB, under CC BY 3.0. Data © OpenStreetMap"
    )

    # Add route polylines
    colors = ['Red', 'Blue', 'Black']
    for idx, color in enumerate(colors):
        route_points = top_routes[idx]['route_points']
        folium.PolyLine(
            locations=route_points,
            weight=3,
            color=color,
            dash_array='10,10'
        ).add_to(nyc_map)

    # Add safest route in green
    safest_route = top_routes[-1]
    route_points = safest_route['route_points']
    folium.PolyLine(
        locations=route_points,
        weight=4,
        color='Green',
        dash_array='5,5'
    ).add_to(nyc_map)

    # Add step instructions for safest route
    for step in safest_route['steps']:
        popup_html = f"""
            <div style="background-color: #fff;
                        border: 2px solid #000;
                        border-radius: 5px;
                        padding: 10px;
                        font-family: Arial, sans-serif;">
                {step.get('html_instructions', '')}
            </div>
        """
        folium.Marker(
            location=(step['end_location']['lat'], step['end_location']['lng']),
            tooltip=popup_html,
            icon=folium.Icon(icon='info-sign')
        ).add_to(nyc_map)

    # Add crime markers for each route
    for route in top_routes:
        for tag in route['tags']:
            crimes = "\n".join([f"{k}: {v}" for k, v in tag.items() if k not in ['Latitude', 'Longitude']])
            popup_html = f"""
                <div style="background-color: #fff;
                            border: 2px solid #000;
                            border-radius: 5px;
                            padding: 10px;
                            font-family: Arial, sans-serif;">
                    {crimes}
                </div>
            """
            folium.Marker(
                location=(tag['Latitude'], tag['Longitude']),
                popup=crimes,
                tooltip=popup_html,
                icon=folium.Icon(icon='glyphicon-warning-sign', color='red')
            ).add_to(nyc_map)

    # Add start and end markers
    start = safest_route['route_points'][0]
    end = safest_route['route_points'][-1]

    folium.Marker(
        location=start,
        popup="Start",
        tooltip="Start",
        icon=folium.Icon(color="green", icon="play")
    ).add_to(nyc_map)

    folium.Marker(
        location=end,
        popup="End",
        tooltip="End",
        icon=folium.Icon(color="red", icon="stop")
    ).add_to(nyc_map)

    # Add optional tile layers
    folium.TileLayer(
        tiles='Stamen Terrain',
        name='Stamen Terrain',
        attr='Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap'
    ).add_to(nyc_map)

    folium.TileLayer(
        tiles='Stamen Toner',
        name='Stamen Toner',
        attr='Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap'
    ).add_to(nyc_map)

    folium.TileLayer(
        tiles='Stamen Watercolor',
        name='Stamen Watercolor',
        attr='Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap'
    ).add_to(nyc_map)

    folium.TileLayer(
        tiles='cartodbdark_matter',
        name='Carto Dark',
        attr='Map tiles by CartoDB, under CC BY 3.0. Data © OpenStreetMap'
    ).add_to(nyc_map)

    # Add layer control (for toggling base maps)
    folium.LayerControl().add_to(nyc_map)

    # Save the map to the templates directory
    nyc_map.save("./templates/routes.html")
