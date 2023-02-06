"""Average Height 1.0"""
# student_heights = input("Enter the list of heights in cm, separated by a  space: ").split(" ")

# sum = 0
# count = 0

# for height in student_heights:
#   height = int(height)
#   sum += height
#   count += 1

# average = round(sum/count)
# print(f"The average height of the students is {average}cm")

"""Average Height 1.1"""
# student_heights = input("Enter the list of heights in cm, separated by a  space: ").split(" ")

# # range(0, len(student_heights)) is from 0 to len(student_heights) - 1! It does not include the upper bound.
# sum = 0
# count = 0 
# for n in range(len(student_heights)):
#   # Change each of the height from str to int
#   student_heights[n] = int(student_heights[n])
#   sum += student_heights[n]
#   count += 1

# average = round(sum / count)
# print(f"Average: {average}")

"""Highest Score"""
# student_scores = input("Input student scores, separated by space: ").split(" ")
# highest_score = 0
# for n in range(len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# for score in student_scores:
#   if score > highest_score:
#     highest_score = score

# print(f"The highest score in the class is: {highest_score}")

"""Adding Natural Numbers 1 to 100"""
# total = 0
# # range(1, 101) includes integers from 1 to 100 only.
# for number in range(1, 101): 
#   total += number
# print(total)

# """Adding Evens 1.0"""
# total = 0
# for number in range(0, 101, 2):
#   total += number
# print(f"The sum of even numbers from 1 to 100 is {total}")

# """Adding Evens 2.0"""
# lower_bound = int(input("Enter the first number: "))
# upper_bound = int(input("Enter the second number: "))

# total_of_evens = 0
# for number in range(lower_bound, upper_bound + 1):
#   if number % 2 == 1:
#     total_of_evens += 0
#   else:
#     total_of_evens += number
# # print the sum of even numbers
# print(f"The sum of the even numbers is: {total_of_evens}")

# # FUN FACT: For any range you try to check the sum of the evens against the odds, the sum of evens is always higher except both bounds are odd or lower bound is even and the upper is odd.
# total_of_odds = 0
# for number in range(lower_bound, upper_bound + 1):
#   if number % 2 == 0:
#     total_of_odds += 0
#   else:
#     total_of_odds += number
# # print the sum of odd numbers
# print(f"The sum of the odd numbers is: {total_of_odds}")

"""Fizz Buzz"""
begin = int(input("First number: "))
end = int(input("Last number: "))

for number in range(begin, end + 1):
  # This logic is not fully considered if it placed after any or both of the two other conditions.
  # Also, the idea of writing number % 3 == 0 and number % 5 == 0 would just be unnecessary since it implies the L.C.M, which is 15. One complete check is better than two checks.
  if number % 15 == 0:
    print('FizzBuzz')
  elif number % 3 == 0:
    print('Fizz')
  elif number % 5 == 0:
    print('Buzz')
  else:
    print(number)