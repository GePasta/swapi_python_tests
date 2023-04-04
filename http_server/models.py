from dataclasses import dataclass
from typing import Optional, TypeVar

from http_server.data_helper import get_timestamp


@dataclass
class Model:
    pass


@dataclass
class Person(Model):
    name: str = 'Luke Skywalker'
    height: str = '172'
    mass: str = '77'
    hair_color: str = 'blond'
    skin_color: str = 'fair'
    eye_color: str = 'blue'
    birth_year: str = '19BBY'
    gender: str = 'male'
    homeworld: str = 'https://swapi.dev/api/planets/1/'
    films: tuple = (
        'https://swapi.dev/api/films/1/',
        'https://swapi.dev/api/films/2/',
        'https://swapi.dev/api/films/3/',
        'https://swapi.dev/api/films/6/'
    )
    vehicles: tuple = (
        'https://swapi.dev/api/vehicles/14/',
        'https://swapi.dev/api/vehicles/30/'
    )
    starships: tuple = (
        'https://swapi.dev/api/starships/12/',
        'https://swapi.dev/api/starships/22/'
    )
    created: str = get_timestamp()
    edited: str = get_timestamp()
    url: str = 'https://swapi.dev/api/people/1/'
    species: Optional[list] = None


@dataclass
class Planet(Model):
    name: str = 'Yavin IV"'
    rotation_period: str = '24'
    orbital_period: str = '4818'
    diameter: str = '10200'
    climate: str = 'temperate, tropical'
    gravity: str = '1 standard'
    terrain: str = 'jungle, rainforests'
    surface_water: str = '8'
    population: str = '1000'
    films: tuple = (
        'https://swapi.dev/api/films/1/',
    )
    created: str = get_timestamp()
    edited: str = get_timestamp()
    url: str = 'https://swapi.dev/api/planets/3/'
    residents: Optional[list] = None


@dataclass
class Starship(Model):
    name: str = 'Death Star'
    model: str = 'DS-1 Orbital Battle Station'
    manufacturer: str = 'Imperial Department of Military Research, Sienar Fleet Systems'
    cost_in_credits: str = '1000000000000'
    length: str = '120000'
    max_atmosphering_speed: str = 'n/a'
    crew: str = '342,953'
    passengers: str = '843,342'
    cargo_capacity: str = '1000000000000'
    consumables: str = '3 years'
    hyperdrive_rating: str = '4.0'
    MGLT: str = '10'
    starship_class: str = 'Deep Space Mobile Battlestation'
    films: tuple = (
        'https://swapi.dev/api/films/1/',
    )
    created: str = get_timestamp()
    edited: str = get_timestamp()
    url: str = 'https://swapi.dev/api/starships/9/'
    pilots: Optional[list] = None


ModelClass = TypeVar('ModelClass', bound=Model)
