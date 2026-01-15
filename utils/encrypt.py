# crypto_ops.py
import base64


def ecs(s: str) -> str:
    encoded = base64.b64encode(s.encode("utf-8")).decode("utf-8")
    return encoded


def dcs(ed: str) -> str:
    try:
        decoded = base64.b64decode(ed.encode("utf-8"), validate=True).decode("utf-8")
    except (ValueError, UnicodeDecodeError):
        return ed
    return decoded
