import mysql.connector as mysql

#******** Setting akun Database ********#
host_db = 'localhost'
user_db = ''
passwd_db = ''
nama_db = 'uji_coba'
#**************************************#

# Koneksi database ke xampp
db = mysql.connect(
    host=host_db,
    user=user_db,
    passwd=passwd_db,
    database=nama_db
)

cursor = db.cursor()
print("Tampilkan Data Databases")
print("1. Admin\n2. Users")
pilih = int(input(" Pilihan : "))

if (pilih == 1):
    # Tampilkan semua data table admin
    sql = "SELECT * FROM admin"
    cursor.execute(sql)
    #db.commit()
    results = cursor.fetchall()
    list_data = ""

    for data in results:
        list_data += f"\nADMIN ID\t: {data[0]} \nADMIN NAME\t: {data[1]} \nADMIN ADDRESS\t: {data[2]}\n"

    print(list_data)

    db.close()

elif (pilih == 2):
    # Tampilkan semua data table admin
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    #db.commit()
    results = cursor.fetchall()
    list_data = ""

    for data in results:
        list_data += f"\nADMIN ID\t: {data[0]} \nADMIN NAME\t: {data[1]} \nADMIN ADDRESS\t: {data[2]}\n"

    print(list_data)

    db.close()

else:
    print("Pilihan tidak ada")
