from mysql_db import *
import os
import sys
import time

#******** Setting akun Database ********#
host_db = 'localhost'
user_db = 'basyair7'
passwd_db = '0712'

nama_db = 'Data_Kelas'
tb_11 = 'Kalkulus_Dsn'
tb_12 = 'Kalkulus_Mhs'
tb_21 = 'Pemrograman_2_Dsn'
tb_22 = 'Pemrograman_2_Mhs'

#**************************************#

def database():
    # koneksi database ke xampp
    db = db_connect(host_db, user_db, passwd_db, nama_db)
    db.create_db() # Buat Database
    # Buat Table
    db.create_table('table_1_dsn',tb_11)
    db.create_table('table_1_mhs',tb_12)
    db.create_table('table_2_dsn',tb_21)
    db.create_table('table_2_mhs',tb_22)

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
                db = db_connect(host_db, user_db, passwd_db, nama_db)
                # Take input
                kode_mk = str(input("Masukan Kode MK\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t: "))
                kls_mk = int(input("Masukan Kelas MK\t: "))
                sks_mk = int(input("Masukan SKS MK\t\t: "))
                nama_dosen = str(input("Masukan Nama Dosen\t: "))
                nip_dosen = int(input("Masukan NIP Dosen\t: "))

                # Input data ke database
                db.input_1_dsn(kode_mk, nama_mk, kls_mk, sks_mk, nip_dosen, nama_dosen, 'input', tb_11)
                time.sleep(3)
                cls_terminal()

            elif(pilihan == '2'):
                print("\nTambah Data Mahasiswa Kelas 1")
                # Koneksi db ke xampp
                db = db_connect(host_db, user_db, passwd_db, nama_db)
                # Take input
                kode_mk = str(input("Masukan Kode MK\t\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t\t: "))
                kls_mk = int(input("Masukan Kelas MK\t\t: "))
                sks_mk = int(input("Masukan SKS MK\t\t\t: "))
                nama_mhs = str(input("Masukan Nama Mahasiswa\t\t: "))
                npm_mhs = int(input("Masukan Nomor Induk Mahasiswa\t: "))

                # Input data ke database
                db.input_1_mhs(kode_mk, nama_mk, kls_mk, sks_mk, npm_mhs, nama_mhs, 'input', tb_12)
                time.sleep(3)
                cls_terminal()

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
                db = db_connect(host_db, user_db, passwd_db, nama_db)
                # Take Input
                kode_mk = str(input("Masukan Kode MK\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t: "))
                kls_mk = int(input("Masukan Kelas MK\t: "))
                sks_mk = int(input("Masukan SKS MK\t\t: "))
                nama_dosen = str(input("Masukan Nama Dosen\t: "))
                nip_dosen = int(input("Masukan NIP Dosen\t: "))

                # Input data ke database
                db.input_2_dsn(kode_mk, nama_mk, kls_mk, sks_mk, nip_dosen, nama_dosen, 'input', tb_21)
                time.sleep(3)
                cls_terminal()

            elif(pilihan == '2'):
                print("\nTambah Data Mahasiswa Kelas 2")
                # Koneksi db ke xampp
                db = db_connect(host_db, user_db, passwd_db, nama_db)

                kode_mk = str(input("Masukan Kode MK\t\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t\t: "))
                kls_mk = int(input("Masukan Kelas MK\t\t: "))
                sks_mk = int(input("Masukan SKS\t\t\t: "))
                nama_mhs = str(input("Masukan Nama Mahasiswa\t\t: "))
                npm_mhs = int(input("Masukan Nomor Induk Mahasiswa\t: "))

                # Input data ke database
                db.input_2_mhs(kode_mk, nama_mk, kls_mk, sks_mk, npm_mhs, nama_mhs, 'input', tb_22)
                time.sleep(3)
                cls_terminal()

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
                cls_terminal()
                db = db_connect(host_db, user_db, passwd_db, nama_db)
                # Tampilkan semua data table dosen
                db.show_data('table_1_dsn', tb_11)
                # Kembali
                back = input("Tekan Y untuk kembali : ")
                if (back == 'Y' or back == 'y'):
                    main()

            elif(pilihan == 2):
                # Koneksi db ke xampp
                cls_terminal()
                db = db_connect(host_db, user_db, passwd_db, nama_db)
                # Tampilkan semua data table dosen
                db.show_data('table_1_mhs', tb_12)
                # Kembali
                back = input("Tekan Y untuk kembali : ")
                if (back == 'Y' or back == 'y'):
                    main()

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
                cls_terminal()
                db = db_connect(host_db, user_db, passwd_db, nama_db)
                # Tampilkan semua data table dosen
                db.show_data('table_2_dsn', tb_21)
                # Kembali
                back = input("Tekan Y untuk kembali : ")
                if (back == 'Y' or back == 'y'):
                    main()

            elif(pilihan == 2):
                # Koneksi db ke xampp
                cls_terminal()
                db = db_connect(host_db, user_db, passwd_db, nama_db)
                # Tampilkan semua data table dosen
                db.show_data('table_2_mhs', tb_22)
                # Kembali
                back = input("Tekan Y untuk kembali : ")
                if (back == 'Y' or back == 'y'):
                    main()

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
                db = db_connect(host_db, user_db, passwd_db, nama_db)

                kode_mk = str(input("Masukan Kode MK\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t: "))
                kelas_mk = int(input("Masukan Kelas MK\t: "))
                sks_mk = int(input("Masukan SKS MK\t\t: "))
                nama_dosen = str(input("Masukan Nama Dosen\t: "))
                nip_dosen = int(input("Masukan NIP Dosen\t: "))

                # Update database
                db.input_1_dsn(kode_mk, nama_mk, kelas_mk, sks_mk, nip_dosen, nama_dosen, 'update', tb_11)
                time.sleep(3)
                cls_terminal

            elif (pilihan == '2'):
                print("\nUpdate Data Mahasiswa Kelas 1")
                # Koneksi db ke xampp
                db = db_connect(host_db, user_db, passwd_db, nama_db)

                kode_mk = str(input("Masukan Kode MK\t\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t\t: "))
                kelas_mk = int(input("Masukan Kelas MK\t\t: "))
                sks_mk = int(input("Masukan SKS MK\t\t\t: "))
                nama_mhs = str(input("Masukan Nama Mahasiswa\t\t: "))
                npm_mhs = int(input("Masukan Nomor Induk Mahasiswa\t: "))

                # Update database
                db.input_1_mhs(kode_mk, nama_mk, kelas_mk, sks_mk, npm_mhs, nama_mhs, 'update', tb_12)
                time.sleep(3)
                cls_terminal()

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
                db = db_connect(host_db, user_db, passwd_db, nama_db)

                kode_mk = str(input("Masukan Kode MK\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t: "))
                kelas_mk = int(input("Masukan Kelas MK\t: "))
                sks_mk = int(input("Masukan SKS MK\t\t: "))
                nama_dosen = str(input("Masukan Nama Dosen\t: "))
                nip_dosen = int(input("Masukan NIP Dosen\t: "))

                # Update database
                db.input_2_dsn(kode_mk, nama_mk, kelas_mk, sks_mk, nip_dosen, nama_dosen, 'update', tb_21)
                time.sleep(3)
                cls_terminal

            elif (pilihan == '2'):
                print("\nUpdate Data Mahasiswa Kelas 2")
                # Koneksi db ke xampp
                db = db_connect(host_db, user_db, passwd_db, nama_db)

                kode_mk = str(input("Masukan Kode MK\t\t\t: "))
                nama_mk = str(input("Masukan Nama MK\t\t\t: "))
                kelas_mk = int(input("Masukan Kelas MK\t\t: "))
                sks_mk = int(input("Masukan SKS MK\t\t\t: "))
                nama_mhs = str(input("Masukan Nama Mahasiswa\t\t: "))
                npm_mhs = int(input("Masukan Nomor Induk Mahasiswa\t: "))

                # Update database
                db.input_2_mhs(kode_mk, nama_mk, kelas_mk, sks_mk, npm_mhs, nama_mhs, 'update', tb_22)
                time.sleep(3)
                cls_terminal()

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
                        db = db_connect(host_db, user_db, passwd_db, nama_db)
                        db.del_table(tb_11)
                        time.sleep(2)
                        main()

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
                        db = db_connect(host_db, user_db, passwd_db, nama_db)
                        db.del_table(tb_12)
                        time.sleep(2)
                        main()

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
                        db = db_connect(host_db, user_db, passwd_db, nama_db)
                        db.del_table(tb_21)
                        time.sleep(2)
                        main()

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
                        db = db_connect(host_db, user_db, passwd_db, nama_db)
                        db.del_table(tb_22)
                        time.sleep(2)
                        main()

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
                db = db_connect(host_db, user_db, passwd_db, nama_db)
                db.del_db()
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
            time.sleep(3)
            cls_terminal()
            sys.exit()
        else:
            cls_terminal()
            print("\nPilihan Tidak Ada...")
            time.sleep(3)
            cls_terminal()

if __name__ == "__main__":
    main()
