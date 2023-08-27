import random as r


def random_game(start_input, genre_input):
    game_dic = {
        'Singleplayer': {'RPG': ['Skyrim', "Baldur's Gate 3", 'Witcher 3', 'Outer Worlds',
                                 'Dragon Age:Origins', 'Red Dead Redemption 2', 'Mass Effect', 'Walking Dead',
                                 'Fallout'],
                         'Action': ['Assassins Creed', 'God of War', 'Spider-Man', 'Halo', 'Call of Duty',
                                    'Battlefield', 'Hades', 'Dead Cells'],
                         'Horror': ['Dead Space', 'Outlast', 'Resident Evil', 'Amnesia', 'F.E.A.R',
                                    'Alan Wake', 'Silent Hill', "Five nights at Freddy's"],
                         'Adventure': ['Only Up', 'Fire Watch', 'Zelda: Breath of the Wild', 'Metro: Exodus',
                                       'Dishonored', "A Bard's Tale", 'Ori and the Blind Forest'],
                         'Strategy': ['Frost Punk', 'Sim City', 'Roller Coaster Tycoon', 'XCOM',
                                      'Command and Conquer', 'Prison Architect']},
        'Multiplayer': {'RPG': ['Elder Scrolls Online', 'World of Warcraft', 'Diablo IV', 'Fallout 76',
                                'Star Wars: The Old Republic'],
                        'Action': ['Rainbow 6 Siege', 'Deep Rock Galactic', "Valorant", 'Overwatch 2',
                                   'Apex Legends', 'Escape from Tarkov'],
                        'Horror': ['Dead by Daylight', 'Dying Light', 'Deceit', 'Phasmaphobia',
                                   'No More Room in Hell', 'Outlast:Trials'],
                        'Adventure': ['Star Citizen', 'Dark Souls', 'Genshin Impact', 'Grand Theft Auto',
                                      'Valheim'],
                        'Strategy': ['Civilization', 'Total War', 'League of Legends', 'Starcraft',
                                     "Bloons Tower Defence 6"]},
        'Cooperative': {'RPG': ["Baldur's Gate 3", "Monster Hunter Rise", "Elden Ring",
                                "Divinity: Original Sin", "Terraria", "Warframe"],
                        'Action': ['It Takes two', 'Army of two', 'A Way Out', 'Splinter Cell',
                                   "Gears of War 5"],
                        'Horror': ['Dead Space 3', 'The Forest', 'Cry of Fear', 'Pacify', 'Dead Island 2',
                                   'Remnant 2'],
                        'Adventure': ['Minecraft', 'Borderlands 3', 'Stardew Valley', 'Trine',
                                      'Brothers: A Tale of two Sons', 'For the King'],
                        'Strategy': ['Chess', "Untitled Goose Game", 'Pandemic', 'Stelaris', 'No Man Sky'
                                                                                             'Total War: Three Kingdoms']},
    }
    len_list = len(game_dic[start_input][genre_input])
    index = r.randint(0, len_list - 1)
    videogame = game_dic[start_input][genre_input][index]
    return print("\nHere is your random video game: ", videogame)


def dic_sorter(start_input, genre_input):
    game_dic = {
        'Singleplayer': {'RPG': ['Skyrim', "Baldur's Gate 3", 'Witcher 3', 'Outer Worlds',
                                 'Dragon Age:Origins', 'Red Dead Redemption 2', 'Mass Effect', 'Walking Dead',
                                 'Fallout'],
                         'Action': ['Assassins Creed', 'God of War', 'Spider-Man', 'Halo', 'Call of Duty',
                                    'Battlefield', 'Hades', 'Dead Cells'],
                         'Horror': ['Dead Space', 'Outlast', 'Resident Evil', 'Amnesia', 'F.E.A.R',
                                    'Alan Wake', 'Silent Hill', "Five nights at Freddy's"],
                         'Adventure': ['Only Up', 'Fire Watch', 'Zelda: Breath of the Wild', 'Metro: Exodus',
                                       'Dishonored', "A Bard's Tale", 'Ori and the Blind Forest'],
                         'Strategy': ['Frost Punk', 'Sim City', 'Roller Coaster Tycoon', 'XCOM',
                                      'Command and Conquer', 'Prison Architect']},
        'Multiplayer': {'RPG': ['Elder Scrolls Online', 'World of Warcraft', 'Diablo IV', 'Fallout 76',
                                'Star Wars: The Old Republic'],
                        'Action': ['Rainbow 6 Siege', 'Deep Rock Galactic', "Valorant", 'Overwatch 2',
                                   'Apex Legends', 'Escape from Tarkov'],
                        'Horror': ['Dead by Daylight', 'Dying Light', 'Deceit', 'Phasmaphobia',
                                   'No More Room in Hell', 'Outlast:Trials'],
                        'Adventure': ['Star Citizen', 'Dark Souls', 'Genshin Impact', 'Grand Theft Auto',
                                      'Valheim'],
                        'Strategy': ['Civilization', 'Total War', 'League of Legends', 'Starcraft',
                                     "Bloons Tower Defence 6"]},
        'Cooperative': {'RPG': ["Baldur's Gate 3", "Monster Hunter Rise", "Elden Ring",
                                "Divinity: Original Sin", "Terraria", "Warframe"],
                        'Action': ['It Takes two', 'Army of two', 'A Way Out', 'Splinter Cell',
                                   "Gears of War 5"],
                        'Horror': ['Dead Space 3', 'The Forest', 'Cry of Fear', 'Pacify', 'Dead Island 2',
                                   'Remnant 2'],
                        'Adventure': ['Minecraft', 'Borderlands 3', 'Stardew Valley', 'Trine',
                                      'Brothers: A Tale of two Sons', 'For the King'],
                        'Strategy': ['Chess', "Untitled Goose Game", 'Pandemic', 'Stelaris', 'No Man Sky'
                                                                                             'Total War: Three Kingdoms']},
    }
    game_list = game_dic[start_input][genre_input]
    print('\nHere is a list of', start_input, genre_input, 'games:')
    print(game_list)


def restart_check(start_input):
    start_list = ('Singleplayer', 'Multiplayer', 'Cooperative')
    genre_list = ('RPG', 'Action', 'Horror', 'Adventure', 'Strategy')
    if start_input == 'Quit':
        print('Have a nice day!!')
        exit()
    elif start_input == 'Restart':
        videogame_picker()
    elif start_input in start_list or genre_list:
        return start_input
    else:
        print("I'm sorry I dont understand \nPlease try again")


def videogame_picker():
    print()
    print('Welcome to game picker 3000.                         Type "Quit" or "Restart" at anytime to quit/restart\n'
          'I hear you want help finding a game to play.')
    print('You have come to the right place\n'
          'PLease help us by choosing who you want to play your game with.     (This answer is case sensitive)')
    print()

    start_input = input('(Singleplayer|Multiplayer|Cooperative)   ')
    restart_check(start_input)
    print("Excellent!! \n"
          "There are plenty of genres to choose from please pick your favorite below: \n")
    genre_input = input('(RPG|Action|Horror|Adventure|Strategy)     ')
    restart_check(genre_input)
    dic_sorter(start_input, genre_input)

    print('\nWould you like to get a random game off of this list? If so please say "yes" \n'
          'Otherwise you can say "Restart" or "Quit"')
    end_input = input("(Random|Quit|Restart)   ")
    restart_check(end_input)
    random_game(start_input, genre_input)
    print()
    print('Thank you for using game picker 3000\n'
          'I hope you enjoy your game, you can now restart or quit')
    final_input = input("(Quit|Restart)   ")
    restart_check(final_input)


if __name__ == '__main__':
    videogame_picker()