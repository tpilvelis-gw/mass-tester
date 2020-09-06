import json

class Manifest:
    def __init__(self, engine: str, file_name: str) -> None:
        self.__manifest = {
            "engine": engine,
            "file_name": file_name
        }

    def payload(self):
        return json.dumps(self.__manifest)
