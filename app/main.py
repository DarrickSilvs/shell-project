import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command, *args = input().split(" ")
        if command == "exit":
            break
        elif command == "echo":
            print(" ".join(args))
        else:
            print(f"{command}: command not found")
    
    return


if __name__ == "__main__":
    main()
