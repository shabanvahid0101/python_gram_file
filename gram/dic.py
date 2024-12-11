#
person1={
    "name":"vahid",
    "age":20,
    "hobby":"footbal"
}
print(person1)
person2=dict(name="ali",age=25,hobby="tenis")
print(person2)

#
person1={}
print(person1)
person2=dict()
print(person2)

#
person = {
    "name"  : "yamada", 
    "age"   : 17,
    "hobby" : "tenis"
}

if "name" in person:
    print("person has name")
else:
    print("person has not name")
if "music" in person :
    print("person has music")
else:
    print("person has not music")
    
#
nations1 = {
    "Japan" : "Tokyo",
    "USA" : "Washington DC",
    "England" : "London",
}
nations2 = {
    "France" : "Paris",
    "Germany" : "Berlin",
}
nations1.update(nations2)
print(nations1)

#
person1 = {
    "name"  : "yamada", 
    "age"   : 17,
    "hobby" : "tenis"
}
print(person1)

person2=dict(person1)
print(person2)

#
nations={"japan":"tokyo",
         "england":"london",
         "iran":"tehran",
         "france":"paris"}
print(nations)

for key in nations.keys():
    print(key)

for value in nations.values():
    print(value)

for key,value in nations.items():
    print(key + " ==>" +value)
    
#
nations3= {
    "Japan" : "tokyo",
    "England" : "london",
    "France" : "paris",
    "Spain" : "madrid",
}

for key,value in nations.items():
    print(f"{key} is the capital of {value}")
    
