import asyncio
import logging
import os
import random
import typing
from dataclasses import asdict

from requests import Request, Response
from fastapi import FastAPI, Depends, HTTPException

from helpers.constans import RESULTS_PATH, TIMESTAMP, LOG_FORMAT
from http_server.models import Person, Planet, Starship

file_name_prefix = f'{RESULTS_PATH}/{TIMESTAMP}'
log_server = logging.getLogger()
log_server.setLevel(logging.DEBUG)
if not os.path.exists(RESULTS_PATH):
    os.makedirs(RESULTS_PATH)
logging.basicConfig(
        format=LOG_FORMAT,
        filename=f'{file_name_prefix}.log',
        level='DEBUG',
    )
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log_server.addHandler(ch)
app = FastAPI()


def check_id(item_id: int) -> None:
    if item_id > 100:
        raise HTTPException(status_code=404, detail='Not Found')


async def add_delay() -> None:
    DELAY = os.getenv('DELAY', '')
    if DELAY:
        await asyncio.sleep(random.uniform(0.1, 1.0))


@app.get('/people/{item_id}')
async def read_person(item_id: int = Depends(check_id)) -> dict:
    """Return a person with the given ID """
    await add_delay()
    person = Person()
    return asdict(person)


@app.get('/planets/{item_id}')
async def read_planet(item_id: int = Depends(check_id)) -> dict:
    """Return a planet with the given ID"""
    await add_delay()
    planet = Planet()
    return asdict(planet)


@app.get('/starships/{item_id}')
async def read_starship(item_id: int = Depends(check_id)) -> dict:
    """Return a starship with the given ID"""
    await add_delay()
    starship = Starship()
    return asdict(starship)


@app.get('/health')
async def health_check() -> dict:
    """Basic health check endpoint to ensure that the API is up and running."""
    return {'status': 'ok'}


@app.middleware('http')
async def log_requests(request: Request, call_next: typing.Any) -> Response:
    log_server.info(f'Incoming request: {request.method} {request.url}')
    response = await call_next(request)
    log_server.info(f'Outgoing response: {response.status_code}')
    return response
