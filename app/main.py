import sys
import os


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
                    PATH="/usr/bin:/usr/local/bin"
                    pathList = PATH.split(':')
                    
                    if os.path.exists(f"{pathList[0]}/{args[0]}") == True:
                        print(f"{args[0]} is {pathList[0]}/{args[0]}")
                    elif os.path.exists(f"{pathList[1]}/{args[0]}") == True:
                        print(f"{args[0]} is {pathList[1]}/{args[0]}")
                    else:
                        print(f"{args[0]}: not found")
            case _:
                print(f"{command}: command not found")
    
    return


if __name__ == "__main__":
    main()
