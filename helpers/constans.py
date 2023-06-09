from datetime import datetime
import os


HOST = '0.0.0.0'
PORT = 8000
PEOPLE_ENDPOINT = '/people'
PLANETS_ENDPOINT = '/planets'
STARSHIPS_ENDPOINT = '/starships'
HEALTH_EVENT_ENDPOINT = '/health'

# RESULTS_PATH = './results'
RESULTS_PATH = os.path.join('results', '')
TIMESTAMP = f'{datetime.now().strftime("%Y%m%d-%H%M%S")}'
LOG_FORMAT = '%(asctime)s %(levelname)s %(filename)s(%(lineno)d) - %(message)s'
