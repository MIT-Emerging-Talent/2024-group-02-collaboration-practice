<!-- this template is for inspiration, feel free to change it however you like! -->

# Constraints

Language: Python
Platform for repository: [GitHub](https://github.com/MIT-Emerging-Talent/2024-group-02-collaboration-practice)
Project Board: [GitHub Project](https://github.com/orgs/MIT-Emerging-Talent/projects/19/views/1)


## Naming conventions:

    Using snake_case with Python:
    - for constants **CONSTANT**, **MY_CONSTANT**, etc
    - for classes **ClassName**, **MyClass**, etc
    - for methods and functions **method_name** or **my_fun**, etc
    - for parameters, arguments and variables **my_variable**, **my_arg**, **some_parameter**, etc


## Type notation is must
    
    example:

    class MyClass:
      # class scope

    # We are try to use Type Notaion, declaring variables, like that:
    # This way everyone will know, includes interpreter the variable my_var has type of MyClass

    my_var:MyClass = MyClass()
    counter:int = 1


    # We are declaring function parameters using Type Notaion, like that:

    def do_some(number:int, word:str, variable:MyClass) -> None:
      # do something, no return

    def do_some(number:int, word:str, variable:MyClass) -> float:
      # do something, return something

    def some_function(list_of_ints:list[int],)

    








## External

<!--
  constraints coming from the outside that your team has no control over. these may include:
  - project deadlines
  - number of unit tests required to pass a code review
  - technologies (sometimes a client will tell you what to use)
-->

## Internal: Involuntary

<!--
  constraints that come from within your team, and you have no control over. they may include:
  - each of your individual skill levels
  - amount of time available to work on the project
-->

## Internal: Voluntary

<!--
  constraints that your team decided on to help scope the project. they may include:
  - coding style & conventions
  - agree on a code review checklist for the project repository
  - the number of hours you want to spend working
  - only using the colors black and white
-->
