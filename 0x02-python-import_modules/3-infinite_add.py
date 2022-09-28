#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    list_of_args = []

    if len(argv) == 1:
        print("0")
    else:
        for i in range(1, len(argv)):
            list_of_args.append(int(argv[i]))

        print(sum(list_of_args))
