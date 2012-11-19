Feature: User

  Scenario: Create new user
  
    {User} Given user <u> does not exist
    {User} Then I can create user <u> and the HTTP status code is <http_status>

    Examples:
      | u  | http_status   |
      | u1 | 204           |


  Scenario: Get existing user

    {User} Given user <u> exists
    {User} Then I can get user <u>

    Examples:
      | u  |
      | u1 |


  Scenario: See existing user in user list

    {User} Given user <u> exists
    {User} Then I see user <u> in the user list

    Examples:
      | u  |
      | u1 |

  Scenario: Update existing user

    {User} Given user <u> exists
    {User} Then I can update user <u> with new email <e>

    Examples:
      | u  | e                 |
      | u1 | newemail@test.com |


  Scenario: Delete user

    {User} Given user <u> exists
    {User} Then I can delete user <u> and the HTTP status code is <http_status>

    Examples:
      | u   | http_status |
      | u1  | 204         |


  Scenario: Get non-existing user

    {User} Given user <u> does not exist
    {User} Then getting user <u> fails and the HTTP status code is <http_status>

    Examples:
      | u   | http_status |
      | u1  | 404         |


  Scenario: Delete non-existing user

    {User} Given user <u> does not exist
    {User} Then deleting user <u> fails and the HTTP status code is <http_status>

    Examples:
      | u   | http_status |
      | u1  | 204         |


  Scenario: Create the same user twice

    {User} Given user <u> exists
    {User} Then creating user <u> again fails and the HTTP status code is <http_status>

    Examples:
      | u   | http_status |
      | u1  | 409         |

      