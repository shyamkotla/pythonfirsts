f = open("Local_Hotels_Database.txt",)
Database = f.read()
f.close()
nnr = Database.split(";")
hnames = []
hrating = []
hvotes = []
for i in range(len(nnr)):
    thishoteldata = nnr[i]
    thishotelname = thishoteldata[:thishoteldata.index(",")]
    thishotelrating = thishoteldata[(thishoteldata.index("=") + 1):thishoteldata.index("(")]
    thishotelvotes = thishoteldata[(thishoteldata.index("(") + 1):(thishoteldata.index(")"))]
    hnames.append(thishotelname)
    hrating.append(thishotelrating)
    hrating[i] = float(hrating[i])
    hvotes.append(thishotelvotes)
    hvotes[i] = int(hvotes[i])
print (hnames)

givenhotelname = input ("Enter the name of the Hotel : ")
givenrating = float(input ("Rate your experience (0.1 - 10.0) : "))

for k in range(len(nnr)):
    if givenhotelname == hnames[k]:
        hrating[k] = ((hrating[k] * hvotes[k]) + givenrating)/(hvotes[k] + 1)
        hvotes[k] += 1


for j in range(len(nnr)) :
    if j == 0 : 
        f = open("Local_Hotels_Database.txt","w",)
        f.write("%s,avg = %1.1f(%d)"%(hnames[j],hrating[j],hvotes[j]))
        f.close()
    else : 
        f = open("Local_Hotels_Database.txt","a",)
        f.write(";%s,avg = %1.1f(%d)"%(hnames[j],hrating[j],hvotes[j]))
        f.close()

