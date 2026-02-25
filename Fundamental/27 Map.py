# | Function Name | Functionality                                                      |
# | ------------- | ------------------------------------------------------------------ |
# | `map()`       | Applies a lambda function to each item in an iterable              |
# | `filter()`    | Filters elements based on a condition in lambda                    |
# | `sorted()`    | Sorts elements using a lambda as a key function                    |
# | `reduce()`    | Reduces iterable to a single value using lambda (from `functools`) |


x=[10,20,30,40,50,60,70,80,90,100]

y=list(map(lambda a:a*2,x))
print(y)

# [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
#####################################
x = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]

z = list(map(lambda a,b:a*b,x,y))
print(z)