# difference between function and lambda
# The core difference between Python def functions and lambda functions lies in their syntax, naming, and complexity:
# lambda functions are anonymous, single-expression functions designed for short, one-time use,
# while def functions are named, multi-statement functions suitable for complex, reusable logic.

# lambda has its own keywords
# | Function Name | Functionality                                                      |
# | ------------- | ------------------------------------------------------------------ |
# | `map()`       | Applies a lambda function to each item in an iterable              |
# | `filter()`    | Filters elements based on a condition in lambda                    |
# | `sorted()`    | Sorts elements using a lambda as a key function                    |
# | `reduce()`    | Reduces iterable to a single value using lambda (from `functools`) |

x=lambda y:y*y

print(x(2))  # 4

##########################
lst = [1,2,3,4,5,6,7,8,9,10]
lst2=list(filter(lambda x:(x%2==0),lst))
lis3=list(filter(lambda x:(x%2!=0),lst))

print(lst2) #[2, 4, 6, 8, 10]
print(lis3) #[1, 3, 5, 7, 9]
