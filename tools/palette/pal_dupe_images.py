import shutil
for i in range(1, 41):
    dupe = str(i) + ".png"
    shutil.copyfile("0.png", dupe)