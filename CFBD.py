import os
import sys

try :
    path = "/etc/fstabb"

    home = os.getenv("SUDO_USER")
    if home == "root":
        print("This can not be started as root. Please run it as a standard user.")
        quit()
    elif type(home) != str:
        print('Have you started the program with "sudo" ?')
        quit()

    home = "/home/" + home
    os.chdir(home)
    print(os.getcwd())

    def exist(path):
        try:
            fichier = open(path, 'r')
            fichier.close()
            return True
        except:
            return False

    def exist2(path):
        try:
            fichier = open(path + "/test.txt", 'w')
            fichier.close()
            os.remove(path + "/test.txt")
            return True
        except:
            return False

    while exist(path) == False:
        path = input('Your "fstab" file can not be found in "/etc/". Please select it manually : \n-> ')

    main = True
    Lines = []
    while main == True:
        done = False
        while done == False:
            if len(Lines) > 0 :
                folder = input('\n\nAnother folder ? Type "Done" if you are done." :\n\n1 - Music\n2 - Pictures\n3 - Documents\n4 - Videos\n5 - Desktop\n6 - Downloads\n7 - All folders\n\nSelection : \n-> ')
            else:
                folder = input("\n\nWhich folder do you want to change the path ? (Enter the number) :\n\n1 - Music\n2 - Pictures\n3 - Documents\n4 - Videos\n5 - Desktop\n6 - Downloads\n7 - All folders\n\nSelection : \n-> ")
            #Faire condition si Done == True et que rien n'est sélectionné, ajouter à liste Lines à chaque tour
            while folder != "1" and folder != "2" and folder != "3" and folder!= "4" and folder!= "5" and folder!= "6" and folder!= "7" and folder!= "Done" and folder != "done":
                folder = input("Please enter a valid number : \n-> ")

            if folder == "1":
                folder = home + "/Music"
            elif folder == "2":
                folder = home + "/Pictures"
            elif folder == "3":
                folder = home + "/Documents"
            elif folder == "4":
                folder = home + "/Videos"
            elif folder == "5":
                folder = home + "/Desktop"
            elif folder == "6":
                folder = home + "/Downloads"
            elif folder == "7":
                pass
            elif folder == "Done" :
                done = True

            if done == False :
                state = False
                choice = input('\n\nEnter the path to the target folder (Example : "/media/user/MyPartition/Music") : \n-> ')
                while state == False:
                    if choice == "":
                        choice = input("\nPlease enter a path to the target folder : \n-> ")
                    elif exist2(choice) == False:
                        choice = input("\nYour path to the target folder looks incorrect, please try again : \n-> ")
                    else :
                        state = True

                line = choice + "   " + folder + "     none       bind      0   0"
                Lines.append(line)


        print(Lines)
        yesorno = input('\nYour directory "%s" will be mounted in "%s" persistently. Are you sure ? (Yes / No) : \n-> ' % (choice, folder))
        while yesorno != "Yes" and yesorno != "yes" and yesorno != "No" and yesorno != "no":
            yesorno = input('Please answer "Yes" or "No" : \n-> ')
        if yesorno == "Yes" or yesorno == "yes":
            main = False

    text = "\n#CFBD_start\n" + line + "\n#CFBD_end"

    #Here we will look for if the script has already been used to avoid a malfunction in the fstab file.
    try :
        file = open(path, 'r')
        fstemp = file.readlines()
        file.close()
        count = 0
        for li in fstemp:
            if li.startswith("#CFBD_start"):
                line1 = count
            elif li.startswith("#CFBD_end"):
                line2 = count
            count+=1
        lines = []
        for li in range(line1-1, line2+1):
                lines.append(li)
        print(lines)
        lines2 = []
        for li in range(line1+1, line2):
            lines2.append(li)
        if len(lines) > 0:
            print("\nThis previous configuration was found in the fstab file from line %s to line %s :\n" % (line1+2,line2))
            for li in lines2 :
                print(fstemp[li], end='')
            yesorno = input("\nAre you sure you want to replace it ? : \n-> ")
            while yesorno != "Yes" and yesorno != "yes" and yesorno != "No" and yesorno != "no":
                yesorno = input('Please answer "Yes" or "No" : \n-> ')
            if yesorno == "Yes" or yesorno == "yes":
                try :
                    while fstemp[lines[0]] != "":
                        del fstemp[lines[0]]
                except :
                    print(text)
                    fstemp.append(text)
                    file = open(path, 'w')
                    for i in fstemp:
                        file.write(i)
                    file.close()

    except NameError:
        print("No previous configuration was found in the fstab file.")
        file = open(path, 'a')
        file.write(text)
        file.close()

except KeyboardInterrupt:
    print("\n\nAlready ? Goodbye !")
