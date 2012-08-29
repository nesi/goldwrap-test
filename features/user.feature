Feature: User

  Scenario: Create, get, delete new user
    {User} Given the user specified in <file> does not exist
    {User} Then I can create the user specified in <file> and get HTTP status code <http_create_status>
    {User} And I can GET the user specified in <file>
    {User} And I can DELETE the user specified in <file> and get HTTP status code <http_delete_status> 

    Examples:
      | file          | http_create_status | http_delete_status |
      | user_001.dict | 204                | 204                |


  Scenario: Verify that creating the same user twice fails
    {User} Given the user specified in <file> does not exist
    {User} Then I can create the user specified in <file> and get HTTP status code <http_create_status>
    {User} And I cannot create another user specified in <file> and get HTTP status code <http_error_status>
    {User} And I can DELETE the user specified in <file> and get HTTP status code <http_delete_status> 

    Examples:
      | file           | http_create_status | http_error_status | http_delete_status |
      | user_001.dict  | 204                | 409               | 204                |
