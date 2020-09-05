from src.file_processing_record import FileProcessingRecord
import json
import boto3
import uuid

RESULTS_TABLE_NAME = "MassTesterResults"


def main(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }


def store_record(record: FileProcessingRecord):
    client = boto3.client('dynamodb')
    response = client.put_item(
        TableName=RESULTS_TABLE_NAME,
        Item=record
    )

def run_test():
    record = FileProcessingRecord(
        guid=uuid.uuid4(),
        file_name="Test",
        engine_return_status=0
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
