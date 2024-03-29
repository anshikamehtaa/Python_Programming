#Boolean values can either be false or true
day="saturday"
temperatue=50
raining=True

#not means opposite of the decided value/true value(in this case)
#raining condition is true so not raining is false
if day=="saturday" and temperatue>30 and not raining:
    print("Go Swimming")
else:
    print("Not today")
print("*"*60)

#raining condition is true in this case
if day=="saturday" and temperatue>30 and raining:
    print("Go Swimming")
else:
    print("Not today")
print("*"*60)

#not>and>or precedence
#this will give wrong output because "not" is evaluated first even when the day condition is false
day="friday"
temperatue=50
raining=False
if day=="saturday" and temperatue>30 or not raining:
    print("Go Swimming")
else:
    print("Not today")

#using parenthesis to make clearer to understand
#use parenthesis when using two conditionals together
day="friday"
temperatue=50
raining=False
if (day=="saturday" and temperatue>30) or not raining:
    print("Go Swimming")
else:
    print("Not today")
print("*"*60)

print("TRUTHY VALUES!!")
#here the string itself is treated as a value
#if we enter enmpty string so if condition will not be evaluated and else will work
name=input("Please enter your name")
if name:
#if name!='' can be used instead
    print("Hello {}".format(name))
else:
    print("You seriously don't have any name??")
print("*"*60)

#letters and values are case sensitive
print("IN AND NOT IN!!")
city="Hyderabad"
letter=input("Enter a letter: ")
if letter in city:
    print("{} is in {}".format(letter,city))
else:
    print("Letter is not present")
print("*"*60)

city="Uttarakhand"
letter=input("Enter a letter: ")
if letter not in city:
    print("{} is not in {}".format(letter,city))
else:
    print("Letter is present")
print("*"*60)

#to avoid the case sensitive nature dusring string comparision we can use casefold
activity=input("What would you like to do? ")
if "gaming" not in activity.casefold():
    print("But gaming is my favourite thing to do")
else:
    print("Nice choice bro!!")
