import json
import util
from lettuce import world, step

@step('{Project} Given the project (.*) does not exist')
def PROJECT_verify_project_not_exists(step, project_file):
  project = eval(open(util.find_path_for_file(project_file)).read())
  (status,body) = world.goldwrap.get_projects()
  projects = json.loads(body)
  for p in projects:
    if project['projectTitle'] == p['projectTitle']:
      world.goldwrap.delete_project(p['projectId'])

@step('{Project} Given the project (.*) exists')
def PROJECT_verify_project_exists(step, project_file):
  if project_file.strip() != '':
    project = eval(open(util.find_path_for_file(project_file)).read())
    (status,body) = world.goldwrap.get_projects()
    projects = json.loads(body)
    for p in projects:
      if project['projectTitle'] == p['projectTitle']:
        world.goldwrap.update_project(p)
        return
    (status,body) = world.goldwrap.create_project(project)
    world.pids.add(json.loads(body)['projectId'])
  
  
@step('{Project} Then I can create the project (.*) and the HTTP status code is (.*)')
def PROJECT_create_project(step, project_file, expected_status):
  project = eval(open(util.find_path_for_file(project_file)).read())
  (status, body) = world.goldwrap.create_project(project)
  assert str(expected_status) == str(status)
  p = json.loads(body)
  world.pids.add(p['projectId'])

@step('{Project} Then I can get the project (.*)')
def PROJECT_get_project(step, project_file):
  project = eval(open(util.find_path_for_file(project_file)).read())
  (status,body) = world.goldwrap.get_projects()
  projects = json.loads(body)
  for tmpp in projects:
    if tmpp['projectTitle'] == project['projectTitle']:
      pid = tmpp['projectId']
      (status, body) = world.goldwrap.get_project(tmpp['projectId'])
      p = json.loads(body)
      for key in project.keys():
        assert key in p
        assert str(p[key]) == str(project[key])
      world.goldwrap.delete_project(tmpp['projectId'])
      return
  assert False
  
@step('{Project} Then I can delete the project (.*) and the HTTP status code is (.*)')
def PROJECT_delete_project(step, project_file, expected_status):
  project = eval(open(util.find_path_for_file(project_file)).read())
  (status,body) = world.goldwrap.get_projects()
  projects = json.loads(body)
  for p in projects:
    if p['projectTitle'] == project['projectTitle']:
      (status,body) = world.goldwrap.delete_project(p['projectId'])
      assert str(expected_status) == str(status)
      assert body.strip() == ''
      break
  (status,body) = world.goldwrap.get_projects()
  projects = json.loads(body)
  for p in projects:
    assert p['projectTitle'] != project['projectTitle']

@step('{Project} Then getting the project (.*) fails and the HTTP status code is (.*)')
def PROJECT_get_non_existing_project(step, project_file, expected_status):
  project = eval(open(util.find_path_for_file(project_file)).read())
  (status,body) = world.goldwrap.get_project('__some_weird_and_for_sure_invalid_project_id__')
  err = json.loads(body)
  assert 'errorCode' in err
  assert 'reason' in err
  assert str(expected_status) == str(status)

@step('{Project} Then deleting the project (.*) fails and the HTTP status code is (.*)')
def PROJECT_delete_non_existing_project(step, project_file, expected_status):
  project = eval(open(util.find_path_for_file(project_file)).read())
  (status,body) = world.goldwrap.delete_project('__some_weird_and_for_sure_invalid_project_id__')
  err = json.loads(body)
  assert 'errorCode' in err
  assert 'reason' in err
  assert str(expected_status) == str(status)
