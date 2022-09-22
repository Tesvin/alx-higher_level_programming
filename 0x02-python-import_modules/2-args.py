#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print(sys.argv)
    print(len(sys.argv))
    for i in range(0,len(sys.argv)):
        print(i,":", sys.argv[i])
