import requests
# Import modul requests untuk mengambil data dari API

# Meminta input nama kota dari user
print("")
kota = input("Masukan nama kota     : ")
if not kota.replace(" ", "").isalpha(): # isalpha : memastikan hanya huruf
    print("jangan masukin angka woi...!!!!")
    exit()

# validasi tahun
tahun = input("Masukan Tahun         : ")
if not tahun.isdigit(): # isdigit : mengecek apakah semua karakter adalah angka
    print("error")
    exit()

# validasi bulan
bulan = input("Masukan bulan (angka) : ")
if not bulan.isdigit():
    print("error")
    exit()

# validasi tanggal
tanggal =input("Masukan Tanggal       : ")
if not tanggal.isdigit():
    print("error")
    exit()


# KONVERSI KE INTEGER
tahun = int(tahun)
bulan = int(bulan)
tanggal = int(tanggal)

# format tanggal
tanggal_lengkap = f"{str(tanggal).zfill(2)}-{str(bulan).zfill(2)}-{tahun}"
# zfill(2) : menambahkan nol di depan jika hanya 1 digit

# Cek Tanggal, Bulan dan Tahun harus angka
# if not (tanggal.isdigit() and bulan.isdigit() and tahun.isdigit()):
#     print("Program Error")
#     exit() 




# Menggabungkan tanggal ke format DD-MM-YYYY
# tanggal_lengkap = f"{tanggal.zfill(2)}-{bulan.zfill(2)}-{tahun}"
# Membuat URL API dengan nama kota dari input
target_url = (
    f"https://api.aladhan.com/v1/timingsByCity/{tanggal_lengkap}"
    f"?city={kota}&country=Indonesia&method=20"
)

# Mengirim request ke API (HTTP GET)
response = requests.get(target_url)

# Mengubah hasil response API menjadi format JSON
data_json = response.json()

if data_json['code'] != 200:
    print("eror")
    exit()

# Mengecek apakah data dari API berhasil diambil
# code 200 artinya berhasil, selain itu berarti error
# if data_json['code'] != 200:
#     print("program error")
#     exit()

# Menampilkan judul jadwal sholat
print("")
print("======= JADWAL SHOLAT =======")
print("")
# print("=" * 20)

# Mengambil data jadwal sholat dari JSON
jadwal = data_json['data']['timings']

# Mengambil masing-masing waktu sholat
imsak    = jadwal['Imsak']
shubuh   = jadwal['Fajr']
terbit   = jadwal['Sunrise']
dzuhur   = jadwal['Dhuhr']
ashar    = jadwal['Asr']
terbenam = jadwal['Sunset']
magrib   = jadwal['Maghrib']
isya     = jadwal['Isha']


# Menampilkan hasil jadwal sholat
print(f"  - Imsak    : {imsak}")
print(f"  - Shubuh   : {shubuh}")
print(f"  - Terbit   : {terbit}")
print(f"  - Dzuhur   : {dzuhur}")
print(f"  - Ashar    : {ashar}")
print(f"  - Terbenam : {terbenam}")
print(f"  - Maghrib  : {magrib}")
print(f"  - Isya     : {isya}")
print("")
print("=============================")
print("")