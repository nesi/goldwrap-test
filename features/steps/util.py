import os 
from lettuce import step, world

@step('{Util} Cleanup')
def cleanup(step):
  for uid in world.uids:
    world.goldwrap.delete_user(uid)
  for pid in world.pids:
    world.goldwrap.delete_project(pid)
  world.uids.clear()
  world.pids.clear()

def find_path_for_file(filename):
  for root, dirs, files in os.walk('.'):
    for file in files:
      if file == filename:
        return os.path.join(root, file)

def simple_dict_equal(dict1, dict2):
  ''' Compare two dicts. Values must be simple data types or dicts '''
  if dict1.keys() != dict2.keys():
    return False
  for key in dict1.keys():
    if type(dict1[key]) == type({}):
      if type(dict2[key]) != type({}):
        return False
      else:
        if not simple_dict_equal(dict1[key], dict2[key]):
          return False
    else:
      if not dict1[key] == dict2[key]:
        return False
  return True

