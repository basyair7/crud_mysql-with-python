import mysql.connector as mysql


#******** Setting akun Database ********#
host_db = 'localhost'
user_db = ''
passwd_db = ''
nama_db = 'uji_coba'

#**************************************#

# Koneksi database ke xampp
database = mysql.connect(
    host=host_db,
    user=user_db,
    passwd=passwd_db
)
c = database.cursor()


# Buat databases
c.execute(f"CREATE DATABASE IF NOT EXISTS {nama_db}")
print("Database berhasil dibuat ")

"""
# Hapus databases
c.execute("DROP DATABASE IF EXISTS uji_coba")
print("Database berhasil dihapus ")
"""

# Tampilkan semua databases

c.execute("SHOW DATABASES;")

for db in c:
    print(db)

# Tutup database
database.close()
