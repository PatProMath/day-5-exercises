# day-5-exercises

## Average Height
A program that calculates the average student height from a List of heights.

### Instructions
This is very basic: the *average height* can be calculated by adding all the heights together and dividing by the total number of heights.

However, you are required to not use either the `len()` or the `sum()` methods of list. Instead attempt to replicate their functionalities. 

Also, the average height value should be rounded up to the nearest whole number.

## Highest Score
A program that calculates the highest score from a list of scores

### Instructions

__Important____  You are not allowed to use the `max()` or `min()` functions. 

Figure out a way to compare numbers for size.

```
Input student scores, separated by space: 78 90 99 34 67 98 12
The highest score in the class is: 99
```

## Adding Evens

A program that calculates the sum of all the even numbers from a number to another number.

### Instructions
You are going to write a program that calculates the sum of all the even numbers from a lower bound to an upper bound. For example, given 1 and 100. We are looking at the numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

**Important** 
1. The second number or the upper bound must be included in the addition.
2. There should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

### Fun Fact: For any range you try to check the sum of the evens against the odds, the sum of evens is always higher except both bounds are odd or lower bound is even and the upper is odd.

## Fizz Buzz Game
A program that gives out the output to a fizz buzz game.

### Instructions
Create a program that gives the output to a Fizz Buzz game. The program should print the numbers in turn and ...
1. When the number is divisible by 3 then instead of printing the number it should print "Fizz".
2. When the number is divisible by 5, then instead of printing the number it should print "Buzz".
3. And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz".

### Expected program output
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```