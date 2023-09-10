import mysql.connector as mysql

#******** Setting akun Database ********#
host_db = 'localhost'
user_db = ''
passwd_db = ''
nama_db = 'uji_coba'
#**************************************#

def drop_db():
    # Koneksi database ke xampp
    db = mysql.connect(
        host=host_db,
        user=user_db,
        passwd=passwd_db,
    )
    c = db.cursor()

    # Hapus database
    del_db = f"DROP DATABASE IF EXISTS {nama_db};"
    c.execute(del_db)
    db.commit()
    print("Database telah dihapus")
    db.close()

def drop_table():
    try:
        # Koneksi database ke xampp
        db = mysql.connect(
            host=host_db,
            user=user_db,
            passwd=passwd_db,
            database=nama_db
        )
        c = db.cursor()

        print("\n1. Hapus table admin\n2. Hapus Table users")
        pilih = int(input(" Pilihan : "))

        if (pilih == 1):
            del_admin = "DROP TABLE IF EXISTS admin;"
            c.execute(del_admin)
            db.commit()
            print("Table admin telah dihapus")
            db.close()
        elif (pilih == 2):
            del_usr = "DROP TABLE IF EXISTS users;"
            c.execute(del_usr)
            db.commit()
            print("Table users telah dihapus")
            db.close()
        else:
            print("Pilihan tidak ada...")

    except:
        print("Error!!!")

print("Hapus Data Database")
print("1. Hapus Database\n2. Hapus Table")
pilih = int(input(" Pilihan : "))

if (pilih == 1):
    drop_db()
elif (pilih == 2):
    drop_table()
else:
    print("Pilihan tidak ada... ")
