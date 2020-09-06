import json
from typing import List
import boto3
import os
from src.manifest import Manifest

RUNNER_LAMBDA_FUNCTION_NAME = "glasswall-core-mass-tester-l-dev-test-runner"
DATA_DIR = "data"

def spin_up_lambda(manifest: Manifest):
    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName=RUNNER_LAMBDA_FUNCTION_NAME,
        InvocationType="Event",
        Payload=manifest.payload()
    )
    return response


def from_local() -> List:
    data_dir = os.path.join(os.curdir, DATA_DIR)
    if not os.path.isdir(data_dir):
        print("No Directory or Cannot Locate Data Directory")
        return []
    contents = os.listdir(data_dir)
    return contents


def load_files() -> List:
    return from_local()
    #from_s3()


def main(event, context):
    print("Starting Manager...")    

    file_list = load_files()
    print(f"Files Loaded: {len(file_list)}")

    print("Spinning Up Lambda...")
    for file_name in file_list:
        manifest = Manifest(
            engine="libglasswall.classic.so",
            file_name=file_name
        )

        spin_up_lambda(manifest)



    print(f"Lambda {RUNNER_LAMBDA_FUNCTION_NAME} Running...")
    #engine_location = load_engine()

    #successful_spun_up_lambdas = 0
    #for file_name in file_list:
    #    lambda_arn = spin_up_lambda()
    #    result = run_test_runner(lambda_arn)
    #    if result == 200:
    #        successful_spun_up_lambdas += 1
    #f"Glasswall Core Test Manager Spun Up Tests: {successful_spun_up_lambdas} / {len(file_list)}"
    
    print("Ending Manager...")
    response = {
        "statusCode": 200,
        "body": json.dumps(event)
    }

    return response

