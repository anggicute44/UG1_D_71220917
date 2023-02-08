
print()
  
x = input('kalimat yang ingin diteliti: ')
print()
 
# Konversi string x ke huruf kecil 
x = x.lower()
 
# Hitung jumlah huruf vokal
vokal = 0
for i in x:
  if(i=='a' or i=='i' or i=='u' or i=='e' or i=='o'):
    vokal = vokal + 1
 
# Tampilkan total huruf vokal jika ditemukan
if vokal > 0 :
  print('Jumlah Kata yang dicari =', vokal)
else:
  print('Huruf vokal tidak ditemukan')
