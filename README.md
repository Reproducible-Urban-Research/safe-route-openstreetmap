# Safe Route Application (openstreetmap)

## Overview

This application identifies and visualizes safe driving routes between two locations based on crime data. Using Google Maps API and a local dataset, it calculates crime probabilities along possible routes and plots the routes on an interactive map using the Folium library. The application is built with Flask for the web interface.

![Route Visualization](./2024-10-16_23-49.png)

![Route Visualization](./2024-10-16_23-52.png)

## Features

- **Route Selection**: Suggests alternative routes between two locations.
- **Crime Probability**: Calculates the likelihood of encountering crime based on historical data.
- **Interactive Map**: Displays routes on a map with crime markers at high-risk locations.
- **Multiple Map Layers**: Users can switch between different map views such as OpenStreetMap, Stamen Terrain, and others.
- **Route Directions**: Displays step-by-step directions with popup markers for visual guidance.

## Prerequisites

- Python 3.x
- Required Libraries:
  - `pandas`
  - `numpy`
  - `googlemaps`
  - `folium`
  - `Flask`
  - `polyline`

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-repo/crime-mapping.git
   cd crime-mapping
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Maps API Key**:
   Replace the placeholder API key in `route.py` with your Google Maps API key:

   ```python
   gmaps = googlemaps.Client(key='YOUR_GOOGLE_MAPS_API_KEY')
   ```

4. **Add crime data**:
   Ensure you have a CSV file named `Updated_Crimes.csv` in the root of your project. This file should contain crime data with latitude, longitude, and crime type columns.

## Usage

1. **Start the Flask server**:

   ```bash
   python app.py
   ```

2. **Access the web interface**:
   Open a web browser and navigate to `http://localhost:5000/safe_route?source=<source_location>&destination=<destination_location>`, replacing `<source_location>` and `<destination_location>` with valid addresses.

3. **Interactive Map**:
   The map will display up to three routes with crime markers:

   - **Red Route**: Shortest route.
   - **Blue Route**: Alternative route.
   - **Black Route**: Another alternative with low risk.

   Crime markers will appear at locations along the routes where crimes have been reported.

## Files

- **route.py**: Contains the logic to fetch routes, calculate crime probability, and return top routes based on crime data.
- **draw_map.py**: Plots the selected routes on an interactive Folium map and adds markers for high-crime locations.
- **app.py**: Flask web server that serves the crime-mapped routes to users via an HTML interface.

## Example

You can test the application using a URL like this:

```bash
http://localhost:5000/safe_route?source=FREEDOM+SQUARE+PLAYGROUND,+NY&destination=BLEECKER+PLAYGROUND,+NY
```

This will calculate and display the safest routes between the two locations based on the crime data.
# 🚗 Safe Route Application (Openstreetmap)

## 📌 Overview
Safe Route Application helps drivers find and visualise **safe driving routes** by analysing crime data. It uses **Google Maps API** and local **crime datasets** to calculate crime probabilities along different routes and display them on an **interactive map** using **Folium**.

This tool is ideal for users who want to avoid high-crime areas while navigating between two locations.

---

## ✅ Features

- **📍 Route Selection** – Generates **alternative routes** based on distance and crime risk.
- **🛑 Crime Probability Calculation** – Estimates crime likelihood on each route using historical data.
- **🗺 Interactive Map View** – Displays routes on an **interactive map** with crime markers.
- **🔄 Multiple Map Layers** – Users can switch between OpenStreetMap, Stamen Terrain, and other views.
- **📌 Step-by-Step Route Directions** – Provides navigation guidance with pop-up markers.

---
## Prerequisites
### Environment Setup

- **Python Version**: 3.x

### Required Libraries

Make sure to install the following Python libraries:

- `pandas`
- `numpy`
- `googlemaps`
- `folium`
- `Flask`
- `polyline`

---
## 📌 Installation

To install **Safe Route Application**, follow these steps:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-repo/crime-mapping.git
cd crime-mapping
```

### 2️⃣ (Optional) Create a Virtual Environment

It's recommended to use a virtual environment to isolate project dependencies.

1. **Create a virtual environment** (only required once):

    ```bash
    python -m venv venv
    ```

2. **Activate the virtual environment**:

    - On **Windows**:

        ```bash
        venv\Scripts\activate
        ```

    - On **macOS/Linux**:

        ```bash
        source venv/bin/activate
        ```

3. Then proceed with installing dependencies below.  
   To **deactivate** the virtual environment when you're done, simply run:

    ```bash
    deactivate
    ```


### 3️⃣ Install Dependencies
Install all required packages along with their specified versions listed in requirements.txt by running the following command:
```bash
pip install -r requirements.txt
```
This ensures your environment matches the project's dependencies and avoids compatibility issues.

> ⚠️ **Note:** If you encounter an error related to `arabic-reshaper==2.1.3`, it's because `pip` version 24.1 and above strictly validate package metadata, and that version of the package has a known metadata issue.  
>
> To resolve this, downgrade `pip` to a version below 24.1 (e.g., 23.3.2) with the following command:
>
> ```bash
> pip install pip==23.3.2
> ```
>
> This allows the installation to proceed without modifying the `requirements.txt` file.
>
>🔍 Additional: How to check your pip version
>You can check your current pip version by running:
> ```
>pip --version
>```
>If your version is 24.1 or above, it's recommended to downgrade as shown above.


### 4️⃣ Set up Google Maps API Key
- Open `route.py`
- Replace the placeholder API key with your Google Maps API key:
```python
gmaps = googlemaps.Client(key='YOUR_GOOGLE_MAPS_API_KEY')
```
- [How to find your Google API key ➤](#how-to-find-your-google-api-key)


### 5️⃣ Ensure crime data is available
- Place a `Updated_Crimes.csv` file in the project root directory.
- The file should contain:
```csv
latitude,longitude,crime_type
40.7128,-74.0060,Robbery
40.7139,-74.0050,Assault
```

---

## 🚀 Usage

### 🛣 1️⃣ Get Safe Routes Between Two Locations

To view safe routes, open a browser and enter:
```
http://localhost:5000/safe_route?source=<source_location>&destination=<destination_location>
```
✅ Example:
```bash
http://localhost:5000/safe_route?source=FREEDOM+SQUARE+PLAYGROUND,+NY&destination=BLEECKER+PLAYGROUND,+NY
```

🗺 **The map will display:**
- **🔴 Red Route** – The shortest route, but may pass through high-crime areas.
- **🔵 Blue Route** – An alternative route with moderate risk.
- **⚫ Black Route** – The safest route with low crime probability.

---

### 🌍 2️⃣ View Interactive Map & Crime Hotspots

Run the Flask server:
```bash
python app.py
```
Then, open the map in a browser. Crime locations will be marked, allowing you to **avoid high-risk zones**.

---

## 📂 API Endpoints & Parameters

### 🔹 API Endpoint
```
GET /safe_route?source=<source>&destination=<destination>
```

### 🔹 Supported Query Parameters

| Parameter       | Description                                      | Example         |
|---------------|----------------------------------|--------------|
| `source` | Starting location (address or lat/lon) | `"New York, NY"` |
| `destination` | Ending location (address or lat/lon) | `"Brooklyn, NY"` |
| `mode` | Travel mode: `driving`, `walking`, `bicycling` | `driving` |
| `avoid_highways` | Avoids motorways if set to `true` | `false` |
| `avoid_tolls` | Avoids toll roads if set to `true` | `true` |

### 🔹 Example JSON Response
```json
{
  "routes": [
    {
      "name": "Shortest Route",
      "colour": "red",
      "distance": "12.5 km",
      "time": "18 min",
      "crime_score": 7.2,
      "polyline": "encoded_polyline_string"
    },
    {
      "name": "Safer Route",
      "colour": "blue",
      "distance": "14.3 km",
      "time": "21 min",
      "crime_score": 5.1,
      "polyline": "encoded_polyline_string"
    }
  ],
  "crime_markers": [
    { "latitude": 40.7128, "longitude": -74.0060, "crime_type": "Robbery" },
    { "latitude": 40.7139, "longitude": -74.0050, "crime_type": "Assault" }
  ]
}
```

---

## 🛑 Error Handling

| Error | Cause | Response Example |
|-------|-------|----------------|
| `400 Bad Request` | Missing required parameters | `{ "error": "Missing source or destination" }` |
| `404 Not Found` | No safe routes found | `{ "error": "No routes available for this area" }` |
| `500 Server Error` | Internal issues with the API | `{ "error": "Unexpected server error. Please try again later." }` |

---

## 🔬 How Crime Probability is Calculated
- Each route is analysed using **crime density per road segment**.
- **Historical crime data** from `Updated_Crimes.csv` is used.
- Routes are **scored based on the number & severity of crimes nearby**.
- A weighted risk factor determines **the safest alternative routes**.

---

## 🚀 Deployment Options

### **Run with Docker**
Create a `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```
Build and run the container:
```bash
docker build -t safe-route-app .
docker run -p 5000:5000 safe-route-app
```


---

## 📖 FAQs & Troubleshooting

> **Q: How can I get my Google Maps API key?**
> A: 

> **Q: Why is my API key not working?**  
> A: Make sure you’ve enabled **Google Maps API & Geocoding API** in the Google Cloud Console.

> **Q: No routes found between locations?**  
> A: Try using different locations or ensure your API key is active.

---

## 🌟 Future Enhancements
✅ Live crime data integration  
✅ User feedback for route adjustments  
✅ Mobile-friendly web UI  

---

## 📜 Licence
This project is licensed under the **MIT Licence**.