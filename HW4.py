#Name:
#Class: 6th Hour
#Assignment: HW4


#1. Print Hello World!
print('Hello World!')
#1. Create a list with 5 strings containing 5 different names in it.
name_List = ['greg','shane', 'yoker', 'jack','ben']
print(name_List)
#2. Append a new name onto the Name List.
name_List.append('James')
print(name_List)
#3. Print out the 4th name on the list.
print(name_List[3])
#4. Create a list with 4 different integers in it.
number_list=[1,6,7,8]
#5. Insert a new integer into the 2nd spot and print the new list.
number_list.insert(1,9)
#6. Sort the list from lowest to highest and print the sorted list.
number_list.sort()
#7. Add the 1st three numbers on the sorted list together and print the sum.
print(number_list[0]+number_list[1]+number_list[2])
#8. Create a list with two strings, two variables, and too boolean values.
big_list=['game','card', 3 , 2 , True , False]
print(big_list)
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(big_list[int(input('number 0 - 5:'))])