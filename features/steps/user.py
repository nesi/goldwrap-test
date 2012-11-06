import json
import util
from lettuce import world, step

@step('{User} Given the user (.*) exists')
def USER_verify_user_exists(step, user_file):
  user = eval(open(util.find_path_for_file(user_file)).read())
  world.uids.add(user['userId'])
  (status,body) = world.goldwrap.get_users()
  users = json.loads(body)
  for u in users:
    if user['userId'] == u['userId']:
      world.goldwrap.update_user(user)
      return
  world.goldwrap.create_user(user)

@step('{User} Given the user (.*) does not exist')
def USER_verify_user_not_exists(step, user_file):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.get_users()
  users = json.loads(body)
  for u in users:
    if user['userId'] == u['userId']:
      world.goldwrap.delete_user(user['userId'])
  
@step('{User} Then I can create the user (.*) and the HTTP status code is (.*)')
def USER_create_user(step, user_file, expected_status):
  user = eval(open(util.find_path_for_file(user_file)).read())
  world.uids.add(user['userId'])
  (status, body) = world.goldwrap.create_user(user)
  assert str(expected_status) == str(status)
  
@step('{User} Then I can get the user (.*)')
def USER_get_user(step, user_file):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status, body) = world.goldwrap.get_user(user['userId'])
  u = json.loads(body)
  assert util.simple_dict_equal(u, user)
    
@step('{User} Then I see user (.*) in the user list')
def USER_get_user_in_list(step, user_file):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status, body) = world.goldwrap.get_users()
  users = json.loads(body)
  for u in users:
    if u['userId'] == user['userId']:
      assert util.simple_dict_equal(u, user)
      return
  assert False
    
@step('{User} Then I can delete the user (.*) and the HTTP status code is (.*)')
def USER_delete_user(step, user_file, expected_status):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.delete_user(user['userId'])
  assert str(expected_status) == str(status)
  (status,body) = world.goldwrap.get_users()
  users = json.loads(body)
  for u in users:
    assert user['userId'] != u['userId']

@step('{User} Then getting the user (.*) fails and the HTTP status code is (.*)')
def USER_verify_failure_for_getting_non_existent_user(step, user_file, expected_status):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.get_user(user['userId'])
  bodyObject = json.loads(body)
  assert 'errorCode' in bodyObject
  assert 'reason' in bodyObject
  assert str(expected_status) == str(status)

@step('{User} Then deleting the user (.*) fails and the HTTP status code is (.*)')
def USER_verify_failure_for_deleting_non_existent_user(step, user_file, expected_status):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.delete_user(user['userId'])
  assert str(expected_status) == str(status)
  
@step('{User} Then creating the user (.*) again fails and the HTTP status code is (.*)')
def USER_verify_failure_for_duplicate_user(step, user_file, expected_status):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.create_user(user)
  bodyObject = json.loads(body)
  assert 'errorCode' in bodyObject
  assert 'reason' in bodyObject
  assert str(expected_status) == str(status)

@step('{User} Then the user (.*) is a principle of the projects (.*)')
def USER_is_principle_of(step, user_file, project_list):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.get_projects_of_principal(user['userId'])
  projects = json.loads(body)
  if project_list.strip() == '':
    num_visible = 0
  else:
    num_visible = len(project_list.split(','))
  assert len(projects) == num_visible

@step('{User} Then the user (.*) is a user of the projects (.*)')
def USER_is_user_of(step, user_file, project_list):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.get_projects_of_user(user['userId'])
  projects = json.loads(body)
  if project_list.strip() == '':
    num_visible = 0
  else:
    num_visible = len(project_list.split(','))
  assert len(projects) == num_visible
  