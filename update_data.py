import mysql.connector as mysql

#******** Setting akun Database ********#
host_db = 'localhost'
user_db = 'basyair7'
passwd_db = '0712'
nama_db = 'uji_coba'
#**************************************#

# Koneksi database ke xampp
account = mysql.connect(
    host=host_db,
    user=user_db,
    passwd=passwd_db,
)

# Buat kursor
cursor = account.cursor()
# Buat database
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nama_db}")
# Tutup database
account.close()

# Koneksi database ke xampp untuk membuat table
db = mysql.connect(
    host=host_db,
    user=user_db,
    passwd=passwd_db,
    database=nama_db
)

c = db.cursor()
# Buat table admin
# admin_id INT AUTO_INCREMENT PRIMARY KEY
admin = """CREATE TABLE IF NOT EXISTS admin(
    admin_id INT PRIMARY KEY,
    admin_name VARCHAR(255),
    address VARCHAR(255)
)
"""

# Buat table users
users = """CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY,
    user_name VARCHAR(255),
    address VARCHAR(255)
)
"""
# Execute table
c.execute(admin)
c.execute(users)

print("Update Data Databases")
print("1. Admin")
print("2. Users")
pilih = int(input(" Pilihan : "))

if (pilih == 1):
    # Masukkan data admin
    print("Update Data Admin")
    adm_id = int(input("Masukkan ID auto : "))
    adm_name = str(input("Masukkan Nama admin : "))
    adm_address = str(input("Masukkan alamat : "))

    # Update data di Database
    sql_adm = "UPDATE admin SET admin_name=%s, address=%s WHERE admin_id=%s"
    val_adm = (f"{adm_name}", f"{adm_address}", f"{adm_id}")

    # Execute data
    c.execute(sql_adm, val_adm)
    # Commit
    db.commit()
    # Done
    print(f"{c.rowcount} data diupdate")

elif (pilih == 2):
    # Masukkan data user
    print("Update Data User")
    usr_id = int(input("Masukkan ID auto : "))
    usr_name = str(input("Masukkan Nama user : "))
    usr_address = str(input("Masukkan alamat : "))

    # Update data di Database
    sql_usr = "UPDATE users SET user_name=%s, address=%s WHERE user_id=%s"
    val_usr = (f"{usr_name}", f"{usr_address}", f"{usr_id}")

    # Execute data
    c.execute(sql_usr, val_usr)
    # Commit
    db.commit()
    # Done
    print(f"{c.rowcount} data diupdate")

else:
    print("Pilihan tidak ada")
