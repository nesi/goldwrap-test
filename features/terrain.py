from lettuce import world, before
from steps.goldwrap import GoldWrap

# configuration parameters
GOLDWRAP_PROTOCOL = 'http'
GOLDWRAP_HOST = 'gold.dev.nesi.org.nz'
GOLDWRAP_PORT = 8080
GOLDWRAP_BASE_PATH = '/goldwrap/rest/goldwrap'
TIMEOUT = 20

@before.all
def init():
  world.goldwrap = GoldWrap(GOLDWRAP_PROTOCOL, GOLDWRAP_HOST, GOLDWRAP_PORT, GOLDWRAP_BASE_PATH, TIMEOUT)
