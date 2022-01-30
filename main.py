import json
import requests
from libraries.Response import Response
from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


# @app.route('/test-results')
# def regression_start():
#     return render_template('pas-test-results.html')
#
#
@app.route('/regression-tests')
def regression_start():
    return render_template('regression-tests.html')


@app.route('/about', methods=['GET'])
def default_page():
    message = {
        'status': 'Flask up!'
    }
    return jsonify(message)


@app.route('/pas')
def trigger_pas_regression():
    # response = requests.post('https://test-service.westfield.com/test-run?suite_id=auth_oauth&suite_id=auth_ott')
    #                          'suite_id=account&suite_id=account_app&suite_id=account_credit_cards&suite_id=account_'
    #                          'external_id&suite_id=account_interests&suite_id=account_kids&suite_id=account_loyalty&'
    #                          'suite_id=account_newsletter&suite_id=account_parking&suite_id=account_password&suite_id='
    #                          'account_status&suite_id=account_upgrade&suite_id=account_vehicles&suite_id=people&'
    #                          'suite_id=people_credit_card&suite_id=people_external_ids&suite_id=people_interests&'
    #                          'suite_id=people_kids&suite_id=people_loyalty&suite_id=people_notes&suite_id='
    #                          'people_notifications&suite_id=people_parking&suite_id=people_password_resets&suite_id='
    #                          'people_tickets&suite_id=people_vehicles')
    test_run_id = 1641618757562596763  #response.json()
    response = requests.get(f'https://test-service.westfield.com/test-run?id=1641618757562596763')
    parsed_response = Response().parse_response(response.json())

    # return jsonify(response.json())
    return render_template('pas-test-results.html', initial_response=parsed_response,
                           test_run_id=test_run_id)


if __name__ == '__main__':
    app.run(debug=True)
