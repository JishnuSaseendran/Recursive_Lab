import os

cwd = os.getcwd()

def walk(directory):

    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path):

walk(cwd)

