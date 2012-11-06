Feature: Project

  Scenario: Create new project
  
    {Project} Given the project <p> does not exist
    {Project} Then I can create the project <p> and the HTTP status code is <http_status>

    Examples:
      | p    | http_status |
      | p1 | 204         |


  Scenario: Get existing project

    {Project} Given the project <p> exists
    {Project} Then I can get the project <p>

    Examples:
      | p    |
      | p1 |


  Scenario: See existing project in project list

    {Project} Given the project <p> exists
    {Project} Then I see project <p> in the project list

    Examples:
      | p    |
      | p1 |


  Scenario: Delete existing project

    {Project} Given the project <p> exists
    {Project} Then I can delete the project <p> and the HTTP status code is <http_status>

    Examples:
      | p    | http_status |
      | p1 | 204         |


  Scenario: Get non-existing project

    {Project} Given the project <p> does not exist
    {Project} Then getting the project <p> fails and the HTTP status code is <http_status>

    Examples:
      | p    | http_status |
      | p1 | 404         |


  Scenario: Delete non-existing project

    {Project} Given the project <p> does not exist
    {Project} Then deleting the project <p> fails and the HTTP status code is <http_status>

    Examples:
      | p    | http_status |
      | p1 | 204         |

      