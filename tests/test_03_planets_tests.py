import logging

import pytest

from http_server.models import Planet
from helpers.api_requests import (
    validate_response_status_code, validate_response_content, get_star_wars_item
)
from helpers.constans import PLANETS_ENDPOINT

log = logging.getLogger()

pytestmark = [pytest.mark.functional, pytest.mark.planets]


@pytest.mark.parametrize('item_id, status_code', [
    ('1', 200),
    ('2', 200),
    ('50', 200),
    ('99', 200),
    ('100', 200),
], ids=[
    'ID_1_BEGINNING_OF_THE_RANGE',
    'ID_2_BEGINNING_OF_THE_RANGE',
    'ID_50_MIDRANGE',
    'ID_99_END_OF_RANGE',
    'ID_100_END_OF_RANGE',
])
def test_check_planets_endpoint_happy_path(server: str, item_id: str, status_code: int) -> None:
    """
    Test check planets endpoint with valid item id's

    GIVEN an HTTP server is running
    WHEN a GET request to planets endpoint with walid item id is made
    THEN response status code is 200 and response contains appropriate body
    """
    log.info(f'Running happy path test with {item_id=}')
    model = Planet()
    response = get_star_wars_item(host=server, endpoint=PLANETS_ENDPOINT, item_id=item_id)
    validate_response_status_code(response=response, expected_status_code=status_code)
    validate_response_content(response=response, model=model)


@pytest.mark.parametrize('item_id, status_code', [
    ('101', 404),
    ('200000', 404),
], ids=[
    'ID_101_OUT_OF_SCOPE',
    'ID_200000_FAR_OUT_OF_SCOPE',
])
def test_check_planets_endpoint_edge_cases(server: str, item_id: str, status_code: int) -> None:
    """
    Test check planets endpoint edge cases

    GIVEN an HTTP planets is running
    WHEN a GET request to planets endpoint with item id higher than 100
    THEN response from the server is contains status code 404 not found
    """
    log.info(f'Running edge cases test with {item_id=}')
    response = get_star_wars_item(host=server, endpoint=PLANETS_ENDPOINT, item_id=item_id)
    validate_response_status_code(response=response, expected_status_code=status_code)


@pytest.mark.parametrize('item_id, status_code', [
    ('test', 422),
    ('!@#$%^&*()', 422),
], ids=[
    'STRING_INSTEAD_OF_NUMERIC_ID',
    'SPECIAL_CHARACTERS_INSTEAD_OF_NUMERIC_ID'
])
def test_check_planets_endpoint_invalid_item_id(server: str, item_id: str, status_code: int
                                                ) -> None:
    """
    Test check planets endpoint with invalid item id

    GIVEN an HTTP server is running
    WHEN a GET request to planets endpoint with invalid item id is made
    THEN response from the server is contains status code 422 not found
    """
    log.info(f'Running invalid id test with {item_id=}')
    response = get_star_wars_item(host=server, endpoint=PLANETS_ENDPOINT, item_id=item_id)
    validate_response_status_code(response=response, expected_status_code=status_code)
