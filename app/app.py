# app.py
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)


######## HOME ############
@app.route('/')
def home_page():
    example_embed='This sample string is from Python, passed into HTML frontend via Flask!'
    return render_template('index.html', embed=example_embed)

######## Example fetch ############
@app.route('/test', methods=['GET', 'POST'])
def testfn():
    message = "default"

    # POST request
    if request.method == 'POST':
        print(request.get_json())
        message = ('OK', 200)
    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
    return render_template('test_page.html', mylog=message)


# run app
if __name__ == "__main__":
    app.run(debug=True)