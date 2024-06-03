inp_str = "sssskkd"
inp_rev = ""

for char in inp_str:
  if inp_str.count(char) == 1 :
    inp_rev = char + inp_rev
print("Char is a : ",inp_rev)