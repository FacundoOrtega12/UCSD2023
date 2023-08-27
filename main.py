
character_dic = { 'Races': ['Aarakocra', 'Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Goliath' , 'Half-elf', 'Halfling',
                            'Half-Orc', 'Half-Elf', 'Human', 'Tiefling'],
                  'Classes': {'Barbarian': 'A fierce warrior of primitive background who can enter a battle rage',
                              'Bard': 'An inspiring magician whose power echoes the music of creation',
                              'Cleric': 'A priestly champion who wields divine magic in service of a higher power',
                              'Druid': 'A priest of the Old Faith, wielding the powers of nature — moonlight and '
                                       'plant growth, fire and lightning — and adopting animal forms',
                              'Fighter': 'A master of martial combat, skilled with a variety of weapons and armor',
                              'Monk': 'A master of martial arts, harnessing the power of the body in pursuit of '
                                      'physical and spiritual perfection',
                              'Paladin': 'A holy warrior bound to a sacred oath',
                              'Ranger': 'A warrior who uses martial prowess and nature magic to combat threats on the '
                                        'edges of civilization',
                              'Rogue': 'A scoundrel who uses stealth and trickery to overcome obstacles and enemies',
                              'Sorcerer': 'A spellcaster who draws on inherent magic from a gift or bloodline',
                              'Warlock': 'A wielder of magic that is derived from a bargain with an extraplanar entity',
                              'Wizard': 'A scholarly magic-user capable of manipulating the structures of reality'},
                  'Alignment': {'Chaotic Evil': 'creatures are motivated by arbitrary and often malicious whims.\n'
                            'They are typically greedy and selfish, and are often violent.\n'
                            'They give no thought to the wants or needs of other creatures, and pay no heed to rules or expectations.\n'
                            'Such creatures will typically only bow to authority when threatened.',
                                 'Chaotic Good': 'Chaotic Good creatures do what they believe to be right with little regard for the opinions of others.\n'
                            ' They are guided by their own sense of good and evil rather than the prevailing opinions of society,\n'
                            'and they do not feel bound by rules, laws, or other creatures’ expectations of behavior.',
                                 'Chaotic Neutral': 'Chaotic Neutral creatures follow their whims, valuing their own freedom and self-interest above other concerns.\n'
                               ' Such creatures dislike being ordered to do things, and pay no regard for rules or other creatures’ expectations.\n'
                               ' And, while they are not always selfish to the point of harming others, they feel no compulsion to help other creatures in need.',
                                 'Lawful Evil': 'Lawful Evil creatures act within a code of behavior, but are otherwise self-centered.\n'
                           'They are often tyrants, or would be if they could, seeking to use their code of behavior to advance their own interests.',
                                 'Lawful Good': 'Lawful Good creatures act how a “good person” is expected to act.\n'
                           'They follow rules, respect legitimate authority, and treat others with kindness, honor, and respect.',
                                 'Lawful Neutral': 'Lawful Neutral act in accordance with the law, tradition, or with some code of behavior.\n'
                              'While this code can often be external (the law, a religious tradition, etc.), it can also be self-determined.',
                                 'Neutral Evil': 'Neutral Evil creatures are self-interested, and do whatever they can get away with to advance their own interests. \n'
                            'They might follow rules if it serves them, but they do not feel bound to do so. At the same time, they aren’t so unpredictable as Chaotic Evil creatures.',
                                 'Neutral Good': 'Neutral Good creatures do their best to do what they consider “good”, but don’t cling to rules or stricture so much as Lawful Good creatures.\n'
                            'A Neutral Good creature might still obey the law or society’s expectations most of the time,\n'
                            'but they are not rigidly bound by them, and they view doing the right thing as more valuable than obeying some strict doctrine.',
                                 'True Neutral': 'True Neutral creatures do what seems like the best option in any given situation.\n'
                            'These creatures might lack strong moral convictions, they might be indecisive, or they might simply be unopinionated.\n'
                            'Such creatures typically act based upon their momentary needs and desires rather than based on a moral philosophy.',
                                }
                  }

class_index_dic = {0: 'Barbarian',
                   1: 'Bard',
                   2: 'Cleric',
                   3: 'Druid',
                   4: 'Fighter',
                   5: 'Monk',
                   6: 'Paladin',
                   7: 'Ranger',
                   8: 'Rogue',
                   9: 'Sorcerer',
                   10: 'Warlock',
                   11: 'Wizard'
                   }
alignment_index_dic = {0: 'Chaotic Evil',
                        1: 'Chaotic Good',
                        2: 'Chaotic Neutral',
                        3: 'Lawful Evil',
                        4: 'Lawful Good',
                        5: 'Lawful Neutral',
                        6: 'Neutral Evil',
                        7: 'Neutral Good',
                        8: 'True Neutral'
                       }

def character_creator():

    for i in range(0, 12):
        char_class = class_index_dic[i]
        class_def = character_dic['Classes'][char_class]
        print(i, "== ",  char_class, ":", class_def)


if __name__ == '__main__':
    character_creator()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
