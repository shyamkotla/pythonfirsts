f = open("License_data.txt")
License_data = f.read()
f.close()
Licenses_list = License_data.split(";")
Licenses_dict = {}

for x in range(len(Licenses_list)):
    i = Licenses_list[x].split(",")
    Licenses_dict ["%s"%i[0]] = "%s"%i[2]

print(Licenses_dict)

name = input("Enter Name : ")
status = Licenses_dict["%s"%name]
print ("%s is code %s" %(name,status))