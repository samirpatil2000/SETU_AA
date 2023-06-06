from enum import Enum
from typing import final

SETU_API_ENDPOINT: final(str) = "https://fiu-uat.setu.co/"

X_CLIENT_ID = "255d0b6c-492d-44cf-8581-e9494c7b0914"
X_CLIENT_SECRET = "9c2fc756-3d17-46d6-b28d-be4d71953e83"


SETU_API_HEADERS = {
  'x-client-id': 'dc692d3c-b7c9-4123-bcd9-0ee5360b5fdf',
  'x-client-secret': '5982f80d-1ea0-4856-a669-41efa576388c',
  'Content-Type': 'application/json'
}


class ConsentStatus(Enum):
    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    REVOKED = "REVOKED"
    PAUSED = "PAUSED"
    EXPIRED = "EXPIRED"


class SessionStatus(Enum):
    COMPLETED = "COMPLETED"
    PARTIAL = "PARTIAL"
    PENDING = "PENDING"