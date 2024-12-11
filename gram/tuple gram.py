#tuple
#(4, 2, 5, 7, 6)
#(4, 2, 5, 7, 6)
numbers1 = (4,2,5,7,6)
print (numbers1)
numbers2=tuple([4,2,5,7,6])
print(numbers2)

#()
#()
numbers1=()
print(numbers1)
numbers2=tuple()
print(numbers2)

# (4, 2, 5, 7, 6)
# (4, 2, 5, 7, 6)
numbers1 = (4,2,5,7,6)
print (numbers1)
numbers2=tuple(numbers1)
print(numbers2)

# ('red', 'blue', 'green', 'yellow', 'pink', 'black')
# ('red', 'blue', 'green')
# ('green', 'yellow')
# ('yellow', 'pink', 'black')
# ('red', 'green', 'pink')
# ('black', 'pink', 'yellow', 'green', 'blue', 'red')
# colors1 = ("red","blue","green","yellow","pink","black")
print(colors1)
colors2=colors1[0:3]
print(colors2)
colors3=colors1[2:4]
print(colors3)
colors4=colors1[3:]
print(colors4)
colors5=colors1[::2]
print(colors5)
colors6=colors1[::-1]
print(colors6)

#('yamada', 'tarou')
# yamada
# tarou
name = ("yamada","tarou")
print(name)
last_name,first_name=name
print(last_name)
print(first_name)

# 0==>red
# 1==>blue
# 2==>green
# 3==>yellow
colors = ("red","blue","green","yellow")
for index,value in enumerate(colors):
    print(str(index)+"==>"+value)
    
