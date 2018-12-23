import glob2
from datetime import datetime
szorsz = ["file1.txt", "file2.txt", "file3.txt"]
#fajlnev = str(date(now)) + ".txt"
fajlnev = "etwas.txt"

def writer(fajlok, fajlpath):
    with open(fajlpath, "a") as myfile:
        for s in fajlok:
            readf = open(s)
            content = readf.read()
            readf.close()
            myfile.write(content + "\n")
    myfile.close()

writer(szorsz, fajlnev)

filenames = glob2.glob("*.txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename, "r") as f:
            file.write(f.read() + "\n")
