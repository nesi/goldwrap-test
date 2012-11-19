import httplib
import json
from urllib import quote

class GoldWrap:
  
  _txt_headers = { 'Accept': 'text/plain', 'Content-Type': 'text/plain' }
  _json_headers = { 'Accept': 'application/json', 'Content-Type': 'application/json' }

  def __init__(self, protocol, host, port, basepath, timeout):
    self._protocol = protocol
    self._host = host
    self._port = port
    self._basepath = basepath
    self._timeout = timeout
    
  def get_users(self):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/users' % (self._basepath))
    conn.request('GET', path, headers=self._json_headers)
    resp = conn.getresponse()
    status = resp.status
    body = resp.read()
    conn.close()
    return (status, body)

  def get_user(self, user_id):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/users/%s' % (self._basepath, user_id))
    conn.request('GET', path, headers=self._json_headers)
    resp = conn.getresponse()
    status = resp.status
    body = resp.read()
    return (status, body)

  def create_user(self, user):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/users' % (self._basepath))
    conn.request('PUT', path, body=json.dumps(user), headers=self._json_headers)
    resp = conn.getresponse()
    status = resp.status
    body = resp.read()
    return (status, body)

  def update_user(self, user):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/users/%s' % (self._basepath, user['userId']))
    conn.request('POST', path, body=json.dumps(user), headers=self._json_headers)
    resp = conn.getresponse()
    status = resp.status
    body = resp.read()
    return (status,body)
      
  def delete_user(self, user_id):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/users/%s' % (self._basepath, user_id))
    conn.request('DELETE', path, headers=self._json_headers)
    resp = conn.getresponse()
    status = resp.status
    body = resp.read()
    return (status,body)

  def add_user_to_project(self, user_id, project_id):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/projects/%s/add_user' % (self._basepath, project_id))
    conn.request('POST', path, body=user_id, headers=self._txt_headers)
    resp = conn.getresponse()
    status = resp.status
    body = resp.read()
    return (status,body)
        
  def get_projects(self):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/projects' % (self._basepath))
    conn.request('GET', path, headers=self._json_headers)
    resp = conn.getresponse()
    status = resp.status
    body = resp.read()
    return (status,body)

  def get_projects_of_user(self, user_id):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/users/%s/projects' % (self._basepath, user_id))
    conn.request('GET', path, headers=self._json_headers)
    resp = conn.getresponse()
    status = resp.status
    body = resp.read()
    return (status,body)
    
  def get_project(self, project_id):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/projects/%s' % (self._basepath, project_id))
    conn.request('GET', path, headers=self._json_headers)
    resp = conn.getresponse()
    status = resp.status
    body = resp.read()
    conn.close()
    return (status,body)

  def create_project(self, project):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/projects' % (self._basepath))
    conn.request('PUT', path, body=json.dumps(project), headers=self._json_headers)
    resp = conn.getresponse()
    status = resp.status
    body = resp.read()
    return (status,body)

  def update_project(self, project):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/projects' % (self._basepath))
    conn.request('POST', path, body=json.dumps(project), headers=self._json_headers)
    resp = conn.getresponse()
    status = resp.status
    body = resp.read()
    return (status,body)
      
  def delete_project(self, project_id):
    conn = httplib.HTTPConnection(self._host, self._port, self._timeout)
    path = quote('%s/projects/%s' % (self._basepath, project_id))
    conn.request('DELETE', path, headers=self._json_headers)
    resp = conn.getresponse()
    status = resp.status
    body = resp.read()
    return (status,body)
    
