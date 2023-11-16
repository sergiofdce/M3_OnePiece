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
        new_ch_name=input("Name of the new character: ")

        print("Side of the new character:\n1)Marine\n2)Pirates\n")
        new_ch_side=input("->Option: ")
        while not new_ch_side.isdigit() or int(new_ch_side) not in (1, 2, 3):
            print("Invalid Option".center(40, "="))
            input("Press enter to continue\n")
            print("Side of the new character:\n1)Marine\n2)Pirates\n")
            new_ch_side=input("->Option: ")

        if new_ch_side==1:
            print("Range or crew of the new character:\n1) Admiral\n2) ViceAdmiral\n3) lieutenant\n")

        elif new_ch_name==2:
            print("Range or crew of the new character:\n1) Straw hat\n2) Pirates Buggy\n3) Pirates Rocks\n\
            4) The Alvida Pirates\n5) The Fake Straw\n")







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
                print("Menu 031 (Select character to Edit)".center(40, "="))
                for clave in dict_characters:
                    if len(dict_characters[clave]['weapons']) == 1:
                        print(f"ID: {clave}, Name: {dict_characters[clave]['name']}, Weapons: {dict_weapons[dict_characters[clave]['weapons'][0]]['name']}"
                            f", Strenght: {dict_characters[clave]['strength'] + dict_weapons[dict_characters[clave]['weapons'][0]]['strength']}"
                            f", Speed: {dict_characters[clave]['speed'] + dict_weapons[dict_characters[clave]['weapons'][0]]['speed']}"
                            f", Experience: {dict_characters[clave]['experience']}")
                    else:
                        print(f"ID: {clave}, Name: {dict_characters[clave]['name']}, Weapons: {dict_weapons[dict_characters[clave]['weapons'][0]]['name']}, {dict_weapons[dict_characters[clave]['weapons'][1]]['name']}"
                            f", Strenght: {dict_characters[clave]['strength'] + dict_weapons[dict_characters[clave]['weapons'][0]]['strength'] + dict_weapons[dict_characters[clave]['weapons'][1]]['strength']}"
                            f", Speed: {dict_characters[clave]['speed'] + dict_weapons[dict_characters[clave]['weapons'][0]]['speed'] + dict_weapons[dict_characters[clave]['weapons'][0]]['speed']}"
                            f", Experience: {dict_characters[clave]['experience']}")
                id_value = input("ID to edit: ")
                while not id_value.isdigit() or int(id_value) not in range(1,len(dict_characters)+1):
                    print("Invalid Option".center(40, "="))
                    input("Press enter to continue\n")
                    id_value = input("ID to edit: ")
                else:
                    print(f"Select feature to edit to character ID: {id_value}, Name: {dict_characters[int(id_value)]['name']}\n"
                          f"1)Name\n2)Weapon\n3)Go back")
                    opc = input("->Option: ")
                    while not opc.isdigit() or int(opc) not in (1, 2, 3):
                        print("Invalid Option".center(40, "="))
                        input("Press enter to continue\n")
                        opc = input("->Option: ")
                    else:
                        opc = int(opc)
                        if opc==1:
                            value = input("Enter the new name: ")
                            confirm = input(f"Do you want to change name {dict_characters[int(id_value)]['name']} by {value}? Y/N: ")
                            confirm = confirm.upper()
                            while not confirm in ("Y","N"):
                                print("Invalid Option".center(40, "="))
                                input("Press enter to continue\n")
                                confirm = input(f"Do you want to change name {dict_characters[int(id_value)]['name']} by {value}? Y/N: ")
                                confirm = confirm.upper()
                            else:
                                if confirm == "Y":
                                    print(f"Name {dict_characters[int(id_value)]['name']} changed to {value}\n")
                                    dict_characters[int(id_value)]['name'] = value
                                else:
                                    print(f"Name {dict_characters[int(id_value)]['name']} didn't change\n")
                        elif opc==2:
                            print("Pendiente de Mar")
                        else:
                            flg_menu_03 = False
                            flg_menu_00 = True

            elif opc==2:
                # sergio
                print("Edit weapon")
                print("Menu 032 (Select Weapon to Edit)".center(40, "=") + "\n")
                for i in range(1, len(dict_weapons) + 1):
                    print(f"{i}) {dict_weapons[i]['name']}, Strenght: {dict_weapons[i]['strength']}, Speed: {dict_weapons[i]['speed']}")
                id_value = input("\nID weapon to edit: ")
                while not id_value.isdigit() or int(id_value) not in range(1, len(dict_weapons) + 1):
                    print("Invalid Option".center(40, "="))
                    input("Press enter to continue\n")
                    id_value = input("\nID weapon to edit: ")
                else:
                    print("\n" + "Menu 032X (Weapon feature to Edit)".center(40, "=") + "\n" +
                    "1)Name\n2)Plus Strength\n3)Plus speed\n4)Go back\n")

                    opc = input(f"Select feature to edit to weapon ID: {id_value}, Name: {dict_weapons[int(id_value)]['name']}\n"
                                f"->Option: ")
                    while not opc.isdigit() or int(opc) not in (1, 2, 3, 4):
                        print("Invalid Option".center(40, "="))
                        input("Press enter to continue\n")
                        opc = input("\n->Option: ")
                    else:
                        opc = int(opc)
                        if opc == 1:
                            value = input("Enter the new name: ")
                            confirm = input(f"Do you want to change name {dict_weapons[int(id_value)]['name']} by {value}? Y/N: ")
                            confirm = confirm.upper()
                            while not confirm in ("Y", "N"):
                                print("Invalid Option".center(40, "="))
                                input("Press enter to continue\n")
                                confirm = input(f"Do you want to change name {dict_weapons[int(id_value)]['name']} by {value}? Y/N: ")
                                confirm = confirm.upper()
                            else:
                                if confirm == "Y":
                                    print(f"Name {dict_weapons[int(id_value)]['name']} changed to {value}\n")
                                    dict_weapons[int(id_value)]['name'] = value
                                else:
                                    print(f"Name {dict_weapons[int(id_value)]['name']} didn't change\n")

                        elif opc == 2:
                            value = input("Enter the new Strength: ")
                            value = int(value)
                            while value not in range (1,10):
                                print("Invalid Option".center(40, "="))
                                input("Press enter to continue\n")
                                value = input("Enter the new Strength: ")
                                value = int(value)
                            confirm = input(f"Do you want to change Strength from {dict_weapons[int(id_value)]['strength']} to {value} in the weapon {dict_weapons[int(id_value)]['name']}? Y/N: ")
                            confirm = confirm.upper()
                            while not confirm in ("Y", "N"):
                                print("Invalid Option".center(40, "="))
                                input("Press enter to continue\n")
                                confirm = input(f"Do you want to change Strength from {dict_weapons[int(id_value)]['strength']} to {value} in the weapon {dict_weapons[int(id_value)]['name']}? Y/N")
                                confirm = confirm.upper()
                            else:
                                if confirm == "Y":
                                    print(f"Strength on {dict_weapons[int(id_value)]['name']} changed from {dict_weapons[int(id_value)]['strength']} to {value}\n")
                                    dict_weapons[int(id_value)]['strength'] = int(value)
                                else:
                                    print(f"Strength on {dict_weapons[int(id_value)]['name']} didn't change\n")

                        elif opc == 3:
                            value = input("Enter the new Speed: ")
                            value = int(value)
                            while value not in range(1, 10):
                                print("Invalid Option".center(40, "="))
                                input("Press enter to continue\n")
                                value = input("Enter the new Speed: ")
                                value = int(value)
                            confirm = input(f"Do you want to change Speed from {dict_weapons[int(id_value)]['speed']} to {value} in the weapon {dict_weapons[int(id_value)]['name']}? Y/N: ")
                            confirm = confirm.upper()
                            while not confirm in ("Y", "N"):
                                print("Invalid Option".center(40, "="))
                                input("Press enter to continue\n")
                                confirm = input(f"Do you want to change Speed from {dict_weapons[int(id_value)]['speed']} to {value} in the weapon {dict_weapons[int(id_value)]['name']}? Y/N")
                                confirm = confirm.upper()
                            else:
                                if confirm == "Y":
                                    print(f"Speed on {dict_weapons[int(id_value)]['name']} changed from {dict_weapons[int(id_value)]['speed']} to {value}\n")
                                    dict_weapons[int(id_value)]['speed'] = int(value)
                                else:
                                    print(f"Strength on {dict_weapons[int(id_value)]['name']} didn't change\n")
                        else:
                            flg_menu_03 = False
                            flg_menu_00 = True




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

