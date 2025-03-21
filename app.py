from flask import Flask, request, render_template
from draw_map import get_map

app = Flask(__name__)

@app.route("/safe_route")
def safe_route():
    source = request.args.get('source')
    destination = request.args.get('destination')

    if not source or not destination:
        return "Please provide both source and destination addresses in the URL."

    # Generate map
    get_map(source, destination)

    # Render the map in HTML template
    return render_template('routes.html')

# ✅ Add this part to actually start the server
if __name__ == "__main__":
    app.run(debug=True)