from lettuce import world, before, after
from steps.goldwrap import GoldWrap
from steps import util

# configuration parameters
GOLDWRAP_PROTOCOL = 'http'
GOLDWRAP_HOST = 'gold.dev.nesi.org.nz'
GOLDWRAP_PORT = 8080
GOLDWRAP_BASE_PATH = '/goldwrap/rest/goldwrap'
TIMEOUT = 20

@before.all
def init():
  world.goldwrap = GoldWrap(GOLDWRAP_PROTOCOL, GOLDWRAP_HOST, GOLDWRAP_PORT, GOLDWRAP_BASE_PATH, TIMEOUT)
  world.pids = set()
  world.uids = set()
  
@after.all
def cleanup(total):
  util.cleanup('')