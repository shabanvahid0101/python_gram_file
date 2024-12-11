#list
#[6, 2, 6, 8]
number1=[1,3,5,6,3,1,3,2,6,7,8]
number2=[x for x in number1 if x%2==0]
print(number2)

#append
# ['orange', 'apple', 'melon']
# ['orange', 'apple', 'melon', 'peach']
# ['orange', 'apple', 'melon', 'peach', 'banana']
fruits = ["orange","apple","melon"]
print(fruits)
fruits.append("peach")
print(fruits)
fruits.append("banana")
print(fruits)

#insert
# ['orange', 'apple', 'melon']
# ['orange', 'apple', 'peach', 'melon']
# ['orange', 'banana', 'apple', 'peach', 'melon']
fruits = ["orange","apple","melon"]
print(fruits)
fruits.insert(2,"peach")
print(fruits)
fruits.insert(1,"banana")
print(fruits)

#remove
# ['orange', 'apple', 'melon', 'grape', 'peach']
# ['orange', 'apple', 'melon', 'peach']
# ['orange', 'apple', 'peach']
fruits = ["orange","apple","melon","grape","peach"]
print(fruits)
fruits.remove("grape")
print(fruits)
fruits.remove("melon")
print(fruits)

#del
# ['orange', 'apple', 'melon', 'grape', 'peach']
# ['orange', 'apple', 'melon', 'peach']
# ['orange', 'apple', 'peach']
fruits = ["orange","apple","melon","grape","peach"]
print(fruits)
del fruits[3]
print(fruits)
del fruits[2]
print(fruits)

#sort
# [5, 8, 2, 9, 13, 10]
# [2, 5, 8, 9, 10, 13]
# [13, 10, 9, 8, 5, 2]
numbers1 = [5,8,2,9,13,10]
print(numbers1)
numbers1.sort()
print(numbers1)
numbers1.sort(reverse=True)
print(numbers1)

#reverse
# ['Ariana', 'Nancy', 'Lucy', 'Meg']
# ['Meg', 'Lucy', 'Nancy', 'Ariana']
names = ["Ariana","Nancy","Lucy","Meg"]
print(names)
names.reverse()
print(names)

#sum
#30
numbers = [5,3,7,2,9,4]
total =sum(numbers)
print (total)

#[12, 9, 18, 6, 27, 15]
numbers = [4,3,6,2,9,5]
numbers2=[i*3 for i in numbers]
print(numbers2)

#[3, 6, 9]
numbers = [4,3,6,2,9,5]
numbers2=[x for x in numbers if x%3==0]
print(numbers2)


