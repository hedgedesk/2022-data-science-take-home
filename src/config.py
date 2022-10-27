from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, order=True)
class Settings:
    root_dir: Path = Path(__file__).resolve().parents[0]
    storage_dir: Path = root_dir / "storage"
    datasets_dir: Path = root_dir / "datasets"


