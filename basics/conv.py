mylist = [10, -20, 100, -400, 25, 15, 9, 38]
def cel_to_fahr(cels):
    if cels > -273.15:
        fahr = cels * 9/5 + 32
        return fahr

def writer(temperatures, filepath):
    with open(filepath,"w") as myfile:
        for i in temperatures:
            #print(cel_to_fahr(i))
            j = cel_to_fahr(i)
            myfile.write(str(j) + "\n")

writer(mylist, "homerseklet.txt")
