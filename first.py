import math 

# def find_gcd(a, b ) : 
#      if ( b == 0 ): 
#           return a 
#      else : 
#           return math.gcd(a ,b )

# a = 10 
# b = 2 
# print( "GCD is : ", find_gcd(a, b)) 

# a = 100 
# b = 27 
# print("GCD is : ", math.gcd(a, b))
# print("LCM is ", math.lcm(a , b ))
# print("Factorial is ", math.factorial(5))
# print("Square root is ", math.isqrt(25))
# print ('he\'s a good person')
# name = "monikumar"
# print('e' in name )
# list_v = list(name)
# print(list_v) 
# marks = [ 23, 45, 90, 67, 89 ]
# marks.sort()
# print(marks)
# print(max(marks))
# print(min(marks))
# print(marks[:])
# print(len(marks))
# marks[1] = 100
# print(marks)


# example_list = "monikumarbiswas"
# list_item = list(example_list) 
# print(list_item)
# list_item[4:] = "kumar"
# print(list_item)
# list_item[ :4] = []
# print(list_item)


example_list = [1, 2, 3, 4, 5, 5, 7, 8, 9]
print(example_list.count(5))

item = [ "moni", "kumar", "biswas" ]

example_list =  item  + example_list
print(example_list)
example_list.extend([ 10, 'a', 12 ])
print(example_list)

