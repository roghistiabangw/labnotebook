# === Stage 8: Генерация идентификаторов ===
# Project: LabNotebook
import uuid


PROJECT_PREFIX = "LNBK"


def generate_unique_id():
    while True:
        candidate = f"{PROJECT_PREFIX}-{uuid.uuid4().hex}"
        if not is_taken(candidate):
            return candidate


def is_taken(candidate):
    return candidate in _taken_ids


_taken_ids = set()


def register_id(candidate):
    _taken_ids.add(candidate)


def unregister_id(candidate):
    try:
        _taken_ids.discard(candidate)
    except KeyError:
        pass
