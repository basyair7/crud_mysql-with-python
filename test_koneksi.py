import mysql.connector as mysql

#******** Setting akun Database ********#
host_db = 'localhost'
user_db = ''
passwd_db = ''

#**************************************#

# Koneksi database ke xampp
db = mysql.connect(
  host=host_db,
  user=user_db,
  passwd=passwd_db
)

# Jika terhubung
if db.is_connected():
  print("Berhasil terhubung ke database")

# Jika gagal terhubung
else:
    print("Gagal terhubung ke database")

# close
db.close()
