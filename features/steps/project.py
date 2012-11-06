import json
import util
from lettuce import world, step

@step('{Project} Given project (.*) exists')
def PROJECT_verify_project_exists(step, project_file):
  if project_file.strip() != '':
    project = eval(open(util.find_path_for_file(project_file)).read())
    world.pids.add(project['projectId'])
    (status, body) = world.goldwrap.get_project(project['projectId'])
    p = json.loads(body)
    if 'projectId' in p and p['projectId'] == project['projectId']:
      return
    (status,body) = world.goldwrap.create_project(project)

@step('{Project} Given project (.*) does not exist')
def PROJECT_verify_project_not_exists(step, project_file):
  project = eval(open(util.find_path_for_file(project_file)).read())
  (status,body) = world.goldwrap.get_projects()
  projects = json.loads(body)
  for p in projects:
    if project['projectId'] == p['projectId']:
      world.goldwrap.delete_project(p['projectId'])

@step('{Project} Given user (.*) is member of project (.*)')
def PROJECT_verify_user_member_of_project(step, user_file, project_file):
  project = eval(open(util.find_path_for_file(project_file)).read())
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status, body) = world.goldwrap.get_project(project['projectId'])
  p = json.loads(body)
  if 'users' not in p or user['userId'] not in p['users']:
    world.goldwrap.add_user_to_project(user['userId'], project['projectId'])
  
@step('{Project} Given user (.*) is not member of project (.*)')
def PROJECT_verify_user_not_member_of_project(step, user_file, project_file):
  project = eval(open(util.find_path_for_file(project_file)).read())
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status, body) = world.goldwrap.get_project(project)
  project = json.loads(body)
  if 'users' in project:
    if user['userId'] in project['users']:
      world.goldwrap.delete_project(project['projectId'])
      world.goldwrap.create_project(project)

@step('{Project} If I add user (.*) to project (.*)')
def PROJECT_add_user_to_project(step, user_file, project_file):
  project = eval(open(util.find_path_for_file(project_file)).read())
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status, body) = world.goldwrap.add_user_to_project(user['userId'], project['projectId'])  

@step('{Project} Then I can create project (.*) and the HTTP status code is (.*)')
def PROJECT_create_project(step, project_file, expected_status):
  project = eval(open(util.find_path_for_file(project_file)).read())
  world.pids.add(project['projectId'])
  (status, body) = world.goldwrap.create_project(project)
  assert str(expected_status) == str(status)

@step('{Project} Then I can get project (.*)')
def PROJECT_get_project(step, project_file):
  project = eval(open(util.find_path_for_file(project_file)).read())
  (status, body) = world.goldwrap.get_project(project['projectId'])
  p = json.loads(body)
  assert p['projectId'] == project['projectId']
  assert p['description'] == project['description']

@step('{Project} Then I see project (.*) in the project list')
def PROJECT_get_project_in_list(step, project_file):
  project = eval(open(util.find_path_for_file(project_file)).read())
  (status, body) = world.goldwrap.get_projects()
  projects = json.loads(body)
  for p in projects:
    if p['projectId'] == project['projectId']:
      return
  assert False
  
@step('{Project} Then I can delete project (.*) and the HTTP status code is (.*)')
def PROJECT_delete_project(step, project_file, expected_status):
  project = eval(open(util.find_path_for_file(project_file)).read())
  (status,body) = world.goldwrap.delete_project(project['projectId'])
  assert str(expected_status) == str(status)
  assert body.strip() == ''
  (status,body) = world.goldwrap.get_projects()
  projects = json.loads(body)
  for p in projects:
    assert p['projectId'] != project['projectId']

@step('{Project} Then getting project (.*) fails and the HTTP status code is (.*)')
def PROJECT_get_non_existing_project(step, project_file, expected_status):
  (status,body) = world.goldwrap.get_project('__some_weird_and_for_sure_invalid_project_id__')
  err = json.loads(body)
  assert 'errorCode' in err
  assert 'reason' in err
  assert str(expected_status) == str(status)

@step('{Project} Then user (.*) is member of project (.*)')
def PROJECT_verify_user_is_member(step, user_file, project_file):
  project = eval(open(util.find_path_for_file(project_file)).read())
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status, body) = world.goldwrap.get_project(project['projectId'])
  p = json.loads(body)
  assert 'users' in p
  assert user['userId'] in p['users']

@step('{Project} Then user (.*) is not member of project (.*)')
def PROJECT_verify_user_is_not_member(step, user_file, project_file):
  project = eval(open(util.find_path_for_file(project_file)).read())
  user = eval(open(util.find_path_for_file(user_file)).read())
  (status, body) = world.goldwrap.get_project(project['projectId'])
  p = json.loads(body)
  if 'users' in p:
    assert user['userId'] not in p['users']

@step('{Project} Then deleting project (.*) fails and the HTTP status code is (.*)')
def PROJECT_delete_non_existing_project(step, project_file, expected_status):
  (status, body) = world.goldwrap.delete_project('__some_weird_and_for_sure_invalid_project_id__')
  assert str(expected_status) == str(status)
