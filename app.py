from flask import Flask, request, jsonify
import json
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)


@app.route('/')
def home():
    return f"Welcome to my API endpoint"

@app.route('/hello', methods=['GET'])
def hello_get():
    """
    This endpoint returns a greeting message.
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: none
    responses:
      200:
        description: A greeting message
    """
    name = request.args.get('name', 'none')
    return f'Hello {name} here you will get an exmaple of what API endpoints can do!'

@app.route('/calculator', methods=['GET'])
def calculator_get():
    """
    This endpoint returns a simple calculation.
    ---
    parameters:
      - name: number
        in: query
        type: int
        required: false
        default: none
    responses:
      200:
        description: A message multipyling the inputted number by itself
    """
    number = request.args.get('number', 'None')
    number_int = int(number)
    number_calculated = number_int * number_int
    output = json.dumps({
        "number calculated" : number_calculated
    })
    return f'The following endpoint will give you a calculated number of: {output}.  Here to use this endpoint you need to add any number at the end of the url enpoint /calulator?number= in order to multiply it by itself.'


if __name__ == '__main__':
    app.run(debug=True, port=8000)

