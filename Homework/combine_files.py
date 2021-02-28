
data = data2 = data3 = ""
with open("Class-Ex-Lecture4_1.py") as fp:
    data = fp.read()

with open("Class-Ex-Lecture4_2.py") as fp:
    data2 = fp.read()

with open("Class-Ex-Lecture4_3.py") as fp:
    data3 = fp.read()

data += "\n"
data += data2
data += "\n"
data += data3

with open("Class-Ex-Lecture4_All.py", 'w') as fp:
    fp.write(data)
