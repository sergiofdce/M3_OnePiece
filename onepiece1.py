dict_characters = { 1 : {"name" : "Luffy","category": 1, "weapons": [1, 1],"strength" : 6, "speed" :
7,"experience": 0},
 2 : {"name" : "Zoro","category": 1, "weapons" : [4],"strength" : 5, "speed" : 6,"experience":
0},
 3 : {"name" : "Sanji", "category" : 1, "weapons" : [1,3],"strength" : 4, "speed" :
6,"experience": 0 },
 4 : {"name" : "Buggy", "category" : 2, "weapons" : [3], "strength" : 2, "speed" : 4,
"experience" : 0},
 5 : {"name" : "Mr3", "category" : 2, "weapons" : [5], "strength" : 3, "speed" : 2, "experience"
: 0},
 6 : {"name" : "Xebec", "category" : 3, "weapons" : [1,3], "strength" : 6, "speed" : 5,
"experience" : 0},
 7 : {"name" : "Kaido", "category" : 3, "weapons" : [4], "strength" : 8, "speed" : 3,
"experience" : 0},
 8 : {"name" : "Mama grande", "category" : 3, "weapons" : [5], "strength" : 7, "speed" : 1,
"experience" : 0},
 9 : {"name" : "Akainu", "category" : 4, "weapons" : [2], "strength" : 6, "speed" : 4,
"experience" : 0},
 10 : {"name" : "Kizaru", "category" : 4, "weapons" : [1,3], "strength" : 5, "speed" : 8,
"experience" : 0},
 11 : {"name" : "Fujitora", "category" : 4, "weapons" : [5], "strength" : 5, "speed" : 4,
"experience" : 0},
 12 : {"name" : "Garp", "category" : 5, "weapons" : [2], "strength" : 6, "speed" : 3,
"experience" : 0},
 13 : {"name" : "Smoker", "category" : 5, "weapons" : [5], "strength" : 5, "speed" : 5,
"experience" : 0},
 14 : {"name" : "Koby", "category" : 6, "weapons" : [4], "strength" : 3, "speed" : 4,
"experience" : 0},
 15 : {"name" : "Tashigi", "category" : 6, "weapons" : [3], "strength" : 4, "speed" : 4,
"experience" : 0},
 }

dict_weapons = { 1 : {"name" : "Sword","strength": 3,"speed": 5,"two_hand":False},
 2 : {"name" : "Greatsword","strength": 5,"speed": 3,"two_hand":True},
 3 : {"name" : "Gun","strength": 2,"speed": 6,"two_hand":False},
 4: {"name": "Rifle", "strength": 3, "speed": 4,"two_hand":True},
 5: {"name": "Chuchi", "strength": 4, "speed": 4,"two_hand":True},
 }

dict_crews = { 1 : {"name" : "Straw hat","members": [8,6]},
 2 : {"name" : "Pirates Buggy","members": [1,3,5]},
 3: {"name": "Pirates Rocks","members": [2,4,7,]}
 }

dict_ranks = { 1 : {"name" : "Admiral","members": [9,10,11]},
 2 : {"name" : "ViceAdmiral","members": [12,13]},
 3: {"name": "Lieutenant","members": [14,15]}
 }

dict_categorys = {1:"Straw hat",2:"Pirates Buggy",3:"Pirates Rocks",4:"Admiral",5:"ViceAdmiral",6:"Lieutenant"}

# Flags menu
flg_menu_00 = True
flg_menu_02 = False
flg_menu_03 = False
flg_menu_04 = False

flg_menu_021 = False
flg_menu_022 = False

flg_menu_031 = False
flg_menu_032 = False

flg_menu_041 = False
flg_menu_042 = False
flg_menu_043 = False
flg_menu_044 = False

exit = False

while exit==False:
    while flg_menu_00:
        menu_00 = "Menu 0 (One Piece)".center(40, "=") + "\n1)Play\n2)Create\n3)Edit\n4)List\n5)Exit\n"
        print(menu_00)
        opc=input("->Option: ")
        while not opc.isdigit() or int(opc) not in (1,2,3,4,5):
            print("Invalid Option".center(40,"="))
            input("Press enter to continue\n")
            print(menu_00)
            opc = input("->Option: ")
        else:
            opc=int(opc)
            if opc==1:
                print("PLAY MODE UNDER CONSTRUCTION".center(40,"-"))
                input("Press enter to return\n")

            elif opc==2:
                flg_menu_02 = True
                flg_menu_00 = False
            elif opc==3:
                flg_menu_03 = True
                flg_menu_00 = False
            elif opc==4:
                flg_menu_04 = True
                flg_menu_00 = False
            else:
                print("Closing program...")
                flg_menu_00 = False
                exit = True

    while flg_menu_02:
        menu_02 = "Menu 02 Create".center(40, "=") + "\n1)Create Character\n2)Create Weapon\n3)Go Back\n"
        print(menu_02)
        opc = input("->Option: ")
        while not opc.isdigit() or int(opc) not in (1, 2, 3):
            print("Invalid Option".center(40, "="))
            input("Press enter to continue\n")
            print(menu_02)
            opc = input("->Option: ")
        else:
            opc = int(opc)

            if opc==1:
                flg_menu_021 = True
                flg_menu_02 = False
            elif opc==2:
                flg_menu_022 = True
                flg_menu_02 = False
            elif opc==3:
                flg_menu_00 = True
                flg_menu_02 = False

    while flg_menu_021:
        menu_021= "Menu 02 New Character".center(40, "=")+"\n"
        print(menu_021)

#--------PICK NAME
        new_ch_name=input("Name of the new character: ")

#--------PICK SIDE
        print("Side of the new character:\n1)Marine\n2)Pirates\n")
        new_ch_side=input("->Option: ")
        while not new_ch_side.isdigit() or int(new_ch_side) not in (1, 2):
            print("Invalid Option".center(40, "="))
            input("Press enter to continue\n")
            print("Side of the new character:\n1)Marine\n2)Pirates\n")
            new_ch_side=input("->Option: ")
        else:
            new_ch_side=int(new_ch_side)

#--------PICK RANGE: MARINE
        if new_ch_side==1:
            print("Range or crew of the new character:\n1) Admiral\n2) ViceAdmiral\n3) lieutenant\n")
            new_ch_range= input("->Option: ")
            while not new_ch_range.isdigit() or int(new_ch_range) not in (1, 2, 3):
                print("Invalid Option".center(40, "="))
                input("Press enter to continue\n")
                print("Range or crew of the new character:\n1) Admiral\n2) ViceAdmiral\n3) lieutenant\n")
                new_ch_range = input("->Option: ")
            else:
                new_ch_range = int(new_ch_range)
                #se guarda

#---------PICK CREW: PIRATES
        elif new_ch_side==2:
            print("Range or crew of the new character:\n1) Straw hat\n2) Pirates Buggy\n3) Pirates Rocks\n\
            4) The Alvida Pirates\n5) The Fake Straw\n")
            new_ch_crew = input("->Option: ")
            while not new_ch_crew .isdigit() or int(new_ch_crew ) not in (1, 2, 3):
                print("Invalid Option".center(40, "="))
                input("Press enter to continue\n")
                print("Range or crew of the new character:\n1) Admiral\n2) ViceAdmiral\n3) Lieutenant\n")
                new_ch_crew  = input("->Option: ")
            else:
                new_ch_crew  = int(new_ch_crew)
                # se guarda

#---------PICK WEAPONS
        new_ch_weapons = []
        pick_weapons = True
        while pick_weapons:
            print("Available Weapons".center(40, "="))
            for i in range(1,len(dict_weapons)+1):
                print(f"{i}) {dict_weapons[i]['name']}, Strenght: {dict_weapons[i]['strength']}, Speed: {dict_weapons[i]['speed']}")
            print()
            print("Character Weapons".center(40, "="))
            if new_ch_weapons==[]:
                print("None".center(40, "-"))
            else:
                for i in range(1, len(new_ch_weapons) + 1):
                    print(i)
                    print(f"{dict_weapons[new_ch_weapons[i]]}, {dict_weapons[new_ch_weapons[i]]['name']}, Strenght: {dict_weapons[new_ch_weapons[i]]['strength']}, Speed: {dict_weapons[new_ch_weapons[i]]['speed']}")

            new_ch_weapons=input("ELIGE ARMA:")
            print(new_ch_weapons)
            input("seguir")












    while flg_menu_03:
        menu_03 = "Menu 03 (Edit Menu)".center(40, "=") + "\n1)Edit character\n2)Edit weapon\n3)Go back\n"
        print(menu_03)
        opc = input("->Option: ")
        while not opc.isdigit() or int(opc) not in (1,2,3):
            print("Invalid Option".center(40,"="))
            input("Press enter to continue\n")
            print(menu_03)
            opc = input("->Option: ")
        else:
            opc=int(opc)
            if opc==1:
                # sergio
                print("Menu 031 (Select character to Edit)").center(40, "=")


            elif opc==2:
                # sergio
                print("Edit weapon")


            else:
                flg_menu_03 = False
                flg_menu_00 = True
    while flg_menu_04:
        menu_04 = "Menu 04 (List)".center(40, "=") + "\n1)List characters\n2)List weapons\n3)List side\n4)List range\n5)Go back"
        print(menu_04)
        opc = input("->Option: ")
        while not opc.isdigit() or int(opc) not in (1, 2, 3, 4, 5):
            print("Invalid Option".center(40, "="))
            input("Press enter to continue\n")
            print(menu_04)
            opc = input("->Option: ")
        else:
            opc=int(opc)
            if opc==1:
                print("List characters")
            elif opc==2:
                print("List weapons")
            elif opc==3:
                print("List side")
            elif opc==4:
                print("List range")
            else:
                # Exit
                flg_menu_04 = False
                flg_menu_00 = True

