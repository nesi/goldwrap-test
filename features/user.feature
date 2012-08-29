Feature: User

  Scenario: Create, get, delete new user
    {User} Given the user specified in <user_file> does not exist
    {User} Then I can create the user specified in <user_file> and get the status code <create_status>
    {User} And I can GET the user specified in <user_file>
    {User} And I can DELETE the user specified in <user_file> and get the status code <delete_status> 

    Examples:
      | user_file     | create_status | delete_status |
      | user_001.dict | 204           | 204           |


  Scenario: Verify that creating the same user twice fails
    {User} Given the user specified in <user_file> does not exist
    {User} Then I can create the user specified in <user_file> and get the status code <create_status>
    {User} And I cannot create another user specified in <user_file> and get the status code <error_status>
    {User} And I can DELETE the user specified in <user_file> and get the status code <delete_status> 

    Examples:
      | user_file      | create_status | error_status | delete_status |
      | user_001.dict  | 204           | 409          | 204           |
