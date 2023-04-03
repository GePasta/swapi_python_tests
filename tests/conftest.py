import logging
import os
import time
from typing import Generator
from multiprocessing import Process

import pytest
import uvicorn
from _pytest.fixtures import FixtureRequest

from helpers.api_requests import check_health_event
from helpers.constans import HOST, PORT
from helpers.custom_execptions import ServerException
from http_server.run_server import app

log = logging.getLogger()


@pytest.fixture(autouse=True)
def log_test_func_name_and_time(request: FixtureRequest) -> Generator:
    """Log test cases name and duration"""
    log.info('\tTest case:\t'.center(100, '='))
    log.info(f'\n\n{request.node.nodeid}\n')
    log.info('============='.center(100, '='))
    func_name = request.function.__name__
    func_doc = request.function.__doc__
    log.info(f'{func_name.upper()}\n{func_doc}')
    start_time = time.time()
    yield
    end_time = time.time()
    log.debug('\n')
    log.debug(f'\tTest case duration: {(end_time - start_time):.3f} sec\t'.center(100, '='))


@pytest.fixture
def random_delay() -> None:
    """Enable random delay"""
    os.environ['DELAY'] = 'True'


def wait_for_server(server_address: str, timeout: int = 60) -> None:
    """Wait for HTTP server to start"""
    start_time = time.time()
    while True:
        time.sleep(1)
        if check_health_event(host=server_address):
            log.info('HTTP server is live')
            break
        elapsed_time = time.time() - start_time
        if elapsed_time >= timeout:
            raise ServerException(timeout)


def run_server() -> None:
    log.info(f'Setting up HTTP server at: {HOST}:{PORT}')
    uvicorn.run(app, host=HOST, port=PORT)


@pytest.fixture(scope='session')
def server() -> Generator:
    proc = Process(target=run_server, args=(), daemon=True)
    proc.start()
    server_address = f'http://{HOST}:{PORT}' # NOQA
    wait_for_server(server_address=server_address)
    yield server_address
    log.info('Cleaning up the environment')
    proc.kill()
