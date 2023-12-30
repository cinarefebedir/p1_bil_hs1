#problem
boy = float(input("boyunu gir"))
kilo = float(input("kilonu gir"))
vkj = kilo / (boy **2)
if vkj > 25:
    idealKilo = 25 * (boy ** 2)
    print("vkiniz çok yüksek." f"{kilo-idealKilo} vermelisiniz")
elif vkj < 18:
    idealKilo = 18 * (boy ** 2)
    print("vkiniz düşük." f"{kilo-idealKilo} vermelisiniz")
else:
    print("vkiniz normal")
