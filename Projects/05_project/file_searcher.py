import os
def file_founder(name):
    for root, dirs, files in os.walk("/home/adu/Documents/Pythontry1/Projects/05_project", topdown=True):
        if name in files:
            return True
        else:
            return False
    return None




