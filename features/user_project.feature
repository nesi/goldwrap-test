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

