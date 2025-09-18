#Name: Kash Watson
#Class: 6th Hour
#Assignment: HW7

#1. Print Hello World!
print('hello world!')
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
gregsCarDict = {
    'brand' : 'ford',
    'model' : 'freestyle',
    'year'  : [2006, 2025, 2012]
}
#3. Print the keys of the dictionary from #2.
print(gregsCarDict.keys())
#4. Print the values of the dictionary from #2
print(gregsCarDict.values())
#5. Print one of the three numbers from the list by itself
print(gregsCarDict['brand'])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
gregsCarDict.update({'cost': [7000]})
#7. Print the entire dictionary from #2 with the updated key and value.
print(gregsCarDict)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
my_class = {
    "friend_1" : {
        "Name" : "Greg",
        "Grade" : 12,
        "Sports" : False,
    },
    "friend_2" : {
        "Name" : "Shane",
        "Grade" : 12,
        "Sports" : False,
    },
    "friend_3" : {
        "Name" : "Aaden",
        "Grade" : 11,
        "Sports" : True,
    },
}
#9. Print the names of all three classmates on the same line.
print(my_class['friend_1']['Name'], my_class['friend_2']['Name'], my_class['friend_3']['Name'])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.