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
            case _:
                sys.stdout.write(f"{command}: command not found\n")
    
    return


if __name__ == "__main__":
    main()
