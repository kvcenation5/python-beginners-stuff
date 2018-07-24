dinner=['Arun', 'Kumaran' , 'Rajesh']
print(dinner)

print("Welcome " + dinner[0] +  " afer a long time" )
print("Hello " + dinner[1] + " As usual we have a drink party")
print("Hi " + dinner[2] + " hope you come for sure this time")

print("Unfortunately " + dinner[2] + "  cannot come due to some official emergency")
dinner[2]='Rajaraman'
print("So "+ dinner[2] + " will be joining us" )
print(dinner[0]+ " ," + dinner[1]+ " and " + dinner[2])
print("The list of people coming to the dinner party")
for i in dinner:
    print (i)

print("Welcome " + dinner[0] +  ", afer a long time" )
print("Hello " + dinner[1] + ", As usual we have a drink party")
print("Dear " + dinner[2] + ", pleased to welcome you" )

print("We just figured we got a big dinner table so get excited as more of our friends circle will be joining us")

dinner.insert(0,'Selva')
dinner.insert(2,'Mahendran')
dinner.append('Babu')

print(dinner)

print("The Revised list finally :)")
for i in dinner:
    print (i)   

for i in dinner:
    print("A Welcome message to everyone: " + i) #Indentation error, it should be a tab space where the line followed by for to not get IndentationError

print("Unfortunately we can accomodate onky two persons for now and we will be announcing the two lucky winners")

print(dinner[4])
print(dinner[5])
print(dinner)
#When adding a pop the array index value decreases every step as they are being removed. So have to adjust the list accordingly

dinner_list1 = dinner.pop(0)
print(dinner)
dinner_list2 = dinner.pop(1)
print(dinner)
dinner_list3 = dinner.pop(3)
print(dinner)
dinner_list4 = dinner.pop(2)
print(dinner)

print("Deeply saddened to let you go : " + dinner_list1)

print("Deeply saddened to let you go : " + dinner_list2)

print("Deeply saddened to let you go : " + dinner_list3)

print("Deeply saddened to let you go : " + dinner_list4)

print(dinner)

for i in dinner:
    print("The Lucky joinees for the dinner are : " + i)

del dinner[0]
del dinner[0]
#Since the max entry on the array has already been removed two '0's

print(dinner)

print("The list at the end of the day for dinner, lol " + dinner)

#Try this execution so it can print all the pop list
'''system = 0
for i = 2:
    print dinner_list[i]'''

