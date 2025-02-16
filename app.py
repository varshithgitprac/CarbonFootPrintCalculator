import webbrowser
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import threading

app = Flask(__name__)
CORS(app)

# CO2 Emission Factors (kg CO₂ per unit)
EMISSION_FACTORS = {
    "car_km": 2.3,
    "bus_km": 0.3,
    "electricity_kwh": 0.9,
    "beef_kg": 27,
    "chicken_kg": 6.9
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    """Calculate the carbon footprint based on user input."""
    data = request.json  
    total_emissions = sum(
        data[key] * EMISSION_FACTORS[key] for key in data if key in EMISSION_FACTORS
    )

    return jsonify({"total_emissions": round(total_emissions, 2)})

# Function to open the browser automatically
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()  # Open browser after 1.5 seconds
    app.run(debug=True)
