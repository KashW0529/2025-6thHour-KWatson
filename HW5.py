#Name: Kash Watson
#Class: 6th Hour
#Assignment: HW5

#1. Create a list with 9 different numbers inside.
Num_list=[9,8,7,6,5,4,3,2,1]
#2. Sort the list from highest to lowest.
Num_list.sort(reverse=True)
#3. Create an empty list.
Empty_list=[]
#4. Remove the median number from the first list and add it to the second list
Who=Num_list[4]
Num_list.pop(4)
Empty_list.append(Who)
#5. Remove the first number from the first list and add it to the second list.
Who2=Num_list[0]
Num_list.pop(0)
Empty_list.append(Who2)
#6. Print both lists.
print(Num_list)
print(Empty_list)
#7. Add the two numbers in the second list together and print the result.
Car=Empty_list[0]+Empty_list[1]
print(Car)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
Empty_list.pop(0)
Empty_list.pop(0)
Num_list.append(Car)
print(Num_list)
#9. Sort the first list from lowest to highest and print it.
Num_list.sort()
print(Num_list)