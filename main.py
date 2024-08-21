import datetime
hozir_sana = datetime.date.today()
yil = str(hozir_sana)
a = yil[:4]
k_sana = int(a)-45
b = str(hozir_sana.replace(k_sana))
k_yil = b[:4]
print(k_yil)
