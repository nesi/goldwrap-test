Feature: Mapping users to projects

  Scenario: Add user to project

    {Project} Given project <p> exists
    {User} Given user <u> exists
    {Project} Given user <u> is not member of project <p>
    {Project} If I add user <u> to project <p>
    {Project} Then user <u> is member of project <p>
    
    Examples:
      | u  | p  | 
      | u1 | p1 |

  Scenario: Delete user and verify user isn't member of project anymore

    {Project} Given project <p> exists
    {User} Given user <u> exists
    {Project} Given user <u> is member of project <p>
    {User} If I delete user <u>
    {Project} Then user <u> is not member of project <p>
    
    Examples:
      | u  | p  | 
      | u1 | p1 |

