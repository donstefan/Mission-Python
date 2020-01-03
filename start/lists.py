#LISTS

friends = ["stefan", "jasmina", "vasi"]

friends[1] = "Mike"
print("You choose: " + friends[1])
print(friends[1:])

#LIST FUNCTIONS
lucky_number = [2, 3, 567, 87, 456, 8, 98]
#this always add to the end of the list
friends.append("Jel")

#insert to particular index
friends.insert(1, "The king")
friends.remove("Jel")

#remove the last element of the list
#friends.pop()


#this will remove all the elements from the list
#friends.clear()

#count the number of the king
friends.count("The king")

#sort in acceding
lucky_number.sort()

#sort in reverse
lucky_number.reverse()

#copy the list

friends2 = friends.copy()
print(friends2)
print(lucky_number)
#extended list (contacanate two lists)
friends.extend(lucky_number)
print(friends)

