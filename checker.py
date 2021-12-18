f = open("License_data.txt")
License_data = f.read()
f.close()
Licenses_list = License_data.split(";")
class License_card:
    def __init__ (self,name,age,status):
       self.Name = name
       self.Age = age
       self.Status = status
    def printcard(self):
        print("%s\n%s\n%s\n"%(self.Name,self.Age,self.Status))


License_cards = []
for x in range(len(Licenses_list)):
    Temp_card = Licenses_list[x].split(",")
    License_cards.append( License_card(Temp_card[0],Temp_card[1],Temp_card[2]))

for x in Licenses_list : 
    print (x)

print ("%s licenses in the database"%len(License_cards))
givenname = input ("Enter name : ")

i = 0
while i < (len(License_cards)) :
    if givenname == License_cards[i].Name :
        License_cards[i].printcard()
        print("code %s" %License_cards[i].Status)
        if License_cards[i].Status == "Green":
            print("good to go")
            break
            pass
        elif License_cards[i].Status == "Yellow":
            print("Fines due")
            break
            pass
        elif License_cards[i].Status == "Red":
            print("I recognize this man!")
            break
            pass
    else: print ("not a match")
    i += 1




