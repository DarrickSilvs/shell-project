import sys
import os
import subprocess

def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command, *args = input().split()

        # Remove single quotes
        args = [arg.strip().replace("'", "") for arg in args]
        
        match command:
            case "exit":
                break
            case "echo":
                print(" ".join(args))
            case "pwd":
                print(os.getcwd())
            case "cd":
                try:
                    os.chdir(args[0])
                except:
                    if args[0] == '~':
                        user_home_dir = os.environ['HOME']
                        os.chdir(user_home_dir)
                    else:    
                        print(f"cd: {args[0]}: No such file or directory")
            case "type":
                builtin = ['exit', 'echo', 'type', 'pwd', 'cd']
                if args[0] in builtin:
                    print(f"{args[0]} is a shell builtin")
                else:
                    path = checkPathFile(args[0])
                    if path != None:
                        print(f"{args[0]} is {path}")
                    else:
                        print(f"{args[0]}: not found")
            case _:
                path = checkPathFile(command)
                if path != None and os.access(path, os.X_OK):
                    subprocess.run([command] + args)
                else:
                    print(f"{command}: command not found")
    
    return

def checkPathFile(file):
    pathList = os.environ["PATH"].split(':')
    for i in pathList:
        if os.path.exists(f"{i}/{file}"):
            return os.path.join(i, file)
    return None

if __name__ == "__main__":
    main()
