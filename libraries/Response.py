import json
import requests
import curlify


class Response:

    def __init__(self):
        self.status_code = None
        self.number_of_tests = 0

    @staticmethod
    def parse_response(response):
        results = {}
        overview = {}
        parsed_results = {
            'overview': overview,
            'details': results

        }

        for suite in response['run_details']:
            end_point = suite["execution_path"].split("/")[-2].split('.')[0]
            file_name = suite["execution_path"].split("/")[-1].split('.')[0]
            print(
                f'* Test file: * {suite["execution_path"].split("/")[-1]} * Number of tests {len(suite["report"]["tests"])}')
            print('\t| status | test names ')
            number_of_tests = len(suite['report']['tests'])
            results.update({
                file_name: {
                    'swagger end point': end_point,
                    'number of tests': number_of_tests
                }
            })
            test_cases = []
            for test in suite['report']['tests']:
                print(f'\t| {test}')

                test_cases.append(test)
            results[file_name].update({
                'results': test_cases
            })
            print('')
        print(f'\nTotal number of test suites  : {len(response["run_details"])}')
        print(f'total number of tests        : {response["total"]}\n')
        print(f'total passed number of tests : {response["passed"]}')
        print(f'total failed number of tests : {response["failed"]}')
        print(f'total number of tests errors : {response["error"]}')
        print(f'percent passing              : {response["percent_pass"]:.2f}')
        overview.update({
            'id': response['id'],
            'status': response['status'],
            'percent passing': round(response["percent_pass"], 2),
            'total number of tests': response["total"],
            'total number of test suites': len(response["run_details"]),
            'total passed number of tests': response["passed"],
            'total failed number of tests': response["failed"],
            'total number of tests errors': response["error"],

        })
        return json.dumps(parsed_results, indent=4)

    @staticmethod
    def debug_response(response, display_500_response=False):
        print('*-------------------')
        print(f'* URL              : {response.url}')
        print(f'* Request headers  : {response.request.headers}')
        print(f'* Request method   : {response.request.method}')
        print(f'* Status code      : {response.status_code}')
        print(f'* Request curl     : {curlify.to_curl(response.request)}')
        print(f'* Request body     : {response.request.body}')
        print(f'* Response time    : {response.elapsed.total_seconds()}')
        print(f'* Response headers : {response.headers}')
        if response.status_code == requests.codes.internal_server_error and display_500_response is False:
            print('* Response body    : 500 response body not displayed by default.\n'
                  '*                  : Set DebugLog display_500_response=True')
        else:
            print(f'* Response body    : {response.text}')
        print('*-------------------')

