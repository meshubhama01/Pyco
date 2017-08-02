import os

os.system("clear")
print "-" * 80
print "OS Walk Program"
print "-" * 80
print "
"

print "Root prints out directories only from what you specified"
print "-" * 70

print "Dirs prints out sub-directories from root"
print "-" * 70

print "Files prints out all files from root and directories"
print "-" * 70

print "This program will do an os.walk on the folder that you specify"
print "-" * 70

path = raw_input("Specify a folder that you want to perform an 'os.walk' on: >> ")

for root, dirs, files in os.walk(path):

    print root
    print "---------------"

    print dirs
    print "---------------"

    print files
    print "---------------"
