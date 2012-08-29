Feature: User

  Scenario: POST, GET, DELETE new user
    {User} Given the user specified in <file> does not exist
    {User} Then I can POST the user specified in <file> and get HTTP status code <http_post_status>
    {User} And I can GET the user specified in <file>
    {User} And I can DELETE the user specified in <file> and get HTTP status code <http_delete_status> 

    Examples:
      | file          | http_post_status   | http_delete_status |
      | user_001.dict | 204                | 204                |


  Scenario: Verify that creating the same user twice fails
    {User} Given the user specified in <file> does not exist
    {User} Then I can POST the user specified in <file> and get HTTP status code <http_post_status>
    {User} And I cannot POST another user specified in <file> and get HTTP status code <http_post_error_status>
    {User} And I can DELETE the user specified in <file> and get HTTP status code <http_delete_status> 

    Examples:
      | file           | http_post_status | http_post_error_status | http_delete_status |
      | user_001.dict  | 204              | 409                    | 204                |
