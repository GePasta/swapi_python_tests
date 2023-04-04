import logging
from typing import Callable

import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from helpers.api_requests import (
    validate_response_status_code, get_star_wars_item
)
from helpers.constans import PLANETS_ENDPOINT

log = logging.getLogger()

pytestmark = [pytest.mark.performance, pytest.mark.planets]


@pytest.mark.parametrize('item_id', range(1, 101))
@pytest.mark.benchmark(group='performance', warmup=False)
def test_check_planets_endpoint_performance(server: str,
                                            random_delay: Callable,
                                            benchmark: BenchmarkFixture,
                                            item_id: int
                                            ) -> None:
    """
    Run performance tests on /planets endpoint. Each planet id, starting from 1, and ending on 100
    will be tested for 2 seconds.
    Given the planets API is running and a random delay is applied
    When I make a GET request to the endpoints from "/planets/1" to "/planets/100"
    Then the response status code should be 200
        And the results for each endpoint are printed out with min, max, mean, median duration
    """

    response = benchmark(lambda: get_star_wars_item(
        host=server, endpoint=PLANETS_ENDPOINT, item_id=item_id)
                         )
    validate_response_status_code(response=response)
