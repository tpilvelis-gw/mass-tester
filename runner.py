from src.file_processing_record import FileProcessingRecord
from src.Glasswall import Glasswall
import json
import boto3
import uuid
import datetime
import os

RESULTS_TABLE_NAME = "MassTesterResults"

def store_record(record: FileProcessingRecord):
    client = boto3.client('dynamodb')
    response = client.put_item(
        TableName=RESULTS_TABLE_NAME,
        Item=record
    )

def run_test(file_path: str, engine_path: str):
    # Logic
    if not os.path.isfile(engine_path):
        print("engine path is invalid...")
        return
    
    print("Loading Library...")
    gw = Glasswall(engine_path)
    print("Done!")

    configFile = open("config.xml", "r")
    xmlContent = configFile.read()
    configFile.close()

    configXMLResult = gw.GWFileConfigXML(xmlContent)

    if configXMLResult.returnStatus != 1:
        print("Failed to apply the content management configuration for the following reason: " + gw.GWFileErrorMsg())
        return

    print("Processing file: " + file_path)
    fileExtension = file_path.split(".")[1]

    manageAndProtectResult = gw.GWFileProtect(file_path, fileExtension)
    print("Processing Complete...")

    # End Logic
    record = FileProcessingRecord(
        timestamp=str(datetime.datetime.now()),
        guid=str(uuid.uuid4()),
        file_path=file_path,
        engine_return_status=manageAndProtectResult
    )

    store_record(record)

def main(event, context):
    print(f"Event:\n{event}\nConext:\n{context}")

    file_name = event.get("file_path")
    engine_path = event.get("engine_path")

    run_test(file_name, engine_path)

    return {
        "statusCode": 200,
        "body": "OK"
    }
