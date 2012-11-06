Feature: User

  Scenario: Create new user
  
    {User} Given the user <u> does not exist
    {User} Then I can create the user <u> and the HTTP status code is <http_status>

    Examples:
      | u  | http_status   |
      | u1 | 204           |


  Scenario: Get existing user

    {User} Given the user <u> exists
    {User} Then I can get the user <u>

    Examples:
      | u  |
      | u1 |


  Scenario: See existing user in user list

    {User} Given the user <u> exists
    {User} Then I see user <u> in the user list

    Examples:
      | u  |
      | u1 |


  Scenario: Delete user

    {User} Given the user <u> exists
    {User} Then I can delete the user <u> and the HTTP status code is <http_status>

    Examples:
      | u   | http_status |
      | u1  | 204         |


  Scenario: Get non-existing user

    {User} Given the user <u> does not exist
    {User} Then getting the user <u> fails and the HTTP status code is <http_status>

    Examples:
      | u   | http_status |
      | u1  | 404         |


  Scenario: Delete non-existing user

    {User} Given the user <u> does not exist
    {User} Then deleting the user <u> fails and the HTTP status code is <http_status>

    Examples:
      | u   | http_status |
      | u1  | 204         |


  Scenario: Create the same user twice

    {User} Given the user <u> exists
    {User} Then creating the user <u> again fails and the HTTP status code is <http_status>

    Examples:
      | u   | http_status |
      | u1  | 409         |

      