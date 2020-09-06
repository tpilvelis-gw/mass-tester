import json

class Manifest:
    def __init__(self, engine_path: str, file_path: str) -> None:
        self.__manifest = {
            "engine_path": engine_path,
            "file_path": file_path
        }

    def payload(self):
        return json.dumps(self.__manifest)
