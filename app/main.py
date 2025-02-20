import sys
import os

PATH="/usr/bin:/usr/local/bin"

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
                    if os.path.exists(f"{PATH}/{args[0]}") == True:
                        print(f"{args[0]} is {PATH}/{args[0]}")
                    else:
                        print(f"{args[0]}: not found")
            case _:
                print(f"{command}: command not found")
    
    return


if __name__ == "__main__":
    main()
