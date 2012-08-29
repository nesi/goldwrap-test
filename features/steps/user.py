import json
import util
from lettuce import world, step

@step('{User} Given the user specified in (.*) does not exist')
def USER_verify_user_not_exists(step, user_file):
  user = eval(open(util.find_path_for_file(user_file)).read())
  users = world.goldwrap.get_users()
  for u in users:
    assert user['userId'] != u['userId']
  
@step('{User} Then I can create the user specified in (.*) and get the status code (.*)')
def USER_create_user(step, user_file, CREATE_status):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.create_user(user)
  assert str(CREATE_status) == str(status)
  
@step('{User} And I can GET the user specified in (.*)')
def USER_get_user(step, user_file):
  user = eval(open(util.find_path_for_file(user_file)).read())
  u = world.goldwrap.get_user(user['userId'])
  for key in user.keys():
    assert key in u
    assert u[key] == user[key]
  for key in u.keys():
    assert key in user
    assert u[key] == user[key]
    

@step('{User} And I can DELETE the user specified in (.*) and get the status code (.*)')
def USER_delete_user(step, user_file, DELETE_status):
  user = eval(open(util.find_path_for_file(user_file)).read())
  status = world.goldwrap.delete_user(user['userId'])
  assert str(DELETE_status) == str(status)
  
@step('{User} And I cannot create another user specified in (.*) and get the status code (.*)')
def USER_verify_failure_for_duplicate_user(step, user_file, ERROR_status):
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status,body) = world.goldwrap.create_user(user)
  bodyObject = json.loads(body)
  assert 'errorCode' in bodyObject
  assert 'reason' in bodyObject
  assert str(ERROR_status) == str(status)


