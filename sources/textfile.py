import os
print(os.getcwd())

fd = open("kant.txt")
content = fd.read()
print(content)

fout = open("file1.txt", "w")
content = fout.write("Alles neu mächt der Mai!")
fout.close()

fapp = open("file2.txt", "a")
content = fapp.write("Alles neu mächt der Mai!\n")
fapp.close()