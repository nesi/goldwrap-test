Feature: Project

  Scenario: Create new project
  
    {User} Given the user <user> exists
    {Project} Given the project <project> does not exist
    {Project} Then I can create the project <project> and the HTTP status code is <http_status>

    Examples:
      | user | project   | http_status   |
      | u001 | p001_u001 | 200           |


  Scenario: Get existing project

    {User} Given the user <user> exists
    {Project} Given the project <project> exists
    {Project} Then I can get the project <project>

    Examples:
      | user | project    |
      | u001 | p001_u001  |


  Scenario: Delete existing project

    {User} Given the user <user> exists
    {Project} Given the project <project> exists
    {Project} Then I can delete the project <project> and the HTTP status code is <http_status>

    Examples:
      | user | project   | http_status |
      | u001 | p001_u001 | 204         |


  Scenario: Get non-existing project

    {Project} Given the project <project> does not exist
    {Project} Then getting the project <project> fails and the HTTP status code is <http_status>

    Examples:
      | project   | http_status |
      | p001_u001 | 404         |


  Scenario: Delete non-existing project

    {Project} Given the project <project> does not exist
    {Project} Then deleting the project <project> fails and the HTTP status code is <http_status>

    Examples:
      | project   | http_status |
      | p001_u001 | 404         |

      