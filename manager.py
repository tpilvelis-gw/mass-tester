import json
from typing import List

RUNNER_LAMBDA_FUNCTION_NAME = "test-runner"

def spin_up_lambda():
    #initalise_lambda()
    #upload_engine_to_lambda()
    #upload_file_to_lambda()
    return lambda_arn

def load_files() -> List:
    return ['file1', 'file2']
    #from_local()
    # OR
    #from_s3()

def run_test_runner():
    client = boto3.client('lambda')
    client.invoke(
        FunctionName=RUNNER_LAMBDA_FUNCTION_NAME,
        Event="Event"
    )
    return 200


def main(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    
    file_list = load_files()
    engine_location = load_engine()

    successful_spun_up_lambdas = 0
    for file_name in file_list:
        lambda_arn = spin_up_lambda()
        result = run_test_runner(lambda_arn)
        if result == 200:
            successful_spun_up_lambdas += 1
        
    response = {
        "statusCode": 200,
        "body": f"Glasswall Core Test Manager Spun Up Tests: {successful_spun_up_lambdas} / {len(file_list)}"
    }

    return response
