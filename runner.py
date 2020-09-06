from src.file_processing_record import FileProcessingRecord
import json
import boto3
import uuid
import datetime

RESULTS_TABLE_NAME = "MassTesterResults"


def main(event, context):
    print(f"Event:\n{event}\nConext:\n{context}")
    event_body = json.loads(event.get("body"))

    file_name = event_body.get("file_name")

    run_test(file_name)

    response = {
        "statusCode": 200,
        "body": "item"
    }

    return response


def store_record(record: FileProcessingRecord):
    client = boto3.client('dynamodb')
    response = client.put_item(
        TableName=RESULTS_TABLE_NAME,
        Item=record
    )

def run_test(file_name: str):
    # Logic




    record = FileProcessingRecord(
        timestamp=str(datetime.datetime.now()),
        guid=str(uuid.uuid4()),
        file_name=file_name,
        engine_return_status=0
    )

    store_record(record)
