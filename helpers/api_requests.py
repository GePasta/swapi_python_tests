"""Module for api request functions"""
import logging
import typing
from dataclasses import asdict

import requests
from requests import Response

from helpers.constans import HEALTH_EVENT_ENDPOINT
from helpers.custom_execptions import ModelException

log = logging.getLogger()


def get_star_wars_item(host: str, endpoint: str, item_id: str | int) -> Response:
    """Combine url and send a GET request"""
    url = f'{host}{endpoint}/{item_id}'
    return send_get_request(url=url)


def check_health_event(host: str) -> bool:
    """Send GET health event and check status code"""
    url = f'{host}{HEALTH_EVENT_ENDPOINT}'
    try:
        response = send_get_request(url=url)
        return response.status_code == 200
    except ConnectionError as e:   # NOQA
        return False


def send_get_request(url: str) -> Response:
    """Send a GET request"""
    log.info(f'Sending GET request to {url=}')
    response = requests.get(url=url)
    try:
        content = response.json()
    except ValueError:
        content = response.text
    log.info(f'Receive response:\n{content}')
    return response


def validate_response_status_code(response: Response, expected_status_code: int = 200) -> None:
    actual_status_code = response.status_code
    status_code_error_message = (
        f"""
        Incorrect status code.
        Expected {expected_status_code}, actual={actual_status_code}
        \n{response}
        """
    )
    assert response.status_code == expected_status_code, status_code_error_message


def validate_response_content(response: Response,  model: typing.Any) -> None:
    try:
        content = response.json()
    except ValueError:
        raise ValueError
    response_keys = set(content.keys())
    model_keys = set(asdict(model).keys())
    unexpected_response_keys = response_keys.difference(model_keys)
    missing_model_keys = model_keys.difference(response_keys)
    if unexpected_response_keys:
        model_error_message = f'Found unexpected keys in response: {response_keys}\n{content}'
        raise ModelException(model_error_message)
    if missing_model_keys:
        model_error_message = f'Missing model keys in response: {response_keys}\n{content}'
        raise ModelException(model_error_message)
