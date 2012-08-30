Feature: User

  Scenario: Create new user
  
    {User} Given the user <user> does not exist
    {User} Then I can create the user <user> and the HTTP status code is <http_status>

    Examples:
      | user | http_status   |
      | u001 | 204           |


  Scenario: Get existing user

    {User} Given the user <user> exists
    {User} Then I can get the user <user>

    Examples:
      | user |
      | u001 |


  Scenario: Delete user

    {User} Given the user <user> exists
    {User} Then I can delete the user <user> and the HTTP status code is <http_status>

    Examples:
      | user  | http_status |
      | u001  | 204         |


  Scenario: Get non-existing user

    {User} Given the user <user> does not exist
    {User} Then getting the user <user> fails and the HTTP status code is <http_status>

    Examples:
      | user  | http_status |
      | u001  | 404         |


  Scenario: Delete non-existing user

    {User} Given the user <user> does not exist
    {User} Then deleting the user <user> fails and the HTTP status code is <http_status>

    Examples:
      | user  | http_status |
      | u001  | 404         |


  Scenario: Create the same user twice

    {User} Given the user <user> exists
    {User} Then creating the user <user> again fails and the HTTP status code is <http_status>

    Examples:
      | user  | http_status |
      | u001  | 409         |


  Scenario: Get project list of a principal

    {Util} Cleanup
    {User} Given the user <u1> exists
    {User} Given the user <u2> exists
    {Project} Given the project <p1> exists
    {Project} Given the project <p2> exists
    {Project} Given the project <p3> exists
    {User} {User} Then the user <u1> is a principle of the projects <visible_u1>
    {User} {User} Then the user <u2> is a principle of the projects <visible_u2>
    
    Examples:
      | u1   | u2   | p1        | p2        | p3        | visible_u1           | visible_u2 | 
      | u001 | u002 |           |           |           |                      |            |
      | u001 | u002 | p001_u001 |           | p004_u002 | p001_u001            | p004_u002  |
      | u001 | u002 | p001_u001 | p002_u001 | p004_u002 | p001_u001, p002_u001 | p004_u002  |


  Scenario: Get project list of a user

    {Util} Cleanup
    {User} Given the user <u1> exists
    {User} Given the user <u2> exists
    {Project} Given the project <p1> exists
    {Project} Given the project <p2> exists
    {Project} Given the project <p3> exists
    {User} {User} Then the user <u1> is a user of the projects <visible_u1>
    {User} {User} Then the user <u2> is a user of the projects <visible_u2>
    
    Examples:
      | u1   | u2   | p1        | p2        | p3        | visible_u1           | visible_u2           | 
      | u001 | u002 |           |           |           |                      |                      |
      | u001 | u002 | p002_u001 |           | p004_u002 | p002_u001            | p004_u002            |
      | u001 | u002 | p002_u001 | p003_u001 | p004_u002 | p002_u001, p003_u001 | p003_u001, p004_u002 |
      