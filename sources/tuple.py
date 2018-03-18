# Tupel

t = "a", "b", "c"
print(t)

t = ("a", "b", "c")
print(t)

t1 = "a",
print(type(t1))

t2 = ("a")
print(type(t2))

t3 = ("a", )
print(type(t3))

t4 = tuple()
print(t4)

motto = tuple("don't panic")
print(motto)

# motto[0] = "W"

motto2 = ("W", ) + motto[1:]
print(motto2)

adr = "joerg@kantel.de"
uname, domain = adr.split("@")
print(uname)
print(domain)

s = "monty"
l = [0, 1, 2, 3, 4, 5]
t = zip(s, l)
print(list(t))
