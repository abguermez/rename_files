import os
print("When you input path please write it with in forward slash in place of blackslash, Thank you.")
path = input("Give your path: ")
name = input("new file name: ")
type = input("the file's type")


def main():
    i = 0
    dest = path
    for filename in os.listdir(dest):
        my_dest = name + str(i) + type
        my_src = dest + filename
        my_dest = dest + my_dest
        os.rename(my_src, my_dest)
        i = i+1
if __name__ == '__main__':
    main()