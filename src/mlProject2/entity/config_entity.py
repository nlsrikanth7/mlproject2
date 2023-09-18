# Update Entity
from dataclasses import dataclass
from pathlib import Path


# Entity _ which return type should the function return.
# custom return type other than configbox

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict