import os

params = {
        "hapikey": os.getenv("api_hapi_key")
    }

headers = {
    "Authorization" : os.getenv("api_authorization"),
    "Content-Type" : "application/json"
}