import mysql.connector as mysql
import os
import sys
import time

#******** Setting akun Database ********#
host_db = 'localhost'
user_db = ''
passwd_db = ''
nama_db = 'Data_Kelas'
#**************************************#

def database():
    # koneksi database ke xampp
    account = mysql.connect(
        host=host_db,
        user=user_db,
        passwd=passwd_db
    )
    cursor_1 = account.cursor()

    # Buat database baru
    new_db = f"CREATE DATABASE IF NOT EXISTS {nama_db};"
    cursor_1.execute(new_db)
    # Commit
    account.commit()
    # Tutup database
    account.close()

    # koneksi database ke xampp untuk buat table baru
    db = mysql.connect(
        host=host_db,
        user=user_db,
        passwd=passwd_db,
        database=nama_db
    )

    cursor_2 = db.cursor()

    # Buat table kelas 11 untuk data dosen
    kelas_1_dsn = """CREATE TABLE IF NOT EXISTS kelas_1_dsn (
        kode_mk VARCHAR(255),
        nama_mk VARCHAR(255),
        kelas INT,
        sks INT,
        nip_dosen BIGINT PRIMARY KEY,
        nama_dosen VARCHAR(255)
    )
    """
    # Buat table kelas 12 untuk data dosen
    kelas_2_dsn = """CREATE TABLE IF NOT EXISTS kelas_2_dsn (
        kode_mk VARCHAR(255),
        nama_mk VARCHAR(255),
        kelas INT,
        sks INT,
        nip_dosen BIGINT PRIMARY KEY,
        nama_dosen VARCHAR(255)
    )
    """

    # Buat table kelas 11 untuk data mahasiswa
    kelas_1_mhs = """CREATE TABLE IF NOT EXISTS kelas_1_mhs (
        kode_mk VARCHAR(255),
        nama_mk VARCHAR(255),
        kelas INT,
        sks INT,
        npm_mhs BIGINT PRIMARY KEY,
        nama_mhs VARCHAR(255)
    )
    """
    # Buat table kelas 12 untuk data mahasiswa
    kelas_2_mhs = """CREATE TABLE IF NOT EXISTS kelas_2_mhs (
        kode_mk VARCHAR(255),
        nama_mk VARCHAR(255),
        kelas INT,
        sks INT,
        npm_mhs BIGINT PRIMARY KEY,
        nama_mhs VARCHAR(255)
    )
    """

    # Execute table
    cursor_2.execute(kelas_1_dsn); cursor_2.execute(kelas_2_dsn)
    cursor_2.execute(kelas_1_mhs); cursor_2.execute(kelas_2_mhs)
    # Commit
    db.commit()
    # tutup database
    db.close()

def tambah_data():
    try:
        cls_terminal()
        print("\nTambah Data Kelas")
        print("1. Kelas 1\n2. Kelas 2\n3. Kembali")
        pilih = input(" Pilih kelas : ")
        if(pilih == '1'):
            cls_terminal()
            print("\nTambah data kelas 1")
            print("1. Tambah data dosen\n2. Tambah data mahasiswa\n3. Kembali")
            pilihan = input("   Pilihan : ")

            if(pilihan == '1'):
                print("\nTambah Data Dosen Kelas 1")
                # Koneksi db ke xampp
                db = mysql.connect(
                    host=host_db,
                    user=user_db,
                    passwd=passwd_db,
                    database=nama_db
                )
                c = db.cursor()

                kode_mk = str(input("Masukan Kode MK\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t: "))
                kls_mk = int(input("Masukan Kelas MK\t: "))
                sks_mk = int(input("Masukan SKS MK\t\t: "))
                nama_dosen = str(input("Masukan Nama Dosen\t: "))
                nip_dosen = int(input("Masukan NIP Dosen\t: "))

                # Input data ke database
                sql_dsn1 = "INSERT INTO kelas_1_dsn (kode_mk, nama_mk, kelas, sks, nip_dosen, nama_dosen) VALUES (%s, %s, %s, %s, %s, %s)"
                val_dsn1 = (f"{kode_mk}", f"{nama_mk}", f"{kls_mk}", f"{sks_mk}", f"{nip_dosen}", f"{nama_dosen}")
                # execute data
                c.execute(sql_dsn1, val_dsn1)
                # commit
                db.commit()
                # Done
                print(f"{c.rowcount} Data ditambah...")
                # Tutup database
                db.close()

            elif(pilihan == '2'):
                print("\nTambah Data Mahasiswa Kelas 1")
                # Koneksi db ke xampp
                db = mysql.connect(
                    host=host_db,
                    user=user_db,
                    passwd=passwd_db,
                    database=nama_db
                )
                c = db.cursor()

                kode_mk = str(input("Masukan Kode MK\t\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t\t: "))
                kls_mk = int(input("Masukan Kelas MK\t\t: "))
                sks_mk = int(input("Masukan SKS MK\t\t\t: "))
                nama_mhs = str(input("Masukan Nama Mahasiswa\t\t: "))
                npm_mhs = int(input("Masukan Nomor Induk Mahasiswa\t: "))

                # Input data ke database
                sql_mhs1 = "INSERT INTO kelas_1_mhs (kode_mk, nama_mk, kelas, sks, npm_mhs, nama_mhs) VALUES (%s, %s, %s, %s, %s, %s)"
                val_mhs1 = (f"{kode_mk}", f"{nama_mk}", f"{kls_mk}", f"{sks_mk}", f"{npm_mhs}", f"{nama_mhs}")
                # execute data
                c.execute(sql_mhs1, val_mhs1)
                # commit
                db.commit()
                # done
                print(f"{c.rowcount} Data ditambah...")
                # Tutup database
                db.close()

            elif(pilihan == '3'):
                cls_terminal()
                tambah_data()

            else:
                print("Pilihan tidak ada....")
                time.sleep(1)
                tambah_data()

        elif(pilih == '2'):
            cls_terminal()
            print("Tambah data kelas 2")
            print("1. Tambah data dosen\n2. Tambah data mahasiswa\n3. Kembali")
            pilihan = input("   Pilihan : ")

            if(pilihan == '1'):
                print("\nTambah Data Dosen Kelas 2")
                # Koneksi db ke xampp
                db = mysql.connect(
                    host=host_db,
                    user=user_db,
                    passwd=passwd_db,
                    database=nama_db
                )
                c = db.cursor()

                kode_mk = str(input("Masukan Kode MK\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t: "))
                kls_mk = int(input("Masukan Kelas MK\t: "))
                sks_mk = int(input("Masukan SKS MK\t\t: "))
                nama_dosen = str(input("Masukan Nama Dosen\t: "))
                nip_dosen = int(input("Masukan NIP Dosen\t: "))

                # Input data ke database
                sql_dsn2 = "INSERT INTO kelas_2_dsn (kode_mk, nama_mk, kelas, sks, nip_dosen, nama_dosen) VALUES (%s, %s, %s, %s, %s, %s)"
                val_dsn2 = (f"{kode_mk}", f"{nama_mk}", f"{kls_mk}", f"{sks_mk}", f"{nip_dosen}", f"{nama_dosen}")
                # execute data
                c.execute(sql_dsn2, val_dsn2)
                # commit
                db.commit()
                # Done
                print(f"{c.rowcount} Data ditambah...")
                # Tutup database
                db.close()

            elif(pilihan == '2'):
                print("\nTambah Data Mahasiswa Kelas 2")
                # Koneksi db ke xampp
                db = mysql.connect(
                    host=host_db,
                    user=user_db,
                    passwd=passwd_db,
                    database=nama_db
                )
                c = db.cursor()

                kode_mk = str(input("Masukan Kode MK\t\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t\t: "))
                kls_mk = int(input("Masukan Kelas MK\t\t: "))
                sks_mk = int(input("Masukan SKS\t\t\t: "))
                nama_mhs = str(input("Masukan Nama Mahasiswa\t\t: "))
                npm_mhs = int(input("Masukan Nomor Induk Mahasiswa\t: "))

                # Input data ke database
                sql_mhs2 = "INSERT INTO kelas_2_mhs (kode_mk, nama_mk, kelas, sks, npm_mhs, nama_mhs) VALUES (%s, %s, %s, %s, %s, %s)"
                val_mhs2 = (f"{kode_mk}", f"{nama_mk}", f"{kls_mk}", f"{sks_mk}", f"{npm_mhs}", f"{nama_mhs}")
                # execute data
                c.execute(sql_mhs2, val_mhs2)
                # commit
                db.commit()
                # done
                print(f"{c.rowcount} Data ditambah...")
                # Tutup database
                db.close()

            elif (pilihan == '3'):
                cls_terminal()
                tambah_data()

            else:
                print("Pilihan tidak ada....")
                time.sleep(1)
                tambah_data()

        else:
            time.sleep(1)
            cls_terminal()
    except:
        print("Error.. Input Harus Berupa Angka !")
        time.sleep(1)
        cls_terminal()

def tampilkan_data():
    try:
        cls_terminal()
        print("\nTampilkan Data Kelas")
        print("1. Kelas 1\n2. Kelas 2\n3. Kembali")
        pilih = int(input(" Pilihan : "))

        if(pilih == 1):
            cls_terminal()
            print("\nTampilkan Data Kelas 1 ")
            print('1. Dosen\n2. Mahasiswa\n3. Kembali')
            pilihan = int(input("   Pilihan : "))

            if(pilihan == 1):
                # Koneksi db ke xampp
                db = mysql.connect(
                    host=host_db,
                    user=user_db,
                    passwd=passwd_db,
                    database=nama_db
                )
                c = db.cursor()
                cls_terminal()
                print("\nData Dosen...")
                # Tampilkan semua data table dosen
                sql_dsn1 = "SELECT * FROM kelas_1_dsn"
                c.execute(sql_dsn1)
                results1 = c.fetchall()
                list_data1 = ""

                for data in results1:
                    list_data1 += f"\n\nKode MK\t\t: {data[0]} \nNama MK\t\t: {data[1]} \nKelas\t\t: {data[2]} \nSKS\t\t: {data[3]} \nNama Dosen\t: {data[5]} \nNIP Dosen\t: {data[4]}"

                print(list_data1)
                # Tutup database
                db.close()

            elif(pilihan == 2):
                # Koneksi db ke xampp
                db = mysql.connect(
                    host=host_db,
                    user=user_db,
                    passwd=passwd_db,
                    database=nama_db
                )
                c = db.cursor()
                cls_terminal()
                print("\nData mahasiswa...")
                # Tampilkan semua data table mhs
                sql_mhs1 = "SELECT * FROM kelas_1_mhs"
                c.execute(sql_mhs1)
                results2 = c.fetchall()
                list_data2 = ""

                for data in results2:
                    list_data2 += f"\n\nKode MK\t\t: {data[0]} \nNama MK\t\t: {data[1]} \nKelas\t\t: {data[2]} \nSKS\t\t: {data[3]} \nNama Mahasiswa\t: {data[5]} \nNPM\t\t: {data[4]}"

                print(list_data2)
                # Tutup database
                db.close()

            elif (pilihan == 3):
                cls_terminal()
                tampilkan_data()

            else:
                print("Pilihan tidak ada...")
                tampilkan_data()

        elif(pilih == 2):
            cls_terminal()
            print("\nTampilkan Data Kelas 2 ")
            print('1. Dosen\n2. Mahasiswa\n3. Kembali')
            pilihan = int(input("   Pilihan : "))

            if(pilihan == 1):
                # Koneksi db ke xampp
                db = mysql.connect(
                    host=host_db,
                    user=user_db,
                    passwd=passwd_db,
                    database=nama_db
                )
                c = db.cursor()
                cls_terminal()
                print("\nData Dosen...")
                # Tampilkan semua data table dosen
                sql_dsn2 = "SELECT * FROM kelas_2_dsn"
                c.execute(sql_dsn2)
                results3 = c.fetchall()
                list_data3 = ""

                for data in results3:
                    list_data3 += f"\n\nKode MK\t\t: {data[0]} \nNama MK\t\t: {data[1]} \nKelas\t\t: {data[2]} \nSKS\t\t: {data[3]} \nNama Dosen\t: {data[5]} \nNIP Dosen\t: {data[4]}"

                print(list_data3)
                # Tutup database
                db.close()

            elif(pilihan == 2):
                # Koneksi db ke xampp
                db = mysql.connect(
                    host=host_db,
                    user=user_db,
                    passwd=passwd_db,
                    database=nama_db
                )
                c = db.cursor()
                cls_terminal()
                print("\nData mahasiswa...")
                # Tampilkan semua data table mhs
                sql_mhs2 = "SELECT * FROM kelas_2_mhs"
                c.execute(sql_mhs2)
                results4 = c.fetchall()
                list_data4 = ""

                for data in results4:
                    list_data4 += f"\n\nKode MK\t\t: {data[0]} \nNama MK\t\t: {data[1]} \nKelas\t\t: {data[2]} \nSKS\t\t: {data[3]} \nNama Mahasiswa\t: {data[5]} \nNPM\t\t: {data[4]}"

                print(list_data4)
                # Tutup database
                db.close()

            elif (pilihan == 3):
                cls_terminal()
                tampilkan_data()

            else:
                print("Pilihan tidak ada...")
                time.sleep(1)
                tambah_data()

        else:
            time.sleep(1)
            cls_terminal()

    except:
        print("Error.. Input Harus Berupa Angka !")
        time.sleep(1)
        cls_terminal()

def update_data():
    try:
        cls_terminal()
        print("\nUpdate Data Kelas")
        print("1. Kelas 1\n2. Kelas 2\n3. Kembali")
        pilih = input(" Pilih kelas : ")

        if (pilih == '1'):
            cls_terminal()
            print("Update Data Kelas 1 ")
            print('1. Dosen\n2. Mahasiswa\n3. Kembali')
            pilihan = input("   Pilihan : ")

            if (pilihan == '1'):
                print("\nUpdate Data Dosen Kelas 1")
                # Koneksi db ke xampp
                db = mysql.connect(
                    host=host_db,
                    user=user_db,
                    passwd=passwd_db,
                    database=nama_db
                )
                c = db.cursor()

                kode_mk = str(input("Masukan Kode MK\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t: "))
                kelas_mk = int(input("Masukan Kelas MK\t: "))
                sks_mk = int(input("Masukan SKS MK\t\t: "))
                nama_dosen = str(input("Masukan Nama Dosen\t: "))
                nip_dosen = int(input("Masukan NIP Dosen\t: "))

                # Update database
                sql_dsn1 = "UPDATE kelas_1_dsn SET kode_mk=%s, nama_mk=%s, kelas=%s, sks=%s, nama_dosen=%s Where nip_dosen=%s"
                val_dsn1 = (f"{kode_mk}", f"{nama_mk}", f"{kelas_mk}", f"{sks_mk}", f"{nama_dosen}", f"{nip_dosen}")

                # Execute data
                c.execute(sql_dsn1, val_dsn1)
                # Commit
                db.commit()
                # Done
                print(f"{c.rowcount} data diupdate")

            elif (pilihan == '2'):
                print("\nUpdate Data Mahasiswa Kelas 1")
                # Koneksi db ke xampp
                db = mysql.connect(
                    host=host_db,
                    user=user_db,
                    passwd=passwd_db,
                    database=nama_db
                )
                c = db.cursor()

                kode_mk = str(input("Masukan Kode MK\t\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t\t: "))
                kelas_mk = int(input("Masukan Kelas MK\t\t: "))
                sks_mk = int(input("Masukan SKS MK\t\t\t: "))
                nama_mhs = str(input("Masukan Nama Mahasiswa\t\t: "))
                npm_mhs = int(input("Masukan Nomor Induk Mahasiswa\t: "))

                # Update database
                sql_mhs1 = "UPDATE kelas_1_mhs SET kode_mk=%s, nama_mk=%s, kelas=%s, sks=%s, nama_mhs=%s Where npm_mhs=%s"
                val_mhs1 = (f"{kode_mk}", f"{nama_mk}", f"{kelas_mk}", f"{sks_mk}", f"{nama_mhs}", f"{npm_mhs}")

                # Execute data
                c.execute(sql_mhs1, val_mhs1)
                # Commit
                db.commit()
                # Done
                print(f"{c.rowcount} data diupdate")

            elif(pilihan == '3'):
                cls_terminal()
                update_data()

            else:
                print("Pilihan Tidak ada...")
                time.sleep(1)
                update_data()

        elif (pilih == '2'):
            cls_terminal()
            print("Update Data Kelas 2 ")
            print('1. Dosen\n2. Mahasiswa\n3. Kembali')
            pilihan = input("   Pilihan : ")

            if (pilihan == '1'):
                print("\nUpdate Data Dosen Kelas 2")
                # Koneksi db ke xampp
                db = mysql.connect(
                    host=host_db,
                    user=user_db,
                    passwd=passwd_db,
                    database=nama_db
                )
                c = db.cursor()

                kode_mk = str(input("Masukan Kode MK\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t: "))
                kelas_mk = int(input("Masukan Kelas MK\t: "))
                sks_mk = int(input("Masukan SKS MK\t\t: "))
                nama_dosen = str(input("Masukan Nama Dosen\t: "))
                nip_dosen = int(input("Masukan NIP Dosen\t: "))

                # Update database
                sql_dsn2 = "UPDATE kelas_2_dsn SET kode_mk=%s, nama_mk=%s, kelas=%s, sks=%s, nama_dosen=%s Where nip_dosen=%s"
                val_dsn2 = (f"{kode_mk}", f"{nama_mk}", f"{kelas_mk}", f"{sks_mk}", f"{nama_dosen}", f"{nip_dosen}")

                # Execute data
                c.execute(sql_dsn2, val_dsn2)
                # Commit
                db.commit()
                # Done
                print(f"{c.rowcount} data diupdate")

            elif (pilihan == '2'):
                print("\nUpdate Data Mahasiswa Kelas 2")
                # Koneksi db ke xampp
                db = mysql.connect(
                    host=host_db,
                    user=user_db,
                    passwd=passwd_db,
                    database=nama_db
                )
                c = db.cursor()

                kode_mk = str(input("Masukan Kode MK\t\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t\t: "))
                kelas_mk = int(input("Masukan Kelas MK\t\t: "))
                sks_mk = int(input("Masukan SKS MK\t\t\t: "))
                nama_mhs = str(input("Masukan Nama Mahasiswa\t\t: "))
                npm_mhs = int(input("Masukan Nomor Induk Mahasiswa\t: "))

                # Update database
                sql_mhs2 = "UPDATE kelas_2_mhs SET kode_mk=%s, nama_mk=%s, kelas=%s, sks=%s, nama_mhs=%s Where npm_mhs=%s"
                val_mhs2 = (f"{kode_mk}", f"{nama_mk}", f"{kelas_mk}", f"{sks_mk}", f"{nama_mhs}", f"{npm_mhs}")

                # Execute data
                c.execute(sql_mhs2, val_mhs2)
                # Commit
                db.commit()
                # Done
                print(f"{c.rowcount} data diupdate")

            elif (pilihan == '3'):
                cls_terminal()
                update_data()

            else:
                print("Pilihan Tidak ada...")
                time.sleep(1)
                update_data()

        else:
            time.sleep(1)
            cls_terminal()

    except:
        print("Error.. Input Harus Berupa Angka !")
        time.sleep(1)
        cls_terminal()

def delete_data():
    try:
        cls_terminal()
        print("\nHapus Data Kelas")
        print("1. Kelas 1\n2. Kelas 2\n3. Hapus Semua Databases\n4. Kembali")
        pilih = input(" Pilihan : ")

        if (pilih == '1'):
            cls_terminal()
            print("Hapus Data kelas 1")
            print("1. Data Dosen\n2. Data Mahasiswa\n3. Kembali")
            pilihan = input("   Pilihan : ")

            if (pilihan == '1'):
                print("\nHapus Semua Data Dosen Kelas 1? ")
                ask = str(input(" Y or N : "))
                if (ask == 'Y' or ask == 'y'):
                    try:
                        # Koneksi db ke xampp
                        db = mysql.connect(
                            host=host_db,
                            user=user_db,
                            passwd=passwd_db,
                            database=nama_db
                        ); c = db.cursor()

                        del_table_dsn_11 = "DROP TABLE IF EXISTS kelas_1_dsn;"
                        c.execute(del_table_dsn_11)
                        db.commit()
                        db.close()
                        print("Semua Data Dosen Kelas 1 Telah Dihapus...")
                        database()

                    except:
                        print("ERROR !!!")
                        time.sleep(1)
                        cls_terminal()

                else:
                    cls_terminal()

            elif (pilihan == '2'):
                print("\nHapus Semua Data Mahasiswa Kelas 1? ")
                ask = str(input(" Y or N : "))
                if(ask == 'Y' or ask == 'y'):
                    try:
                        # Koneksi db ke xampp
                        db = mysql.connect(
                            host=host_db,
                            user=user_db,
                            passwd=passwd_db,
                            database=nama_db
                        ); c = db.cursor()

                        del_table_mhs_11 = "DROP TABLE IF EXISTS kelas_1_mhs;"
                        c.execute(del_table_mhs_11)
                        db.commit()
                        db.close()
                        print("Semua Data Mahasiswa Kelas 1 Telah Dihapus...")
                        database()

                    except:
                        print("ERROR !!!")
                        time.sleep(1)
                        cls_terminal()
                else:
                    cls_terminal()

            elif(pilihan == '3'):
                cls_terminal(); delete_data()

            else:
                print("\nPilihan Tidak Ada...")
                time.sleep(1)
                cls_terminal()

        elif (pilih == '2'):
            cls_terminal()
            print("Hapus Data kelas 2")
            print("1. Data Dosen\n2. Data Mahasiswa\n3. Kembali")
            pilihan = input("   Pilihan : ")

            if (pilihan == '1'):
                print("\nHapus Semua Data Dosen Kelas 2? ")
                ask = str(input(" Y or N : "))
                if (ask == 'Y' or ask == 'y'):
                    try:
                        # Koneksi db ke xampp
                        db = mysql.connect(
                            host=host_db,
                            user=user_db,
                            passwd=passwd_db,
                            database=nama_db
                        ); c = db.cursor()

                        del_table_dsn_11 = "DROP TABLE IF EXISTS kelas_2_dsn;"
                        c.execute(del_table_dsn_11)
                        db.commit()
                        db.close()
                        print("Semua Data Dosen Kelas 2 Telah Dihapus...")
                        database()

                    except:
                        print("ERROR !!!")
                        time.sleep(1)
                        cls_terminal()
                else:
                    cls_terminal()

            elif (pilihan == '2'):
                print("\nHapus Semua Data Mahasiswa Kelas 2? ")
                ask = str(input(" Y or N : "))
                if(ask == 'Y' or ask == 'y'):
                    try:
                        # Koneksi db ke xampp
                        db = mysql.connect(
                            host=host_db,
                            user=user_db,
                            passwd=passwd_db,
                            database=nama_db
                        ); c = db.cursor()

                        del_table_mhs_11 = "DROP TABLE IF EXISTS kelas_2_mhs;"
                        c.execute(del_table_mhs_11)
                        db.commit()
                        db.close()
                        print("Semua Data Mahasiswa Kelas 2 Telah Dihapus...")
                        database()

                    except:
                        print("ERROR !!!")
                        time.sleep(1)
                        cls_terminal()

                else:
                    cls_terminal()

            elif(pilihan == '3'):
                cls_terminal(); delete_data()

            else:
                print("\nPilihan Tidak Ada...")
                time.sleep(1)
                cls_terminal()

        elif (pilih == '3'):
            cls_terminal()
            print("Hapus Semua Database Kelas? ")
            ask = str(input(" Y or N : "))

            if(ask == 'Y' or ask == 'y'):
                # Koneksi db ke xampp
                db = mysql.connect(
                    host=host_db,
                    user=user_db,
                    passwd=passwd_db,
                ); c = db.cursor()

                del_db = f"DROP DATABASE IF EXISTS {nama_db};"
                c.execute(del_db)
                db.commit()
                db.close()
                print("\nDatabase Telah Dihapus...")
                time.sleep(1)
                cls_terminal()
                database()

            else:
                cls_terminal()

        elif(pilih == '4'):
            cls_terminal()

        else:
            print("\nPilihan Tidak Ada...")
            time.sleep(1)
            cls_terminal()

    except:
        print("Error.. Input Harus Berupa Angka !")
        time.sleep(1)
        cls_terminal()

def cls_terminal():
    if (sys.platform.startswith('win')):
        os.system('cls')
    else:
        os.system('clear')

def main():
    cls_terminal()
    database()
    while True:
        print("\n\nAplikasi CRUD Kelas")
        print("Versi 0.1")
        print("\n1. Tambah Data Kelas\n2. Tampilkan Data Kelas\n3. Update/Ubah Data\n4. Hapus Data\n5. Keluar\n")
        pilih = input(" Pilihan : ")

        if(pilih == '1'):
            tambah_data()
        elif(pilih == '2'):
            tampilkan_data()
        elif(pilih == '3'):
            update_data()
        elif(pilih == '4'):
            delete_data()
        elif(pilih == '5'):
            cls_terminal()
            print("\nKeluar dari program...")
            time.sleep(1)
            sys.exit()
        else:
            cls_terminal()
            print("\nPilihan Tidak Ada...")
            time.sleep(1)

if __name__ == "__main__":
    main()
