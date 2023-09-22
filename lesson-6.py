import os


#
# path = os.path.normpath("C:/Windows/Web")
# dir_1 = "Windows"
# dir_2 = "Web"
# path_1 = os.path.join(dir_1, dir_2)
#
# for path, dirnames, filenames in os.walk(path):
#     print(f"path = {path}")
#     print(f"dirnames = {dirnames}")
#     print(f"filenames = {filenames}")
#
# print(path_1)
# print(os.path.isabs(path))
# print(os.path.isfile(path))
# print(os.path.isdir(path))
# print(os.path.islink(path))
# os.mkdir("new_dir")
# os.mkdir("new_dir1")
# os.rmdir("new_dir")

# file = open("file.txt", "w")
# file.write("Hello World")
# file.close()
# file = open("file.txt", "a")
# file.write("\nHi")
# file.close()
# file = open("file.txt", "r")
# print(file.read())
# file.close()

# with open("file.txt", "w") as file:
#     file.write("Hello World")
# with open("file.txt", "a") as file:
#     file.write("\nHi")
# with open("file.txt", "r") as file:
#     print(file.read())

# os.rename("file.txt", "files.txt")
# os.rename("file.txt", "files.txt")
# print(os.path.getsize("files.txt"))
# print(os.path.getmtime("files.txt"))

def file_collector(path):
    path = os.path.normpath(path)
    result = {"dirs": [], "files": []}
    for path, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result["dirs"].append(dir)
        for file in filenames:
            result["files"].append(file)
    with open("skiper.txt", "w") as file:
        file.write("\n{:-<50}\n".format("Directories"))
        for dir in result["dirs"]:
            file.write(f"\t{dir}\n")
            file.write("\n{:-<50}".format("Files"))
        for files in result["files"]:
            file.write(f"\t{files}\n")


path = "C:\Program Files"
file_collector(path)
