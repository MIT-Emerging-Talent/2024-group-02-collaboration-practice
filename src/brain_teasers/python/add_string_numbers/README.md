Author: tvsirius
Date 18/01/2024

Adding string numbers challenge for learning

Simple task, all done.


I have come to this error with tests:

```Traceback (most recent call last):
     self.assertEqual(add_string_numbers("1.1", "2.2"), "3.3")
AssertionError: '3.3000000000000003' != '3.3'
 - 3.3000000000000003
 + 3.3
```
So I come up with idea of rounding the result to constant like ROUND_CONSTANT=15

Then I invented more complex solution, I get the number or digits of original numbers, 
and round the result to the maximum of digits plus 1, so this kind of error will be avoided
