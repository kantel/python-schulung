de2nl = {"eins" : "een", "zwei" : "twee", "drei" : "drie", "vier" : "vier", "fünf" : "vijf", "sechs" : "zes"}
print(de2nl)

for key in de2nl:
    print(key, de2nl[key])
    
print(len(de2nl))

ziffern = de2nl.values()
print("zes" in ziffern)

t = de2nl.items()
print(t)

s = de2nl.keys()
print(s)

for key in de2nl.keys():
    print(key)
    
