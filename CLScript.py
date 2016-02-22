buffer = ["run (console.log) (\"Hello World\")"]
ns = {'__builtins__': None}
variables = {}
#change default print function if needed
#def print(txt):
#   #

##### SET DEFAULT VARIABLES AND FUNCTIONS HERE #####
#variables["@player.location.x"] = 0
#variables["@player.location.y"] = 0
#variables["@player.location.z"] = 0

def split(s):
     parts = []
     bracket_level = 0
     current = []
     for c in (s + " "):
         if c == " " and bracket_level == 0:
             parts.append("".join(current))
             current = []
         else:
             if c == "(":
                 bracket_level += 1
             elif c == ")":
                 bracket_level -= 1
             current.append(c)
     return parts

def execute(cmd):
    try:
        if cmd[0] == "set":
            cmd[1] = cmd[1].lstrip("(").rstrip(")")
            cmd[2] = cmd[2].lstrip("(").rstrip(")")
            if bool(variables[cmd[1]]):
                variables[cmd[1]] = eval(cmd[2], ns)
            else:
                print("variable does not exist")
        elif cmd[0] == "get":
            cmd[1] = cmd[1].lstrip("(").rstrip(")")
            if bool(variables[cmd[1]]):
                print(variables[cmd[1]])
            else:
                print("'" + cmd[1] + "' does not exist")
        elif cmd[0] == "new":
            cmd[1] = cmd[1].lstrip("(").rstrip(")")
            variables[cmd[1]] = " "
        elif cmd[0] == "del":
            cmd[1] = cmd[1].lstrip("(").rstrip(")")
            variables[cmd[1]] = None
        elif cmd[0] == "makefunc":
            cmd[1] = cmd[1].lstrip("(").rstrip(")")
            variables[cmd[1]] = ["func"]
        elif cmd[0] == "setfunc":
            cmd[1] = cmd[1].lstrip("(").rstrip(")")
            cmd[2] = cmd[2].lstrip("(").rstrip(")")
            cmd[3] = cmd[3].lstrip("(").rstrip(")")
            variables[cmd[1]][int(cmd[2])] = cmd[3]
        elif cmd[0] == "if":
            cmd[1] = cmd[1].lstrip("(").rstrip(")")
            cmd[2] = cmd[2].lstrip("(").rstrip(")")
            cmd[3] = cmd[3].lstrip("(").rstrip(")")
            if bool(eval(variables[cmd[1]], ns)):            
                execute(variables[cmd[2]])
            else:
                execute(variables[cmd[3]])
        elif cmd[0] == "run":
            execute(cmd[1])
        elif cmd[0] == "exit":
            #reset anything here
            exit()
        else:
            print("invalid command")
    except IndexError:
        print("wrong number of arguments supplied")
    except KeyError:
        print("variable does not exist")

##### RUN A FILE #####
#for line in buffer:
#    if list(line)[0] != "#":
#        execute(split(line))

##### INTERPRETER #####
while True:
    line = input("@CLScript> ")
    execute(split(line))
