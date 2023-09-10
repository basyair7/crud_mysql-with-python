import mysql.connector as mysql

#******** Setting akun Database ********#
host_db = 'localhost'
user_db = ''
passwd_db = ''
nama_db = 'uji_coba'

#**************************************#

# koneksi database ke xampp
account = mysql.connect(
    host=host_db,
    user=user_db,
    passwd=passwd_db
)
cursor = account.cursor()

# Buat database
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nama_db}")

# Tutup database
account.close()

# koneksi database ke xampp untuk membuat table
db = mysql.connect(
    host=host_db,
    user=user_db,
    passwd=passwd_db,
    database=nama_db
)

c = db.cursor()
# Buat table admin
admin = """CREATE TABLE IF NOT EXISTS admin (
    admin_id INT PRIMARY KEY,
    admin_name VARCHAR(255),
    address VARCHAR(255)
)
"""
c.execute(admin)

# Buat table users
users = """CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(255),
    address VARCHAR(255)
)
"""
c.execute(users)

# Masukkan nama admin
adm_id = int(input("Masukkan id admin : "))
adm_name = str(input("Masukkan Nama admin : "))
adm_address = str(input("Masukkan alamat : "))

# Masukkan nama users
print("\n")
usr_id = int(input("Masukkan id user : "))
usr_name = str(input("Masukkan nama user : "))
usr_address = str(input("Masukkan alamat : "))

# Input data ke database
sql_adm = "INSERT INTO admin (admin_id, admin_name, address) VALUES (%s, %s, %s)"
val_adm = (f"{adm_id}", f"{adm_name}", f"{adm_address}")
sql_user = "INSERT INTO users (user_id, user_name, address) VALUES (%s, %s, %s)"
val_user = (f"{usr_id}", f"{usr_name}", f"{usr_address}")

# Execute data
c.execute(sql_adm, val_adm)
c.execute(sql_user, val_user)

# commit
db.commit()

# Done
print(f"{c.rowcount} data ditambah")

# close
db.close()
