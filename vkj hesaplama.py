#problem
boy = float(input("boyunu gir"))
kilo = float(input("kilonu gir"))
vkj = kilo / (boy **2)
if vkj < 18:
    print("zayıfsın")
elif 25>vkj and vkj<18:
    print("normal")
elif 29>vkj and vkj<25:
    print("kilolu")
elif 34>vkj and vkj<30:
    print("obezitsin")   