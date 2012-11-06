Feature: Add user to project

  Scenario: Add user to project

    {Project} Given the project <p> exists
    {User} Given the user <u> exists
    {Project} Given the user <u> is not a member of project <p>
    {Project} If I add the user <u> to project <p>
    {Project} Then the user <u> is member of project <p>
    
    Examples:
      | u  | p  | 
      | u1 | p1 |

  Scenario: Delete user and verify user isn't member of project anymore

    {Project} Given the project <p> exists
    {User} Given the user <u> exists
    {Project} Given the user <u> is a member of project <p>
    {User} If I delete the user <u>
    {Project} Then the user <u> is not a member of project <p>
    
    Examples:
      | u  | p  | 
      | u1 | p1 |

