Feature: Project

  Scenario: Create new project
  
    {Project} Given project <p> does not exist
    {Project} Then I can create project <p> and the HTTP status code is <http_status>

    Examples:
      | p    | http_status |
      | p1 | 204         |


  Scenario: Get existing project

    {Project} Given project <p> exists
    {Project} Then I can get project <p>

    Examples:
      | p    |
      | p1 |


  Scenario: See existing project in project list

    {Project} Given project <p> exists
    {Project} Then I see project <p> in the project list

    Examples:
      | p    |
      | p1 |


  Scenario: Update existing project

    {Project} Given project <p> exists
    {Project} Then I can update project <p> with new description <d>

    Examples:
      | p  | http_status | d                    |
      | p1 | 204         | some new description |


  Scenario: Delete existing project

    {Project} Given project <p> exists
    {Project} Then I can delete project <p> and the HTTP status code is <http_status>

    Examples:
      | p    | http_status |
      | p1 | 204         |


  Scenario: Get non-existing project

    {Project} Given project <p> does not exist
    {Project} Then getting project <p> fails and the HTTP status code is <http_status>

    Examples:
      | p    | http_status |
      | p1 | 404         |


  Scenario: Delete non-existing project

    {Project} Given project <p> does not exist
    {Project} Then deleting project <p> fails and the HTTP status code is <http_status>

    Examples:
      | p    | http_status |
      | p1 | 204         |

      