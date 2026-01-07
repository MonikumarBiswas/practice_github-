# def find_letter( String , value ):
#    return value in String 
    

# letter = input("Enter the letter to be searched: ")
# print(find_letter("monikumarbiswas", letter))

# def reverse_string( str ): 
   
#     length = len(str)
#     return str[length-1 : : -1]

# print(reverse_string("helloworld"))

# str = "abcdefghijklmnopqrstuvwxyz"
# i = 0 
# str2 = input("Enter the string: ")
# ans = ''
# while ( i < len(str2) ):
#  j = str.find(str2[i])
#  print(j)
#  ans += str[(j+4)% 26]
#  i += 1

# print(ans)



# def count_occurence( str , word1 , word2 ): 
#     count1 = str.count(word1)
#     count2 = str.count(word2)
     
#     if( count1 == count2):
#        return True 
#     else :
#       return False 
    
# string = "catdogcatdog"
# print(count_occurence(string , "cat" , "dog"))

# numbers = { 1 , 5 ,3 ,3 , 4, 5 }
# print(type(numbers))
# print(numbers)
# numbers.add(10)
# print(numbers)
# numbers.remove(3)
# print(numbers)

# people = {"Jay", "Idrish", "Archi"}
# people.add(1)
# print(people)

# for i in range(1, 6):
#     people.add(i)

# print(people)

# flowers = {"rose", "lily", "tulip"}
# fruits = {"apple", "banana", "mango","rose"}

# print(flowers.union(fruits))
# print(flowers.intersection(fruits))
# print(flowers.difference(fruits))

# print(flowers|fruits)
# print(flowers & fruits)
# fruits.clear()
# print(fruits)


# dic1 = { "name" : "monikumar",
#         "age" : 23 ,
#         "city" : "sylhet",
#         1 : (1,2,3),
#         2: (4,5,6),
#         (1,"Monikumar") : "hello",
#         3 :{
#             "a" : 10 ,
#             "b" : 20
#         }
#         }
# dic1["profession"] = "student"
# dic1["age"] = 24 

# del dic1["city"]
# print(dic1.pop((1, "Monikumar")))
# print(dic1.popitem()) 
# print(dic1)


# students = {}

# students['student1'] = {'name': 'Drake', 'age': 20, 'grade': 'A'}
# students['student2'] = {'name': 'Travis', 'age': 22, 'grade': 'B'}
# students['student3'] = {'name': 'Charlie', 'age': 21, 'grade': 'A+'}

# students['student2']['city'] = "sylhet"
# del students["student3"]["grade"]
# students["student4"] = {'name': 'Monikumar', 'age': 23, 'grade': 'A'}
# print("Student Details:")
# print(students)


# dic2 = dict( name = "monikumar" , age = 23 , city = "sylhet"  )
# print(dic2) 

