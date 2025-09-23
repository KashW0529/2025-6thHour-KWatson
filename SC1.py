#Name: Kash
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.
Enemy_list = {
        'megachicken' : {
            'health' : 1200,
            'damage' : 400,
            'height' : 200,
            'speed' : 100,

        },
        'crusader' : {
            'health' : 100,
            'damage' : 10,
            'speed' : 5,
            'armor' : 17,
        },
        'dragon' : {
            'health' : 1000,
            'damage' : 600,
            'flight_speed' : 50,
            'armor' : 200,
            'firebreath' : 3000,
        },
        'samurai' : {
            'health' : 200,
            'damage' : 100,
            'speed' : 50,
            'armor' : 100,
            'special_attack' : 600,
        },
        'hippo' : {
            'health' : 150,
            'damage' : 150,
            'speed' : 35,
            'roll_ability' : 100
        }
}

user_choice = input('megachicken, crusader, dragon, samurai, hippo :')
print(Enemy_list[user_choice])
Enemy_list[user_choice].update({'damage' : int(input('choose damage :'))})
print(user_choice,Enemy_list[user_choice])