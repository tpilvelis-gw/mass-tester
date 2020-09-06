from dataclasses import dataclass

@dataclass
class FileProcessingRecord:
    timestamp: str
    guid: str
    file_path: str
    engine_return_status: int
    