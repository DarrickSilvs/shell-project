import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if str(command) == "exit 0":
            break

        ls = command.split(" ")
        if str(ls[0]) == "echo":
            print(ls[1:])
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
