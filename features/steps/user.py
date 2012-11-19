import json
import util
from lettuce import world, step

@step('{User} Given user (.*) exists')
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

@step('{User} Given user (.*) does not exist')
def USER_verify_user_not_exists(step, user_file):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.get_users()
  users = json.loads(body)
  for u in users:
    if user['userId'] == u['userId']:
      world.goldwrap.delete_user(user['userId'])
  
@step('{User} If I delete user (.*)')
def USER_delete_user(step, user_file):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.delete_user(user['userId'])

@step('{User} Then I can create user (.*) and the HTTP status code is (.*)')
def USER_create_user(step, user_file, expected_status):
  user = eval(open(util.find_path_for_file(user_file)).read())
  world.uids.add(user['userId'])
  (status, body) = world.goldwrap.create_user(user)
  assert str(expected_status) == str(status)
  
@step('{User} Then I can get user (.*)')
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
    
@step('{User} Then I can update user (.*) with new email (.*)')
def USER_update_user_with_full_name(step, user_file, new_email):
  user = eval(open(util.find_path_for_file(user_file)).read())
  uid = user['userId']
  old_email = user['email']
  user['email'] = new_email
  (status, body) = world.goldwrap.update_user(user)
  (status, body) = world.goldwrap.get_user(uid)
  u = json.loads(body)
  assert u['email'] == new_email
  user['email'] = old_email
  (status, body) = world.goldwrap.update_user(user)
  (status, body) = world.goldwrap.get_user(uid)
  u = json.loads(body)
  assert u['email'] == old_email

@step('{User} Then I can delete user (.*) and the HTTP status code is (.*)')
def USER_delete_user_and_check_status_code(step, user_file, expected_status):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.delete_user(user['userId'])
  assert str(expected_status) == str(status)
  (status,body) = world.goldwrap.get_users()
  users = json.loads(body)
  for u in users:
    assert user['userId'] != u['userId']

@step('{User} Then getting user (.*) fails and the HTTP status code is (.*)')
def USER_verify_failure_for_getting_non_existent_user(step, user_file, expected_status):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.get_user(user['userId'])
  bodyObject = json.loads(body)
  assert 'errorCode' in bodyObject
  assert 'reason' in bodyObject
  assert str(expected_status) == str(status)

@step('{User} Then deleting user (.*) fails and the HTTP status code is (.*)')
def USER_verify_failure_for_deleting_non_existent_user(step, user_file, expected_status):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.delete_user(user['userId'])
  assert str(expected_status) == str(status)
  
@step('{User} Then creating user (.*) again fails and the HTTP status code is (.*)')
def USER_verify_failure_for_duplicate_user(step, user_file, expected_status):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.create_user(user)
  bodyObject = json.loads(body)
  assert 'errorCode' in bodyObject
  assert 'reason' in bodyObject
  assert str(expected_status) == str(status)

@step('{User} Then user (.*) is a principle of the projects (.*)')
def USER_is_principle_of(step, user_file, project_list):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.get_projects_of_principal(user['userId'])
  projects = json.loads(body)
  if project_list.strip() == '':
    num_visible = 0
  else:
    num_visible = len(project_list.split(','))
  assert len(projects) == num_visible

@step('{User} Then user (.*) is a user of the projects (.*)')
def USER_is_user_of(step, user_file, project_list):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.get_projects_of_user(user['userId'])
  projects = json.loads(body)
  if project_list.strip() == '':
    num_visible = 0
  else:
    num_visible = len(project_list.split(','))
  assert len(projects) == num_visible
  