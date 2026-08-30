from pathlib import Path


def upload_destination(root: Path, filename: str) -> Path:
    base = root.resolve()
    destination = (base / filename).resolve()
    if not destination.is_relative_to(base):
        raise ValueError("filename escapes upload directory")
    return destination

