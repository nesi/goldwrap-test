from lettuce import world, before
from steps.goldwrap import GoldWrap
from steps import util
from steps import user

# configuration parameters
GOLDWRAP_PROTOCOL = 'http'
GOLDWRAP_HOST = 'gold.dev.nesi.org.nz'
GOLDWRAP_PORT = 8080
GOLDWRAP_BASE_PATH = '/goldwrap/rest/goldwrap'
TIMEOUT = 20

@before.all
def init():
  world.goldwrap = GoldWrap(GOLDWRAP_PROTOCOL, GOLDWRAP_HOST, GOLDWRAP_PORT, GOLDWRAP_BASE_PATH, TIMEOUT)
  u = eval(open(util.find_path_for_file('user_001.dict')).read())
  world.goldwrap.delete_user(u['userId'])