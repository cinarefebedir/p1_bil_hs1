# print("Sevgi Hesaplayıcıya HG")
isim1 = input("Adınız?")
isim2 = input("Onun adı?")

isimler = (isim1 + isim2 ). lower()
g = isimler.count("g")
e = isimler.count("e")
r = isimler.count("r")
ç = isimler.count("ç")
e = isimler.count("e")
k = isimler.count("k")
a = isimler.count("a")
ş = isimler.count("ş")
k = isimler.count("k")

toplam = g + e + r + ç + e + k + a + ş + k

if(toplam < 10 and toplam > 90):
    print(f"Sevgi puanınız: {toplam}, kola mentos gibisiniz")
elif(toplam > 40 and toplam < 50):
    print(f"Sevgi Puanınız: {toplam}, beraber iyisiniz!")
else:
    print(f"Sevgi Puanınız: {toplam}")