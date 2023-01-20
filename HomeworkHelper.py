from os.path import exists

savefile = "data.txt"

test = 5
abelbodoy = True

def AfCommand(command=""):
    if exists(savefile) == True:
        if len(command) >= 2 and str(command[0] + command[1]) == "pr":
            v = command.replace("pr", "").rstrip()
            count = 0
            data = open(savefile, "r")
            if v != "":
                for line in data.readlines():
                    count += 1
                    Pline = "[{}] : {}".format(count, line.strip())
                    # Checks if what ur finding is in the line
                    if v.lower() in Pline.lower():
                        print(Pline)
            else:
                for line in data.readlines():
                    count += 1
                    print("[{}] : {}".format(count, line.strip()))
            print("")
            data.close()

        elif "+pr" in command:
            v = command.replace("+pr", "").rstrip()
            if v != "":
                data = open(savefile, "a")
                data.write(v + "\n")
                data.close()
            else:
                print("There is no name added. Add a name after like this '+pr name'\n")

        elif "-pr" in command:
            v = command.replace("-pr", "").rstrip()
            if v != "":
                v = int(v) - 1
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

        elif command == "sF":
            print(savefile + "\n")

        else:
            print("This is Not a Command!\n")


if __name__ == "__main__":
    if exists(savefile) == False:
        open(savefile, "w").close()
    while 1:
        command = input("Command : ")
        print("")
        AfCommand(command)
