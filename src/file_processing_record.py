from dataclasses import dataclass
from uuid import UUID

@dataclass
class FileProcessingRecord:
    guid: UUID
    file_name: str
    engine_return_status: int
    