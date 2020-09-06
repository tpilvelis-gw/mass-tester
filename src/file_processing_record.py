from dataclasses import dataclass

@dataclass
class FileProcessingRecord:
    timestamp: str
    guid: str
    file_name: str
    engine_return_status: int
    