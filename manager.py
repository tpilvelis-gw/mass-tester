import json
from typing import List
import boto3
import os
from src.manifest import Manifest

ENGINE_NAME = "libglasswall.classic.so"
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
    files_list = []
    for root, folders, files in os.walk("data"):
        for eachFile in files:
            filepath = os.path.join(root, eachFile)
            files_list.append(filepath)
    return files_list


def load_files() -> List:
    return from_local()
    #from_s3()


def main(event, context):
    print("Starting Manager...")    

    file_list = load_files()
    print(f"Files Loaded: {len(file_list)}")

    for file_path in file_list:
        manifest = Manifest(
            engine_path=os.path.join("lib", ENGINE_NAME),
            file_path=file_path
        )
        print(f"Spinning Up Lambda for {manifest.payload()}...")
        spin_up_lambda(manifest)

    print("Ending Manager...")
    response = {
        "statusCode": 200,
        "body": json.dumps(event)
    }

    return response

