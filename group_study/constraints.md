<!-- this template is for inspiration, feel free to change it however you like! -->

# Constraints


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

    
    # This way everyone will know, includes interpreter the variable my_var has type of MyClass
    my_var:MyClass = MyClass()


    # func do_some has a parameter of integer and string, and MyClass
    def do_some(number, word, variable):
      # do something
    
    If we will leave it as is someone could pass to number say float, and program will throw an error, and it will require some debugging, etc.

    This is why declaring func parameters we should notate types of parameters like that
    
    def do_some(number:int, word:str, variable:MyClass):
      # do something






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
