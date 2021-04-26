# app.py
from flask import Flask, jsonify, redirect, render_template, request

from helpers import testHelper

app = Flask(__name__)

# TODO: replace global with database
INPUT_FEATURES = []

######## HOME ############
@app.route('/')
def home_page():
    example_embed = (
        'This sample string is from Python, passed into HTML frontend via Flask!'
    )
    return render_template('index.html', embed=example_embed)


# Process GET requests for diagnosis
@app.route('/retrieve_diagnosis', methods=['GET'])
def retrieve_diagnosis():
    diagnosis = testHelper(INPUT_FEATURES)
    return jsonify({'diagnosis': diagnosis})


# Process POST request with input features from user
@app.route('/add_feature', methods=['POST'])
def add_feature_old():
    global INPUT_FEATURES
    feature_data = request.get_json()
    INPUT_FEATURES = feature_data
    return 'Done', 201


@app.route('/submitfn', methods=['POST', 'GET'])
def submitfn():
    if request.method == 'POST':
        symp = request.form['tags']  # comma separated string
        print("symp is ", symp, len(symp))
        msg = testHelper(symp)
        return render_template('index.html', disease_output=msg)
    else:
        return redirect('/')


###### Backend Helpers ###########
# Take frontend input and convert to training data point
# input = format_input(frontend_input)

# Elsewhere train and save model e.g. pickle.dump(model, open(filename, 'wb'))
# Load trained model e.g. pickle.load(open(filename, 'rb'))

# Generate model prediction
# output = model.predict(input)

# Pass prediction to front page
# render_template('index.html', output_display=output)

# run app
if __name__ == "__main__":
    app.run(debug=True)
