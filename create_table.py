import mysql.connector as mysql

#******** Setting akun Database ********#
host_db = 'localhost'
user_db = 'basyair7'
passwd_db = '0712'
nama_db = 'uji_coba'
#**************************************#

# koneksi database ke xampp
db = mysql.connect(
    host=host_db,
    user=user_db,
    passwd=passwd_db,
    database=nama_db
)

c = db.cursor()
# Buat table admin
admin = """CREATE TABLE IF NOT EXISTS admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255)
)
"""
c.execute(admin)

# Buat table user
user = """CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255)
)
"""
c.execute(user)
print("Table berhasil dibuat")

# Tampilkan hasil
c.execute("SHOW COLUMNS FROM user")
print("\nTampilkan table user")
for table in c:
    print(table)

c.execute("SHOW COLUMNS FROM admin")
print("\nTampilkan table admin")
for table in c:
    print(table)


"""
# Hapus table
c.execute("DROP TABLE IF EXISTS admin")
print("Table *admin* sudah dihapus..")
c.execute("DROP TABLE IF EXISTS user")
print("\nTable *user* sudah dihapus..")
"""
