import random

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
 3: {"name": "Pirates Rocks","members": [2,4,7]}
 }

dict_ranks = { 1 : {"name" : "Admiral","members": [9,10,11]},
 2 : {"name" : "ViceAdmiral","members": [12,13]},
 3: {"name": "Lieutenant","members": [14,15]}
 }

dict_categorys = {1:"Straw hat",2:"Pirates Buggy",3:"Pirates Rocks",4:"The Alvida Pirates",5:"The Fake Straw",6:"Admiral",7:"ViceAdmiral",8:"Lieutenant"}

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

            if opc == 1:
                flg_menu_021 = True
                flg_menu_02 = False
            elif opc == 2:
                flg_menu_022 = True
                flg_menu_02 = False
            elif opc == 3:
                flg_menu_00 = True
                flg_menu_02 = False

# \\\\\\\\\\\\\\MENU 021 CREATE CHARACTER
    while flg_menu_021:
        menu_021 = "Menu 021 New Character".center(40, "=") + "\n"
        print(menu_021)

# --------PICK NAME
        new_ch_name = input("Name of the new character: ")

# --------PICK SIDE
        print("Side of the new character:\n1)Marine\n2)Pirates\n")
        new_ch_side = input("->Option: ")
        while not new_ch_side.isdigit() or int(new_ch_side) not in (1, 2):
            print("Invalid Option".center(40, "="))
            input("Press enter to continue\n")
            print("Side of the new character:\n1)Marine\n2)Pirates\n")
            new_ch_side = input("->Option: ")
        else:
            new_ch_side = int(new_ch_side)

# --------PICK RANGE: MARINE
        if new_ch_side == 1:
            print("Range of the new character:\n1) Admiral\n2) ViceAdmiral\n3) Lieutenant\n")
            new_ch_category = input("->Option: ")
            while not new_ch_category.isdigit() or int(new_ch_category) not in (1, 2, 3):
                print("Invalid Option".center(40, "="))
                input("Press enter to continue\n")
                print("Range of the new character:\n1) Admiral\n2) ViceAdmiral\n3) Lieutenant\n")
                new_ch_category = input("->Option: ")
            else:
                new_ch_category = int(new_ch_category)
                if new_ch_category == 1:
                    new_ch_category = 6
                elif new_ch_category == 2:
                    new_ch_category = 7
                elif new_ch_category == 3:
                    new_ch_category = 8

# ---------PICK CREW: PIRATES
        elif new_ch_side == 2:
            print(
                "Crew of the new character:\n1) Straw hat\n2) Pirates Buggy\n3) Pirates Rocks\n4) The Alvida Pirates\n5) The Fake Straw\n")
            new_ch_category = input("->Option: ")
            while not new_ch_category.isdigit() or int(new_ch_category) not in (1, 2, 3, 4, 5):
                print("Invalid Option".center(40, "="))
                input("Press enter to continue\n")
                print(
                    "Crew of the new character:\n1) Straw hat\n2) Pirates Buggy\n3) Pirates Rocks\n\4) The Alvida Pirates\n5) The Fake Straw\n")
                new_ch_category = input("->Option: ")
            else:
                new_ch_category = int(new_ch_category)
                # se guarda

# ---------PICK WEAPONS
        new_ch_weapons = []

        pick_weapons = True
        while pick_weapons:

            # AVAILABLE WEAPONS:
            print("Available Weapons".center(40, "="))
            if (len(new_ch_weapons)) == 2:
                print("None".center(40, "-") + "\n")
            elif (len(new_ch_weapons) > 0 and dict_weapons[new_ch_weapons[0]]["two_hand"] == True):
                print("None".center(40, "-") + "\n")
            else:
                for i in range(1, len(dict_weapons) + 1):
                    if len(new_ch_weapons) > 0 and dict_weapons[i]['two_hand'] == True:
                        continue
                    else:
                        print(
                            f"{i}) {dict_weapons[i]['name']}, Strength: {dict_weapons[i]['strength']}, Speed: {dict_weapons[i]['speed']}")
                print()

            # CHARACTER WEAPONS:
            print("Character Weapons".center(40, "="))
            if new_ch_weapons == []:
                print("None".center(40, "-") + "\n")
            else:
                for clave in new_ch_weapons:
                    if clave in dict_weapons:
                        print(
                            f"{clave}) {dict_weapons[clave]['name']}, Strength: {dict_weapons[clave]['strength']}, Speed: {dict_weapons[clave]['speed']}")
                print()

            # ELEGIR OPCION:
            select_weapon = input(
                "Add Weapons:\nWeapon Id) To add weapon ID\n0) Finish add weapons\n-Weapon Id) Delete Weapon Id\n->Option: ")
            num_negativo = False
            if select_weapon.startswith("-"):
                select_weapon = select_weapon[1:]
                num_negativo = True
                # print(select_weapon)
            while not select_weapon.isdigit() or int(select_weapon) > len(dict_weapons):
                print("Invalid Option".center(40, "="))
                select_weapon = input(
                    "Add Weapons:\nWeapon Id) To add weapon ID\n0) Finish add weapons\n-Weapon Id) Delete Weapon Id\n->Option: ")
                num_negativo = False
                if select_weapon.startswith("-"):
                    select_weapon = select_weapon[1:]
                    num_negativo = True

            # AÑADIR:
            if num_negativo == False and int(select_weapon) > 0:
                # si no hay armas inventario, entra
                if new_ch_weapons == []:
                    new_ch_weapons.append(int(select_weapon))
                # si tenemos 1 arma inventario, y la que intentamos meter es doble mano, no entra
                elif len(new_ch_weapons) > 1 or (
                        len(new_ch_weapons) > 0 and dict_weapons[int(select_weapon)]["two_hand"] == True):
                    print("Invalid Option".center(40, "="))
                # si tenemos 1 arma inventario, y la que intentamos meter NO es doble mano, entra
                elif (len(new_ch_weapons) == 1 and dict_weapons[new_ch_weapons[0]]["two_hand"] == False):
                    new_ch_weapons.append(int(select_weapon))
                # si tenemos 1 arma en el inventario de doble mano, no entra nada más
                elif len(new_ch_weapons) == 2 or dict_weapons[new_ch_weapons[0]]["two_hand"] == True:
                    print("Invalid Option".center(40, "="))

                # print("se añade")
                # print("resultado", new_ch_weapons)


            # QUITAR:
            elif num_negativo == True and int(select_weapon) > 0:
                new_ch_weapons.remove(int(select_weapon))
                # print("se quita")
                # print("resultado", new_ch_weapons)


            # GUARDAR:
            elif int(select_weapon) == 0:
                # lock list
                # print("salir")
                pick_weapons = False

            # print("MIS WEAPONS SON", new_ch_weapons)
            # input("seguir")

        new_ch_strength = random.randint(1, 9)
        new_ch_speed = random.randint(1, 9)
        new_ch_experience = 0

# ----------SAVE CHARACTER
        print()
        if len(new_ch_weapons) == 0:
            print(
                f"The new player will be:\nName: {new_ch_name}\nCategory: {dict_categorys[new_ch_category]}\nWeapons: \nStrength: {new_ch_strength}\nSpeed: {new_ch_speed}\nExperience: {new_ch_experience}")
        elif len(new_ch_weapons) < 2:
            print(
                f"The new player will be:\nName: {new_ch_name}\nCategory: {dict_categorys[new_ch_category]}\nWeapons: {dict_weapons[new_ch_weapons[0]]['name']}\nStrength: {new_ch_strength}\nSpeed: {new_ch_speed}\nExperience: {new_ch_experience}")
        elif len(new_ch_weapons) == 2:
            print(
                f"The new player will be:\nName: {new_ch_name}\nCategory: {dict_categorys[new_ch_category]}\nWeapons: {dict_weapons[new_ch_weapons[0]]['name']}, {dict_weapons[new_ch_weapons[1]]['name']}\nStrength: {new_ch_strength}\nSpeed: {new_ch_speed}\nExperience: {new_ch_experience}")

        siono = input("Save this player? S/N ")
        siono = siono.upper()
        while not siono.isalpha() or not siono in ("S", "N"):
            print("Invalid Option".center(40, "="))
            siono = input("Save this player? S/N ")
            siono = siono.upper()

        if siono == ("S"):
            numerolista = len(dict_characters) + 1
            dict_characters[numerolista] = {"name": new_ch_name, "category": new_ch_category,
                                            "weapons": new_ch_weapons, "strength": new_ch_strength,
                                            "speed": new_ch_speed, "experience": new_ch_experience}
            # print(dict_characters)
            print("Player saved")
        elif siono == ("N"):
            print("Player discarded")

        input("Press Enter to return to menu")
        flg_menu_00 = True
        flg_menu_021 = False

# \\\\\\\\\\\\\\MENU 021 CREATE WEAPON
    while flg_menu_022:
        menu_022 = "Menu 022 New Weapon".center(40, "=") + "\n"
        print(menu_022)

# --------PICK NAME
        new_weapon_name = input("Name of the new weapon: ")

# --------PICK STRENGTH
        new_weapon_strength = input("Weapon Strength 1-9:\n->Strength: ")
        while not new_weapon_strength.isdigit() or int(new_weapon_strength) not in range(1, 10):
            print("Invalid Option".center(40, "="))
            input("Press enter to continue\n")
            new_weapon_strength = input("Weapon Strength 1-9:\n->Strength: ")
        else:
            new_weapon_strength = int(new_weapon_strength)

# --------PICK SPEED
        new_weapon_speed = input("Weapon Speed 1-9:\n->Speed: ")
        while not new_weapon_speed.isdigit() or int(new_weapon_speed) not in range(1, 10):
            print("Invalid Option".center(40, "="))
            input("Press enter to continue\n")
            new_weapon_speed = input("Weapon Speed 1-9:\n->Speed: ")
        else:
            new_weapon_speed = int(new_weapon_speed)

# --------PICK KIND OF WEAPON
        new_weapon_kind = input("Kind of Weapon:\n1)One Hand\n2)Two Hands\n->Option: ")
        while not new_weapon_kind.isdigit() or int(new_weapon_kind) not in (1, 2):
            print("Invalid Option".center(40, "="))
            input("Press enter to continue\n")
            new_weapon_kind = input("Kind of Weapon:\n1)One Hand\n2)Two Hands\n->Option: ")
        else:
            new_weapon_kind = int(new_weapon_kind)

            if new_weapon_kind == 1:
                new_weapon_kind = False
            elif new_weapon_kind == 2:
                new_weapon_kind = True

# ------------SAVE WEAPON
        print(
            f"The new weapon will be:\nName: {new_weapon_name}\nStrength: {new_weapon_strength}\nSpeed: {new_weapon_speed}\nTwo hands type: {new_weapon_kind}\n")

        siono = input("Save this weapon? S/N ")
        siono = siono.upper()
        while not siono.isalpha() or not siono in ("S", "N"):
            print("Invalid Option".center(40, "="))
            siono = input("Save this weapon? S/N ")
            siono = siono.upper()

        if siono == ("S"):
            numerolista = len(dict_weapons) + 1
            dict_weapons[numerolista] = {"name": new_weapon_name, "strength": new_weapon_strength,
                                         "speed": new_weapon_speed, "two_hand": new_weapon_kind}
            # print(dict_weapons)
            print("Weapon saved")
        elif siono == ("N"):
            print("Weapon discarded")

        input("Press Enter to return to menu")
        flg_menu_00 = True
        flg_menu_022 = False







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
                # print(dict_characters)
                for clave in dict_characters:
                    if len(dict_characters[clave]['weapons']) == 0:
                        print(f"ID: {clave}, Name: {dict_characters[clave]['name']}, Weapons: 0"
                            f", Strenght: {dict_characters[clave]['strength']}"
                            f", Speed: {dict_characters[clave]['speed']}"
                            f", Experience: {dict_characters[clave]['experience']}")

                    elif len(dict_characters[clave]['weapons']) == 1:
                        print(f"ID: {clave}, Name: {dict_characters[clave]['name']}, Weapons: {dict_weapons[dict_characters[clave]['weapons'][0]]['name']}"
                            f", Strenght: {dict_characters[clave]['strength'] + dict_weapons[dict_characters[clave]['weapons'][0]]['strength']}"
                            f", Speed: {dict_characters[clave]['speed'] + dict_weapons[dict_characters[clave]['weapons'][0]]['speed']}"
                            f", Experience: {dict_characters[clave]['experience']}")
                    elif len(dict_characters[clave]['weapons']) == 2:
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
                            new_ch_weapons = dict_characters[int(id_value)]["weapons"]

                            pick_weapons = True
                            while pick_weapons:

                                # AVAILABLE WEAPONS:
                                print("Available Weapons".center(40, "="))
                                if (len(new_ch_weapons)) == 2:
                                    print("None".center(40, "-") + "\n")
                                elif (len(new_ch_weapons) > 0 and dict_weapons[new_ch_weapons[0]]["two_hand"] == True):
                                    print("None".center(40, "-") + "\n")
                                else:
                                    for i in range(1, len(dict_weapons) + 1):
                                        if len(new_ch_weapons) > 0 and dict_weapons[i]['two_hand'] == True:
                                            continue
                                        else:
                                            print(f"{i}) {dict_weapons[i]['name']}, Strength: {dict_weapons[i]['strength']}, Speed: {dict_weapons[i]['speed']}")
                                    print()

                                # CHARACTER WEAPONS:
                                print("Character Weapons".center(40, "="))
                                if new_ch_weapons == []:
                                    print("None".center(40, "-") + "\n")
                                else:
                                    for clave in new_ch_weapons:
                                        if clave in dict_weapons:
                                            print(f"{clave}) {dict_weapons[clave]['name']}, Strength: {dict_weapons[clave]['strength']}, Speed: {dict_weapons[clave]['speed']}")
                                    print()

                                # ELEGIR OPCION:
                                select_weapon = input("Add Weapons:\nWeapon Id) To add weapon ID\n0) Finish add weapons\n-Weapon Id) Delete Weapon Id\n->Option: ")
                                num_negativo = False
                                if select_weapon.startswith("-"):
                                    select_weapon = select_weapon[1:]
                                    num_negativo = True
                                    # print(select_weapon)
                                while not select_weapon.isdigit() or int(select_weapon) > len(dict_weapons):
                                    print("Invalid Option".center(40, "="))
                                    select_weapon = input(
                                        "Add Weapons:\nWeapon Id) To add weapon ID\n0) Finish add weapons\n-Weapon Id) Delete Weapon Id\n->Option: ")
                                    num_negativo = False
                                    if select_weapon.startswith("-"):
                                        select_weapon = select_weapon[1:]
                                        num_negativo = True

                                # AÑADIR:
                                if num_negativo == False and int(select_weapon) > 0:
                                    # si no hay armas inventario, entra
                                    if new_ch_weapons == []:
                                        new_ch_weapons.append(int(select_weapon))
                                    # si tenemos 1 arma inventario, y la que intentamos meter es doble mano, no entra
                                    elif len(new_ch_weapons) > 1 or (
                                            len(new_ch_weapons) > 0 and dict_weapons[int(select_weapon)][
                                        "two_hand"] == True):
                                        print("Invalid Option".center(40, "="))
                                    # si tenemos 1 arma inventario, y la que intentamos meter NO es doble mano, entra
                                    elif (len(new_ch_weapons) == 1 and dict_weapons[new_ch_weapons[0]][
                                        "two_hand"] == False):
                                        new_ch_weapons.append(int(select_weapon))
                                    # si tenemos 1 arma en el inventario de doble mano, no entra nada más
                                    elif len(new_ch_weapons) == 2 or dict_weapons[new_ch_weapons[0]][
                                        "two_hand"] == True:
                                        print("Invalid Option".center(40, "="))

                                    # print("se añade")
                                    # print("resultado", new_ch_weapons)


                                # QUITAR:
                                elif num_negativo == True and int(select_weapon) > 0:
                                    new_ch_weapons.remove(int(select_weapon))
                                    # print("se quita")
                                    # print("resultado", new_ch_weapons)


                                # GUARDAR:
                                elif int(select_weapon) == 0:
                                    # lock list
                                    # print("salir")
                                    pick_weapons = False

                                # print("MIS WEAPONS SON", new_ch_weapons)
                                # input("seguir")

                            new_ch_strength = random.randint(1, 9)
                            new_ch_speed = random.randint(1, 9)
                            new_ch_experience = 0




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
        menu_04 = "Menu 04 (List)".center(40,"=") + "\n1)List characters\n2)List weapons\n3)List side\n4)List range\n5)Go back"
        print(menu_04)
        opc = input("->Option: ")
        while not opc.isdigit() or int(opc) not in (1, 2, 3, 4, 5):
            print("Invalid Option".center(40, "="))
            input("Press enter to continue\n")
            print(menu_04)
            opc = input("->Option: ")
        else:
            opc = int(opc)
            if opc == 1:
                print("List characters")
                flg_menu_041 = True
                flg_menu_04 = False
            elif opc == 2:
                print("List weapons")
                flg_menu_042 = True
                flg_menu_04 = False
            elif opc == 3:
                print("List side")
                flg_menu_043 = True
                flg_menu_04 = False
            elif opc == 4:
                print("List range")
                flg_menu_044 = True
                flg_menu_04 = False
            else:
                # Exit
                flg_menu_04 = False
                flg_menu_00 = True

    while flg_menu_041:
        menu_041 = "Menu 042 (List Characters)".center(40,"=") + "\n1)List by ID\n2)List by name\n3)List by strength\n4)List by speed\n5)Go back"
        print(menu_041)
        opc = input("->Option: ")
        while not opc.isdigit() or int(opc) not in range (6):
            print("Invalid Option".center(40, "="))
            input("Press enter to continue\n")
            print(menu_04)
            opc = input("->Option: ")
        else:
            opc = int(opc)
# -----------LIST CHARACTERS BY ID
            if opc == 1:
                print("Characters ordered by ID".center(60, "=") + "\n" + "Id".ljust(10) + "Name".ljust(
                    17) + "Strength".rjust(8) + " " * 5 + "Speed".rjust(5) + " " * 5 + "Experience".ljust(
                    10) + "\n" + "*" * 60)

                for clave in dict_characters:
                    if len(dict_characters[clave]['weapons']) == 0:
                        print(f"{clave}".ljust(10)
                              + f"{dict_characters[clave]['name']}".ljust(17)
                              + f"{dict_characters[clave]['strength']}".rjust(8) + " "*5
                              + f"{dict_characters[clave]['speed']}".rjust(5) + " "*5
                              + str(dict_characters[clave]['experience']).ljust(10)
                              )

                    elif len(dict_characters[clave]['weapons']) == 1:
                        print(f"{clave}".ljust(10)
                              + f"{dict_characters[clave]['name']}".ljust(17)
                              + f"{dict_characters[clave]['strength'] + dict_weapons[dict_characters[clave]['weapons'][0]]['strength']}".rjust(8) + " "*5
                              + f"{dict_characters[clave]['speed'] + dict_weapons[dict_characters[clave]['weapons'][0]]['speed']}".rjust(5) + " "*5
                              + str(dict_characters[clave]['experience']).ljust(10)
                              )

                    elif len(dict_characters[clave]['weapons']) == 2:
                        print(f"{clave}".ljust(10)
                              + f"{dict_characters[clave]['name']}".ljust(17)
                              + f"{dict_characters[clave]['strength'] + dict_weapons[dict_characters[clave]['weapons'][0]]['strength'] + + dict_weapons[dict_characters[clave]['weapons'][1]]['strength']}".rjust(8) + " " * 5
                              + f"{dict_characters[clave]['speed'] + dict_weapons[dict_characters[clave]['weapons'][0]]['speed'] + dict_weapons[dict_characters[clave]['weapons'][1]]['speed']}".rjust(5) + " " * 5
                              + str(dict_characters[clave]['experience']).ljust(10)
                              )

# -----------LIST CHARACTERS BY NAME
            elif opc == 2:
                print("Characters ordered by Name".center(60, "=") + "\n" + "Id".ljust(10) + "Name".ljust(17) + "Strength".rjust(8) + " " * 5 + "Speed".rjust(5) + " " * 5 + "Experience".ljust(10) + "\n" + "*" * 60)

                claves_characters = list(dict_characters.keys())
                for pasada in range(len(claves_characters) - 1):
                    for j in range(len(claves_characters) - 1 - pasada):
                        if dict_characters[claves_characters[j]]["name"] > dict_characters[claves_characters[j + 1]]["name"]:
                            aux = claves_characters[j]
                            claves_characters[j] = claves_characters[j + 1]
                            claves_characters[j + 1] = aux

                for clave in claves_characters:
                    if len(dict_characters[clave]['weapons']) == 0:
                        print(f"{clave}".ljust(10)
                              + f"{dict_characters[clave]['name']}".ljust(17)
                              + f"{dict_characters[clave]['strength']}".rjust(8) + " "*5
                              + f"{dict_characters[clave]['speed']}".rjust(5) + " "*5
                              + str(dict_characters[clave]['experience']).ljust(10)
                              )

                    elif len(dict_characters[clave]['weapons']) == 1:
                        print(f"{clave}".ljust(10)
                              + f"{dict_characters[clave]['name']}".ljust(17)
                              + f"{dict_characters[clave]['strength'] + dict_weapons[dict_characters[clave]['weapons'][0]]['strength']}".rjust(8) + " "*5
                              + f"{dict_characters[clave]['speed'] + dict_weapons[dict_characters[clave]['weapons'][0]]['speed']}".rjust(5) + " "*5
                              + str(dict_characters[clave]['experience']).ljust(10)
                              )

                    elif len(dict_characters[clave]['weapons']) == 2:
                        print(f"{clave}".ljust(10)
                              + f"{dict_characters[clave]['name']}".ljust(17)
                              + f"{dict_characters[clave]['strength'] + dict_weapons[dict_characters[clave]['weapons'][0]]['strength'] + + dict_weapons[dict_characters[clave]['weapons'][1]]['strength']}".rjust(8) + " " * 5
                              + f"{dict_characters[clave]['speed'] + dict_weapons[dict_characters[clave]['weapons'][0]]['speed'] + dict_weapons[dict_characters[clave]['weapons'][1]]['speed']}".rjust(5) + " " * 5
                              + str(dict_characters[clave]['experience']).ljust(10)
                              )

# -----------LIST CHARACTERS BY STRENGTH
            elif opc == 3:
                print("Characters ordered by Strength".center(60, "=") + "\n" + "Id".ljust(10) + "Name".ljust(17) + "Strength".rjust(8) + " " * 5 + "Speed".rjust(5) + " " * 5 + "Experience".ljust(10) + "\n" + "*" * 60)
                claves_characters = list(dict_characters.keys())
                for pasada in range(len(claves_characters) - 1):
                    for j in range(len(claves_characters) - 1 - pasada):
                        # suma_p1 es la suma total de su pj
                        # print(f"personaje : {dict_characters[claves_characters[j]]['name']}")
                        suma_p1 = 0
                        claves_wp = list(dict_weapons.keys())
                        # Por longitud de mi lista de armas
                        for i in range(len(dict_characters[claves_characters[j]]['weapons'])):
                            # Comprobamos arma en diccionario de armas
                            for arma in range(len(dict_weapons)):
                                # print(f"id : {claves_wp[arma]}")
                                # print(f"nombre : {dict_weapons[claves_wp[arma]]['name']}")
                                if dict_characters[claves_characters[j]]['weapons'][i] == claves_wp[arma]:
                                    suma_p1 += dict_weapons[claves_wp[arma]]['strength']
                        suma_p1 += dict_characters[claves_characters[j]]['strength']
                        # print(f"suma daño : {suma_p1}")

                        # suma_p2 es la suma total de su pj
                        # print(f"personaje : {dict_characters[claves_characters[j+1]]['name']}")
                        suma_p2 = 0
                        claves_wp = list(dict_weapons.keys())
                        # Por longitud de mi lista de armas
                        for i in range(len(dict_characters[claves_characters[j+1]]['weapons'])):
                            # Comprobamos arma en diccionario de armas
                            for arma in range(len(dict_weapons)):
                                # print(f"id : {claves_wp[arma]}")
                                # print(f"nombre : {dict_weapons[claves_wp[arma]]['name']}")
                                if dict_characters[claves_characters[j+1]]['weapons'][i] == claves_wp[arma]:
                                    suma_p2 += dict_weapons[claves_wp[arma]]['strength']
                        suma_p2 += dict_characters[claves_characters[j+1]]['strength']
                        # print(f"suma daño : {suma_p2}")

                        if suma_p1 > suma_p2:
                            aux = claves_characters[j]
                            claves_characters[j] = claves_characters[j + 1]
                            claves_characters[j + 1] = aux


                for clave in claves_characters:
                    if len(dict_characters[clave]['weapons']) == 0:
                        print(f"{clave}".ljust(10)
                              + f"{dict_characters[clave]['name']}".ljust(17)
                              + f"{dict_characters[clave]['strength']}".rjust(8) + " "*5
                              + f"{dict_characters[clave]['speed']}".rjust(5) + " "*5
                              + str(dict_characters[clave]['experience']).ljust(10)
                              )

                    elif len(dict_characters[clave]['weapons']) == 1:
                        print(f"{clave}".ljust(10)
                              + f"{dict_characters[clave]['name']}".ljust(17)
                              + f"{dict_characters[clave]['strength'] + dict_weapons[dict_characters[clave]['weapons'][0]]['strength']}".rjust(8) + " "*5
                              + f"{dict_characters[clave]['speed'] + dict_weapons[dict_characters[clave]['weapons'][0]]['speed']}".rjust(5) + " "*5
                              + str(dict_characters[clave]['experience']).ljust(10)
                              )

                    elif len(dict_characters[clave]['weapons']) == 2:
                        print(f"{clave}".ljust(10)
                              + f"{dict_characters[clave]['name']}".ljust(17)
                              + f"{dict_characters[clave]['strength'] + dict_weapons[dict_characters[clave]['weapons'][0]]['strength'] + + dict_weapons[dict_characters[clave]['weapons'][1]]['strength']}".rjust(8) + " " * 5
                              + f"{dict_characters[clave]['speed'] + dict_weapons[dict_characters[clave]['weapons'][0]]['speed'] + dict_weapons[dict_characters[clave]['weapons'][1]]['speed']}".rjust(5) + " " * 5
                              + str(dict_characters[clave]['experience']).ljust(10)
                              )

# -----------LIST CHARACTERS BY SPEED
            elif opc == 4:
                print("Characters ordered by Speed".center(60, "=") + "\n" + "Id".ljust(10) + "Name".ljust(
                    17) + "Strength".rjust(8) + " " * 5 + "Speed".rjust(5) + " " * 5 + "Experience".ljust(
                    10) + "\n" + "*" * 60)

                claves_characters = list(dict_characters.keys())
                for pasada in range(len(claves_characters) - 1):
                    for j in range(len(claves_characters) - 1 - pasada):
                        # suma_p1 es la suma total de su pj
                        # print(f"personaje : {dict_characters[claves_characters[j]]['name']}")
                        suma_p1 = 0
                        claves_wp = list(dict_weapons.keys())
                        # Por longitud de mi lista de armas
                        for i in range(len(dict_characters[claves_characters[j]]['weapons'])):
                            # Comprobamos arma en diccionario de armas
                            for arma in range(len(dict_weapons)):
                                # print(f"id : {claves_wp[arma]}")
                                # print(f"nombre : {dict_weapons[claves_wp[arma]]['name']}")
                                if dict_characters[claves_characters[j]]['weapons'][i] == claves_wp[arma]:
                                    suma_p1 += dict_weapons[claves_wp[arma]]['speed']
                        suma_p1 += dict_characters[claves_characters[j]]['speed']
                        # print(f"suma daño : {suma_p1}")

                        # suma_p2 es la suma total de su pj
                        # print(f"personaje : {dict_characters[claves_characters[j+1]]['name']}")
                        suma_p2 = 0
                        claves_wp = list(dict_weapons.keys())
                        # Por longitud de mi lista de armas
                        for i in range(len(dict_characters[claves_characters[j + 1]]['weapons'])):
                            # Comprobamos arma en diccionario de armas
                            for arma in range(len(dict_weapons)):
                                # print(f"id : {claves_wp[arma]}")
                                # print(f"nombre : {dict_weapons[claves_wp[arma]]['name']}")
                                if dict_characters[claves_characters[j + 1]]['weapons'][i] == claves_wp[arma]:
                                    suma_p2 += dict_weapons[claves_wp[arma]]['speed']
                        suma_p2 += dict_characters[claves_characters[j + 1]]['speed']
                        # print(f"suma daño : {suma_p2}")

                        if suma_p1 > suma_p2:
                            aux = claves_characters[j]
                            claves_characters[j] = claves_characters[j + 1]
                            claves_characters[j + 1] = aux

                for clave in claves_characters:
                    if len(dict_characters[clave]['weapons']) == 0:
                        print(f"{clave}".ljust(10)
                              + f"{dict_characters[clave]['name']}".ljust(17)
                              + f"{dict_characters[clave]['strength']}".rjust(8) + " "*5
                              + f"{dict_characters[clave]['speed']}".rjust(5) + " "*5
                              + str(dict_characters[clave]['experience']).ljust(10)
                              )

                    elif len(dict_characters[clave]['weapons']) == 1:
                        print(f"{clave}".ljust(10)
                              + f"{dict_characters[clave]['name']}".ljust(17)
                              + f"{dict_characters[clave]['strength'] + dict_weapons[dict_characters[clave]['weapons'][0]]['strength']}".rjust(8) + " "*5
                              + f"{dict_characters[clave]['speed'] + dict_weapons[dict_characters[clave]['weapons'][0]]['speed']}".rjust(5) + " "*5
                              + str(dict_characters[clave]['experience']).ljust(10)
                              )

                    elif len(dict_characters[clave]['weapons']) == 2:
                        print(f"{clave}".ljust(10)
                              + f"{dict_characters[clave]['name']}".ljust(17)
                              + f"{dict_characters[clave]['strength'] + dict_weapons[dict_characters[clave]['weapons'][0]]['strength'] + + dict_weapons[dict_characters[clave]['weapons'][1]]['strength']}".rjust(8) + " " * 5
                              + f"{dict_characters[clave]['speed'] + dict_weapons[dict_characters[clave]['weapons'][0]]['speed'] + dict_weapons[dict_characters[clave]['weapons'][1]]['speed']}".rjust(5) + " " * 5
                              + str(dict_characters[clave]['experience']).ljust(10)
                              )

            else:
                flg_menu_041 = False
                flg_menu_04 = True



#/////////////FLG MENU 042 LIST WEAPONS
    while flg_menu_042:
        menu_042 = "Menu 042 (List Weapons)".center(40,"=") + "\n1)List by ID\n2)List by name\n3)List by strength\n4)List by speed\n5)Go back"
        print(menu_042)
        opc = input("->Option: ")
        while not opc.isdigit() or int(opc) not in (1, 2, 3, 4, 5):
            print("Invalid Option".center(40, "="))
            input("Press enter to continue\n")
            print(menu_042)
            opc = input("->Option: ")
        else:
            opc = int(opc)
# -----------LIST WEAPONS BY ID
            if opc == 1:
                print("Weapons ordered by ID".center(60, "=") + "\n" + "Id".ljust(10) + "Name".ljust(
                    17) + "Strength".rjust(8) + " " * 5 + "Speed".rjust(5) + " " * 5 + "Two_Hand".ljust(
                    10) + "\n" + "*" * 60)
                for clave in dict_weapons:
                    print(str(clave).ljust(10) + dict_weapons[clave]['name'].ljust(17) + str(
                        dict_weapons[clave]['strength']).rjust(8) + " " * 5 + str(
                        dict_weapons[clave]['speed']).rjust(5) + " " * 5 + str(
                        dict_weapons[clave]['two_hand']).ljust(10))

# -----------LIST WEAPONS BY NAME
            elif opc == 2:
                print("Weapons ordered by Name".center(60, "=") + "\n" + "Id".ljust(10) + "Name".ljust(
                    17) + "Strength".rjust(8) + " " * 5 + "Speed".rjust(5) + " " * 5 + "Two_Hand".ljust(
                    10) + "\n" + "*" * 60)
                claves_weapons = list(dict_weapons.keys())
                for pasada in range(len(claves_weapons) - 1):
                    for j in range(len(claves_weapons) - 1 - pasada):
                        if dict_weapons[claves_weapons[j]]["name"] > dict_weapons[claves_weapons[j + 1]]["name"]:
                            aux = claves_weapons[j]
                            claves_weapons[j] = claves_weapons[j + 1]
                            claves_weapons[j + 1] = aux

                for clave in claves_weapons:
                    print(str(clave).ljust(10) + dict_weapons[clave]['name'].ljust(17) + str(
                        dict_weapons[clave]['strength']).rjust(8) + " " * 5 + str(
                        dict_weapons[clave]['speed']).rjust(5) + " " * 5 + str(
                        dict_weapons[clave]['two_hand']).ljust(10))

# -----------LIST WEAPONS BY STRENGTH
            elif opc == 3:
                print("Weapons ordered by Strength".center(60, "=") + "\n" + "Id".ljust(10) + "Name".ljust(
                    17) + "Strength".rjust(8) + " " * 5 + "Speed".rjust(5) + " " * 5 + "Two_Hand".ljust(
                    10) + "\n" + "*" * 60)
                claves_weapons = list(dict_weapons.keys())
                for pasada in range(len(claves_weapons) - 1):
                    for j in range(len(claves_weapons) - 1 - pasada):
                        if dict_weapons[claves_weapons[j]]["strength"] > dict_weapons[claves_weapons[j + 1]]["strength"]:
                            aux = claves_weapons[j]
                            claves_weapons[j] = claves_weapons[j + 1]
                            claves_weapons[j + 1] = aux

                for clave in claves_weapons:
                    print(str(clave).ljust(10) + dict_weapons[clave]['name'].ljust(17) + str(
                        dict_weapons[clave]['strength']).rjust(8) + " " * 5 + str(
                        dict_weapons[clave]['speed']).rjust(
                        5) + " " * 5 + str(dict_weapons[clave]['two_hand']).ljust(10))

# -----------LIST WEAPONS BY SPEED
            elif opc == 4:
                print("Weapons ordered by Speed".center(60, "=") + "\n" + "Id".ljust(10) + "Name".ljust(
                    17) + "Strength".rjust(8) + " " * 5 + "Speed".rjust(5) + " " * 5 + "Two_Hand".ljust(
                    10) + "\n" + "*" * 60)
                claves_weapons = list(dict_weapons.keys())
                for pasada in range(len(claves_weapons) - 1):
                    for j in range(len(claves_weapons) - 1 - pasada):
                        if dict_weapons[claves_weapons[j]]["speed"] > dict_weapons[claves_weapons[j + 1]]["speed"]:
                            aux = claves_weapons[j]
                            claves_weapons[j] = claves_weapons[j + 1]
                            claves_weapons[j + 1] = aux

                for clave in claves_weapons:
                    print(str(clave).ljust(10) + dict_weapons[clave]['name'].ljust(17) + str(
                        dict_weapons[clave]['strength']).rjust(8) + " " * 5 + str(
                        dict_weapons[clave]['speed']).rjust(
                        5) + " " * 5 + str(dict_weapons[clave]['two_hand']).ljust(10))

# -----------GO BACK TO LIST04
            elif opc == 5:
                # Exit
                flg_menu_042 = False
                flg_menu_04 = True


    # ///////////////FLG MENU 043 LIST BY SIDE
    while flg_menu_043:
        print("Characters ordered by Side".center(80, "=") + "\n" + "Id".ljust(10)
              + "Name".ljust(17) + "Strength".rjust(8) + " " * 5 + "Speed".rjust(5) + " " * 5
              + "Experience".rjust(10)
              + "Side".rjust(20) + "\n" + "*" * 80)

        claves_characters = list(dict_characters.keys())
        claves_crew = list(dict_crews.keys())
        claves_rank = list(dict_ranks.keys())

        datos1 = ""
        datos2 = ""
        for clave in claves_characters:
            strength = 0
            claves_wp = list(dict_weapons.keys())
            for i in range(len(dict_characters[clave]['weapons'])):
                for arma in range(len(dict_weapons)):
                    if dict_characters[clave]['weapons'][i] == claves_wp[arma]:
                        strength += dict_weapons[claves_wp[arma]]['strength']
            strength += dict_characters[clave]['strength']

            speed = 0
            claves_wp = list(dict_weapons.keys())
            for i in range(len(dict_characters[clave]['weapons'])):
                for arma in range(len(dict_weapons)):
                    if dict_characters[clave]['weapons'][i] == claves_wp[arma]:
                        speed += dict_weapons[claves_wp[arma]]['speed']
            speed += dict_characters[clave]['speed']




            if dict_characters[clave]["category"] > 5:
                datos1 += (str(clave).ljust(10) + dict_characters[clave]['name'].ljust(17)
                           + str(strength).rjust(8) + " " * 5
                           + str(speed).rjust(5) + " " * 5
                           + str(dict_characters[clave]['experience']).rjust(10)
                           + "Marine".rjust(20)) + "\n"
            else:
                datos2 += (str(clave).ljust(10) + dict_characters[clave]['name'].ljust(17)
                           + str(strength).rjust(8) + " " * 5
                           + str(speed).rjust(5) + " " * 5
                           + str(dict_characters[clave]['experience']).rjust(10)
                           + "Pirate".rjust(20)) + "\n"

        print(datos1 + datos2)
        input("Press Enter to go back")
        flg_menu_043 = False
        flg_menu_04 = True



#///////////////FLG MENU 044 LIST BY RANGE
    while flg_menu_044:
        print("Characters ordered by Range".center(80, "=") + "\n" + "Id".ljust(10) + "Name".ljust(
            17) + "Strength".rjust(8) + " " * 5 + "Speed".rjust(5) + " " * 5 + "Experience".rjust(
            10) + "Range".rjust(20) + "\n" + "*" * 80)
        claves_characters = list(dict_characters.keys())
        for pasada in range(len(claves_characters) - 1):
            for j in range(len(claves_characters) - 1 - pasada):
                if dict_categorys[dict_characters[claves_characters[j]]['category']] > dict_categorys[dict_characters[claves_characters[j + 1]]['category']]:
                    aux = claves_characters[j]
                    claves_characters[j] = claves_characters[j + 1]
                    claves_characters[j + 1] = aux

        for clave in claves_characters:
            strength = 0
            claves_wp = list(dict_weapons.keys())
            for i in range(len(dict_characters[clave]['weapons'])):
                for arma in range(len(dict_weapons)):
                    if dict_characters[clave]['weapons'][i] == claves_wp[arma]:
                        strength += dict_weapons[claves_wp[arma]]['strength']
            strength += dict_characters[clave]['strength']

            speed = 0
            claves_wp = list(dict_weapons.keys())
            for i in range(len(dict_characters[clave]['weapons'])):
                for arma in range(len(dict_weapons)):
                    if dict_characters[clave]['weapons'][i] == claves_wp[arma]:
                        speed += dict_weapons[claves_wp[arma]]['speed']
            speed += dict_characters[clave]['speed']

            print(str(clave).ljust(10) + dict_characters[clave]['name'].ljust(17) + str(strength).rjust(8) + " " * 5 + str(speed).rjust(
                5) + " " * 5 + str(dict_characters[clave]['experience']).rjust(10) + dict_categorys[
                      dict_characters[clave]['category']].rjust(20))

        input("Press Enter to go back")
        flg_menu_044 = False
        flg_menu_04 = True
