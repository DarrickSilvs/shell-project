import sys


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
                if args in builtin:
                    print(f"{command} is a shell builtin")
                else:
                    print(f"{command}: not found")
            case _:
                print(f"{command}: command not found")
    
    return


if __name__ == "__main__":
    main()
