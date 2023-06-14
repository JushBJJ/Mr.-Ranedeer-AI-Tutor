import os

directory = "./v2.6/testing/outputs/"

for filename in os.listdir(directory):
    with open(directory + filename, "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents, end="")
