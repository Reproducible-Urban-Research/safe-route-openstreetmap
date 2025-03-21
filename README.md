# 🛣️ Safe Route Application

## Overview

**Safe Route** is a Flask-based web application that visualises **safe driving routes** between two locations based on **historical crime data**. It combines **Google Maps routing** with a local crime dataset to help users avoid high-risk areas.

This tool is ideal for researchers, urban planners, and safety-conscious individuals seeking routes that balance distance and safety. It visualises routes using **Folium** (Leaflet.js for Python), with layered maps and interactive crime markers.

---

## ✅ Features

### 📍 Supported Data Sources

- 🧭 Google Maps Directions API – for route options.
- 🧾 CSV crime data – must include `Latitude`, `Longitude`, and crime-related fields.

### ⚙️ Functionality

- 🛣 Route Alternatives – Up to **three routes** shown per query.
- 🔴 Route Safety Colouring:
  - Red = shortest route  
  - Blue = alternative
  - Black = another option  
  - ✅ Green = safest route (least crime)
- 📍 Crime Markers – Visualised near routes, with popups showing detail.
- 🗺 Layer Control – Switch between OpenStreetMap, Stamen, and Carto tile layers.
- 📌 Start/End Markers – Clearly labelled on the map.
- 🧾 Route Instructions – Step-by-step directions embedded in the map.

---

## 📁 Files
This project consists of three main Python files:

- `route.py` contains the core logic for fetching multiple route alternatives using the Google Maps API, analyzing nearby crime data, and ranking routes by safety.
- `draw_map.py` generates an interactive Folium map that visualizes the routes, crime locations, and directions.
- `app.py` is a lightweight Flask server that handles user requests and serves the final map through a web interface.

---

## 📦 Prerequisites

Ensure you have the following:

- Python 3.x
- A valid Google Maps API Key
- A local crime dataset file named `Updated_Crimes.csv` with crime location data

### Required Python Libraries

All required Python packages (and their specific versions) are listed in the `requirements.txt` file.

To install all dependencies:

```bash
pip install -r requirements.txt
```

This ensures consistent and reproducible environments across machines.

---

## 🛠 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Reproducible-Urban-Research/safe-route-openstreetmap.git
cd safe-route-openstreetmap
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Google Maps API Key

In `route.py`, replace:

```python
gmaps = googlemaps.Client(key='YOUR_GOOGLE_MAPS_API_KEY')
```

with your own API key from Google Cloud Platform.

---

## 🚀 Usage

### 🖥️ Start the Flask App

Run the Flask server:

```bash
python app.py
```

Then open your browser and visit:

```
http://localhost:5000/safe_route?source=<SOURCE>&destination=<DESTINATION>
```

Replace `<SOURCE>` and `<DESTINATION>` with actual place names or addresses.  
Use **`+` instead of spaces** between words.

#### ✅ Example

```
http://localhost:5000/safe_route?source=FREEDOM+SQUARE+PLAYGROUND,+NY&destination=BLEECKER+PLAYGROUND,+NY
```

This will display up to 3 route options between **Freedom Square Playground** and **Bleecker Playground** in New York, with crime data visualised on the map.

---

## 🗺️ Map Output

- Up to **3 routes** plotted on the map  
- Crime markers near the route (within ~500m)  
- Colour-coded routes with start/end points  
- Clickable steps and popups for direction and risk details  
- Switchable basemaps

---

## 📂 Crime Data Format

Your crime data must be in **CSV format**.

### Required Columns:

| Column Name | Description         |
|-------------|---------------------|
| Latitude    | Latitude (float)    |
| Longitude   | Longitude (float)   |
| [Other]     | Crime types/counts  |

📄 **File name must be**:

```
Updated_Crimes.csv
```

📁 **Place it in the root directory** of the project.

### Example row:

```
Latitude,Longitude,Burglary,Theft
40.748817,-73.985428,2,5
```

---

## 📍 Example Query

Try this in your browser after running the app:

```
http://127.0.0.1:5000/safe_route?source=Times+Square,+NY&destination=Central+Park,+NY
```

---

## 🎨 Visualisation Adjustments

You can customise how the map looks and behaves:

- 🗺️ **Map Style** – Choose from OpenStreetMap, Stamen Terrain, Toner, Watercolor, CartoDB, etc.
- 📍 **Crime Marker Filtering** – Crime points are filtered within a configurable distance from each route (default: 500m)
- 🎯 **Route Highlighting** – Safest route is highlighted in green with step-by-step markers

---

## ⚙️ Configuration Options

You can adjust the following options to customise the behaviour and appearance of the map.  
These settings can be found in either `route.py` or `draw_map.py`.

### 🔧 route.py

| Parameter         | Description                                                      | Default / Example |
|-------------------|------------------------------------------------------------------|-------------------|
| `search_radius_m` | Radius (in metres) to filter nearby crimes along each route      | `500`             |
| `max_routes`      | Maximum number of alternative routes to display (1–3)            | `3`               |

### 🎨 draw_map.py

| Parameter            | Description                                                | Default / Example                |
|----------------------|------------------------------------------------------------|----------------------------------|
| `map_center`         | Default map centre coordinates when the app starts         | `[40.730610, -73.935242]` (NYC) |
| `zoom_start`         | Initial zoom level for the map                             | `12`                             |
| `route_colors`       | Colours used for drawing each route (in order)             | `['Red', 'Blue', 'Black']`       |
| `safest_route_color` | Colour used to highlight the safest route                  | `'Green'`                        |
| `crime_icon_color`   | Marker icon colour for crime locations                     | `'red'`                          |
| `tile_layers`        | List of base map layers user can switch between            | `OpenStreetMap`, `Stamen`, etc. |

> 🎛️ You can modify these parameters directly in the Python files for simple customisation.

---

## 🧪 Example Data

Looking for sample crime data?

You can:

- Use **Open Data portals** like [NYC OpenData](https://opendata.cityofnewyork.us/), [UK Police API](https://data.police.uk/), or [Chicago Data Portal](https://data.cityofchicago.org/)
- Generate synthetic data for testing
- Manually collect from **OpenStreetMap** using **Overpass API** (for places of interest, not crime)

---

## 🙋‍♀️ Maintainer

Originally adapted from [electroBakuza/safe-route-openstreetmap](https://github.com/electroBakuza/safe-route-openstreetmap)

Maintained and extended by [Yuchi Lai](https://github.com/Yuchi-Lai)  
For [Reproducible Urban Research](https://github.com/Reproducible-Urban-Research)


## 📫 Feedback

Feel free to open an [Issue](https://github.com/Reproducible-Urban-Research/safe-route-openstreetmap/issues) or submit a pull request for suggestions and improvements!