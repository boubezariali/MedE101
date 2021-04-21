# app.py
from flask import Flask, jsonify, request, render_template, redirect
app = Flask(__name__)


######## HOME ############
@app.route('/')
def home_page():
    example_embed='This sample string is from Python, passed into HTML frontend via Flask!'
    return render_template('index.html', embed=example_embed)

@app.route('/tester')
def tester_page():
    items = ['heart attack', 'stroke', 'asthma']
    json = jsonify({'test_items': items})
    return json

@app.route('/add_feature', methods = ['POST'])
def add_feature():
    feature_data = request.get_json()
    # Do something with posted feature data
    print("feature_data: ", feature_data)
    return 'Done', 201


@app.route('/submitfn', methods = ['POST', 'GET'])
def submitfn():
    if request.method == 'POST':
        symp = request.form['tags'] # comma separated string
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


# Dummy to test processing input data
def testHelper(input):
    diseases = ["heart attack", "flu", "cancer", "allergy"]
    pick = len(input) % len(diseases)
    return diseases[pick]



# run app
if __name__ == "__main__":
    app.run(debug=True)