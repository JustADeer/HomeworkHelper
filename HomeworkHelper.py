from os.path import exists

savefile = "data.txt"


def AfCommand(command=""):
    if len(command) >= 2 and str(command[0] + command[1]) == "pr":
        v = command.replace("pr", "").rstrip()
        count = 0
        if exists(savefile) == True:
            data = open(savefile, "r")
            for line in data.readlines():
                count += 1
                Pline = "[{}] : {}".format(count, line.strip())
                # Checks if what ur finding is in the line
                if v != "":
                    if v.lower() in Pline.lower():
                        print(Pline)
                else:
                    print(Pline)
        data.close()
        print("")

    elif "+pr" in command:
        v = command.replace("+pr", "").rstrip()
        if v != "":
            if exists(savefile) == True:
                data = open(savefile, "a")
                data.write(v + "\n")
                data.close()

    elif "-pr" in command:
        v = command.replace("-pr", "").rstrip()
        if v != "":
            v = int(v) - 1
            if exists(savefile) == True:
                data = open(savefile, "r")
                lines = data.readlines()
                data.close()
                del lines[v]
                new_file = open(savefile, "w")
                for line in lines:
                    new_file.write(line)
                new_file.close()

    elif command == "clear":
        open(savefile, "w").close()

    elif command == "help":
        print("\npr .[find],\n+pr [name],\n-pr [index],\nclear,\nquit,\nhelp\n")

    elif command == "quit":
        quit()

    else:
        print("This is Not a Command!\n")


if __name__ == "__main__":
    if exists(savefile) == False:
        f = open(savefile, "w")
        f.close()
    while True:
        command = input("Command : ")
        print("")
        AfCommand(command)
