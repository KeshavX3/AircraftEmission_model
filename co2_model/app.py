from flask import Flask, render_template, request
from predict_co2 import predict_co2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        aircraft_type = request.form['aircraft']
        origin = request.form['origin']
        destination = request.form['destination']
        
        
        predicted_emission = predict_co2(aircraft_type, origin, destination)
        
        
        return render_template('index.html', 
                               aircraft=aircraft_type, 
                               origin=origin, 
                               destination=destination, 
                               prediction=predicted_emission)

if __name__ == "__main__":
    app.run(debug=True)
