import sys
import os
import subprocess

def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command, *args = input().split(" ")
        match command:
            case "exit":
                break
            case "echo":
                print(" ".join(args))
            case "type":
                builtin = ['exit', 'echo', 'type']
                if args[0] in builtin:
                    print(f"{args[0]} is a shell builtin")
                else:
                    path = checkPathFile(args[0])
                    if path != False:
                        print(f"{args[0]} is {path}/{args[0]}")
                    else:
                        print(f"{args[0]}: not found")
            case _:
                path = checkPathFile(sys.argv[0])
                if path != False:
                    subprocess.run(sys.argv[0] + sys.argv[1])
                else:
                    print(f"{command}: command not found")
    
    return

def checkPathFile(file):
    pathList = os.environ["PATH"].split(':')
    flag = False
    for i in pathList:
        if os.path.exists(f"{i}/{file}") == True:
            flag = i
            break
    return flag

if __name__ == "__main__":
    main()
