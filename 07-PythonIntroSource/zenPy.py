# # #Zen principles of Python
# #
# # # Principle 1: Beautiful is better than ugly.
# # # What not to do:
# # a=5;b=10;print("Sum:",a+b)
# # # What to do:
# # a = 5
# # b = 10
# # sum_result = a + b
# # print("Sum:", sum_result)
# #
# # # Principle 2: Explicit is better than implicit.
# # # What not to do:
# # def calculate_area(radius):
# #     return 3.14 * radius * radius
# # # What to do:
# # def calculate_area_explicitly(radius):
# #     pi = 3.14
# #     return pi * radius * radius
# #
# # # Principle 3: Simple is better than complex.
# # # What not to do:
# # def factorial_complex(n):
# #     if n == 0 or n == 1:
# #         return 1
# #     else:
# #         return n * factorial_complex(n-1)
# # # What to do:
# # def factorial_simple(n):
# #     result = 1
# #     for i in range(1, n+1):
# #         result *= i
# #     return result
# #
# # # Principle 4: Complex is better than complicated.
# # # What not to do:
# # def complicated_logic(x, y):
# #     result = (x + y) * (x - y) / (x * x + y * y)
# #     return result
# # # What to do:
# # def complex_logic(x, y):
# #     numerator = (x + y) * (x - y)
# #     denominator = x * x + y * y
# #     result = numerator / denominator
# #     return result
# #
# # # Principle 5: Flat is better than nested.
# # # What not to do:
# # def nested_structure(a, b):
# #     if a > b:
# #         if a % b == 0:
# #             return "Divisible"
# #         else:
# #             return "Not divisible"
# #     else:
# #         return "Invalid"
# # # What to do:
# # def flat_structure(a, b):
# #     if a <= b or a % b != 0:
# #         return "Invalid"
# #     return "Divisible"
# #
# # # Principle 6: Sparse is better than dense.
# # # What not to do:
# # dense_code = [x*2 for x in range(10) if x % 2 == 0]
# # # What to do:
# # sparse_code = []
# # for x in range(10):
# #     if x % 2 == 0:
# #         sparse_code.append(x*2)
# #
# # # Principle 7: Readability counts.
# # # What not to do:
# # x=10;y=5;z=2;x+=y;z*=x;result=x+z;print(result)
# # # What to do:
# # initial_value = 10
# # increment_value = 5
# # multiplier = 2
# # x = initial_value + increment_value
# # z = multiplier * x
# # result = x + z
# # print(result)
# #
# # # Principle 8: Special cases aren't special enough to break the rules.
# # # What not to do:
# # def special_case_handling(value):
# #     if value == 42:
# #         return "The Answer"
# #     elif value == 0:
# #         return "Zero"
# #     else:
# #         return "Other value"
# # # What to do:
# # def generic_case_handling(value):
# #     return f"Value: {value}"
# #
# # # Principle 9: Although practicality beats purity.
# # # What not to do:
# # def pure_function():
# #     # Pure function with side effect
# #     print("Hello, I'm pure!")
# #     return True
# # # What to do:
# # def practical_function():
# #     # Practical function with side effect
# #     print("Hello, I'm practical!")
# #     return True
# #
# # # Principle 10: Errors should never pass silently.
# # # What not to do:
# # try:
# #     result = 10 / 0
# # except:
# #     pass
# # # What to do:
# # try:
# #     result = 10 / 0
# # except ZeroDivisionError as e:
# #     print(f"Error: {e}")
# #
# # # Principle 11: Unless explicitly silenced.
# # # What not to do:
# # try:
# #     result = 10 / 0
# # except ZeroDivisionError as e:
# #     pass
# # # What to do:
# # try:
# #     result = 10 / 0
# # except ZeroDivisionError as e:
# #     print(f"Error: {e}")
# #
# # # Principle 12: In the face of ambiguity, refuse the temptation to guess.
# # # What not to do:
# # def guess_result(a, b):
# #     return a + b
# # # What to do:
# # def avoid_guessing(a:int, b:int)->str:
# #     return f"Sum of {a} and {b}"
# #
# # # Principle 13: There should be one—and preferably only one—obvious way to do it.
# # # What not to do:
# # def multiple_ways_to_format(a, b):
# #     return "Result: {}".format(a + b)
# # # What to do:
# # def obvious_way_to_format(a, b):
# #     return f"Result: {a + b}"
# #
# # # Principle 14: Although that way may not be obvious at first unless you're Dutch.
# # # What not to do:
# # def non_obvious_code():
# #     a = [1, 2, 3]
# #     b = [4, 5, 6]
# #     result = a + b
# # # What to do:
# # def obvious_code():
# #     a = [1, 2, 3]
# #     b = [4, 5, 6]
# #     a.extend(b)
# #     result = a
# #
# # # Principle 15: Now is better than never.
# # # What not to do:
# # def delayed_action():
# #     import time
# #     time.sleep(5)
# #     print("Action performed!")
# # # What to do:
# # def immediate_action():
# #     print("Performing action now!")
# #
# # # Principle 16: Although never is often better than right now.
# # # What not to do:
# # def rushed_implementation():
# #     # ... code with potential issues ...
# # # What to do:
# # def careful_implementation():
# #     # ... well-thought-out code ...
# #
# # # Principle 17: If the implementation is hard to explain, it's a bad idea.
# # # What not to do:
# # def cryptic_logic(a, b):
# #     result = (a * b) // (a + b)
# #     return result
# # # What to do:
# # def clear_logic(a, b):
# #     numerator = a * b
# #     denominator = a + b
# #     result = numerator // denominator
# #     return result
# #
# # # Principle 18: If the implementation is easy to explain, it may be a good idea.
# # # What not to do:
# # def calculate_average(values):
# #     total = sum(values)
# #     count = len(values)
# #     average = total / count
# #     return average
# # # What to do:
# # def calculate_average(values):
# #     total = sum(values)
# #     count = len(values)
#     average = total / count
#     return average
#
# # Principle 19: Namespaces are one honking great idea—let's do more of those!
# # What not to do:
# import module
# from module import *
# # What to do:
# from module import specific_function  # Import only the specific function
