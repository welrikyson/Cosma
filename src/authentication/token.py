from src.utils.file_storage import FileStore
from datetime import datetime

filename = "data.pickle"


def load_token():
    return FileStore.load(filename)


def save_token(token):
    FileStore.save(token, filename)


class Token:
    token: str
    refresh_token: str
    expires_at: datetime
    expires_in: str
