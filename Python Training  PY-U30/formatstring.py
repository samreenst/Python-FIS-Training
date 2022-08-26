place="Chennai"
name = "Samreen"
info = ("I am from {}, my name is {}")
print(info.format(place,name))
name='tommy timmy'
name1=name.replace('m','n')
print(name1.strip())

#to reverse
place2=place[::-1]
print(place2)

#to check palindrome
if(place2==place):
    print("The string is palindrome")
else:
    print("It is not a palindrome")


