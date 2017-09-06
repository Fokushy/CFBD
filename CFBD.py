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
            return True
        except:
            return False

    while exist(path) == False:
        path = input('Your "fstab" file can not be found in "/etc/". Please select it manually : \n-> ')

    main = True
    while main == True:
        folder = input("\n\nWhich folder do you want to change the path ? (Enter the number) :\n\n1 - Music\n2 - Pictures\n3 - Documents\n4 - Videos\n5 - Desktop\n6 - Downloads\n7 - All folders\n\nSelection : \n-> ")

        while folder != "1" and folder != "2" and folder != "3" and folder!= "4" and folder!= "5" and folder!= "6" and folder!= "7":
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

        yesorno = input('Your directory "%s" will be mounted in "%s" persistently. Are you sure ? (Yes / No) : \n-> ' % (choice, folder))
        while yesorno != "Yes" and yesorno != "yes" and yesorno != "No" and yesorno != "no":
            yesorno = input('Please answer "Yes" or "No" : \n-> ')
        print(yesorno)
        if yesorno == "Yes" or yesorno == "yes":
            main = False

    file = open(path, 'a')
    text = "\n\n#CFBD\n" + line

    #Here we will look for if the script has already been used to avoid a malfunction in the fstab file.
    l = "Doge"
    while l != "":
        l = file.readline()
        if l.startswith("#CFBD_Start") :
            pass
    #fichier.write(text)
    file.close()
except KeyboardInterrupt:
    print("\n\nAlready ? Goodbye !")
