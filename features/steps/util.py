import os 
from lettuce import step, world

def find_path_for_file(filename):
  for root, dirs, files in os.walk('.'):
    for file in files:
      if file == filename:
        return os.path.join(root, file)

@step('{Util} Cleanup')
def cleanup(step):
  for uid in world.uids:
    world.goldwrap.delete_user(uid)
  for pid in world.pids:
    world.goldwrap.delete_project(pid)
  world.uids.clear()
  world.pids.clear()