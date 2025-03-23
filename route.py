import pandas as pd
import numpy as np
import googlemaps
import polyline
from datetime import datetime

gmaps = googlemaps.Client(key='YOUR_GOOGLE_API_KEY')

# Load the crime dataset
crime_data = pd.read_csv('Updated_Crimes.csv')
total_crime = crime_data['Total Crime']
crime_locs = crime_data[['Latitude', 'Longitude']]

# === Crime marker tag function ===
def crime_list(route_points, crime_df):
    crimes_tags_list = []
    seen = set()
    for p in route_points:
        row_mask = (np.isclose(crime_df['Latitude'], p[0], rtol=1e-3)) & \
                   (np.isclose(crime_df['Longitude'], p[1], rtol=1e-3))

        if True in row_mask:
            lat = crime_df['Latitude'][row_mask].values[0]
            lon = crime_df['Longitude'][row_mask].values[0]

            if (lat, lon) in seen:
                continue
            seen.add((lat, lon))

            tag = {
                'Murder': crime_df['Murder '][row_mask].values[0],
                'Rape': crime_df['Rape'][row_mask].values[0],
                'Robbery': crime_df['Robbery'][row_mask].values[0],
                'Kidnapping': crime_df['Kidnapping'][row_mask].values[0],
                'Harassment': crime_df['Harassment'][row_mask].values[0],
                'Latitude': lat,
                'Longitude': lon
            }

            if any(tag[k] != 0 for k in ['Murder', 'Rape', 'Robbery', 'Kidnapping', 'Harassment']):
                crimes_tags_list.append(tag)

            crime_df = crime_df.drop(crime_df[row_mask].index)

    print("tags count:", len(crimes_tags_list))
    return crimes_tags_list, crime_df

# === Sum route crime ===
def sum_crime_for_route(route_points):
    crimes = [
        total_crime[
            (np.isclose(crime_locs['Latitude'], p[0], rtol=1e-3)) &
            (np.isclose(crime_locs['Longitude'], p[1], rtol=1e-3))
        ].sum()
        for p in route_points
    ]
    return sum(crimes)

# === Probability ===
def crime_probability(sum_crime):
    total_sum = total_crime.sum()
    return (sum_crime / total_sum) if total_sum > 0 else 0

# === Main route function ===
def get_top_routes(start_loc, end_loc):
    directions_result = gmaps.directions(
        start_loc, end_loc,
        mode="driving",
        departure_time=datetime.now(),
        alternatives=True
    )

    dynamic_crime_data = crime_data.copy()
    routes = []

    for route in directions_result:
        duration = route['legs'][0]['duration']['value']
        steps = route['legs'][0]['steps']
        route_points = []

        for step in steps:
            decoded = polyline.decode(step['polyline']['points'])
            route_points.extend(decoded)

        sum_crime = sum_crime_for_route(route_points)
        tags, dynamic_crime_data = crime_list(route_points, dynamic_crime_data)
        prob = crime_probability(sum_crime)

        routes.append({
            'steps': steps,
            'duration': duration,
            'points': route_points,
            'probability': prob,
            'tags': tags
        })

    # Sort by risk, add safest to end
    sorted_routes = sorted(routes, key=lambda x: x['probability'], reverse=True)
    top_3 = sorted_routes[:3]
    top_3.append(sorted_routes[-1])  # safest one at end

    return [
        {
            'steps': r['steps'],
            'route_points': r['points'],
            'duration': r['duration'],
            'probability': r['probability'],
            'tags': r['tags']
        }
        for r in top_3
    ]
