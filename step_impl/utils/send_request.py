"""
Sending requests functions.
"""
import requests


def send_request(method, endpoint, **kwargs):
    """
    A function to send a request.

    Args:
        method (str) : The method of sending request, [POST, GET, DELETE, PUT]
        endpoint (str) : The endpoint of the request
        **kwargs : Possible keywords [ json (dictionary), headers (dictionary), parameters (dictionary) ]
    Return:
        Response <response> object
    """
    response = None
    try:
        response = requests.request(
            method,
            endpoint,
            **kwargs
        )
    except Exception as e:
        print(e)
    return response

def get(endpoint, **kwargs):
    """
    GET request which will call the send_request function to do the request.
    """
    return send_request('GET', endpoint, **kwargs)

def post(endpoint, **kwargs):
    """
    POST request which will call the send_request function to do the request.
    """
    return send_request('POST', endpoint, **kwargs)

def put(endpoint, **kwargs):
    """
    PUT request which will call the send_request function to do the request.
    """
    return send_request('PUT', endpoint, **kwargs)

def delete(endpoint, **kwargs):
    """
    DELETE request which will call the send_request function to do the request.
    """
    return send_request('DELETE', endpoint, **kwargs)
