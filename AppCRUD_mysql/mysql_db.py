import mysql.connector as mysql

class db_connect:
    def __init__(self, host_db, user_db, passwd_db, nama_db):
        self.host = host_db
        self.user = user_db
        self.passwd = passwd_db
        self.nama_db = nama_db

    def create_db(self):
        # connect database to xampp
        account = mysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd
        )
        
        # cursor 
        cursor = account.cursor()

        # Create new database
        new_db = f"CREATE DATABASE IF NOT EXISTS {self.nama_db};"
        cursor.execute(new_db)
        # Commit
        account.commit()
        # Close
        account.close()

    def create_table(self, table, name_tb):
        self.tb = table
        self.name_tb = name_tb
        # Connected
        db = mysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.nama_db
        )

        # cursor 
        cursor = db.cursor()

        # Create new table
        if(self.tb == 'table_1_dsn'):
            table_1_dsn = f"CREATE TABLE IF NOT EXISTS {self.name_tb} ( nip_dosen BIGINT PRIMARY KEY, nama_dosen VARCHAR(35), kode_mk VARCHAR(7), nama_mk VARCHAR(25), kelas INT, sks INT )"
            # Execute table
            cursor.execute(table_1_dsn)
            # commit
            db.commit()
            # close
            db.close()

        elif(self.tb == 'table_2_dsn'):
            table_2_dsn = f"CREATE TABLE IF NOT EXISTS {self.name_tb} ( nip_dosen BIGINT PRIMARY KEY, nama_dosen VARCHAR(35), kode_mk VARCHAR(7), nama_mk VARCHAR(25), kelas INT, sks INT )"
            # Execute table
            cursor.execute(table_2_dsn)
            # commit
            db.commit()
            # close
            db.close()
        
        elif(self.tb == 'table_1_mhs'):
            table_1_mhs = f"CREATE TABLE IF NOT EXISTS {self.name_tb} ( npm_mhs BIGINT PRIMARY KEY, nama_mhs VARCHAR(35), kode_mk VARCHAR(7), nama_mk VARCHAR(25), kelas INT, sks INT )"
            # Execute table
            cursor.execute(table_1_mhs)
            # commit
            db.commit()
            # close
            db.close()
        
        elif(self.tb == 'table_2_mhs'):
            table_2_mhs = f"CREATE TABLE IF NOT EXISTS {self.name_tb} ( npm_mhs BIGINT PRIMARY KEY, nama_mhs VARCHAR(35), kode_mk VARCHAR(7), nama_mk VARCHAR(25), kelas INT, sks INT )"
            # Execute table
            cursor.execute(table_2_mhs)
            # commit
            db.commit()
            # close
            db.close()

        else:
            print("\nOnly 4 new tables avaliable")
            # close
            db.close()

    def input_1_dsn(self, kode, mk, kls, sks, nip, nama, action, name_tb):
        self.kode = kode
        self.nama_mk = mk
        self.kls = kls
        self.sks = sks
        self.nip = nip
        self.nama_dsn = nama
        self.action = action
        self.name_tb = name_tb

        # Connected
        db = mysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.nama_db
        )
        c= db.cursor()

        if(self.action == 'input'):
            # Input data
            sql_input = f"INSERT INTO {self.name_tb} (nip_dosen, nama_dosen, kode_mk, nama_mk, kelas, sks) VALUES (%s, %s, %s, %s, %s, %s)"
            val_input = (f"{self.nip}", f"{self.nama_dsn}", f"{self.kode}", f"{self.nama_mk}", f"{self.kls}", f"{self.sks}")
            # Execute data
            c.execute(sql_input, val_input)
            # Commit
            db.commit()
            # Done
            print(f"\n{c.rowcount} Data ditambah...")

        elif(self.action == 'update'):
            # Input data
            sql_update = f"UPDATE {self.name_tb} SET nama_dosen=%s, kode_mk=%s, nama_mk=%s, kelas=%s, sks=%s WHERE nip_dosen=%s"
            val_update = (f"{self.nama_dsn}", f"{self.kode}", f"{self.nama_mk}", f"{self.kls}", f"{self.sks}", f"{self.nip}")
            # Execute data
            c.execute(sql_update, val_update)
            # Commit
            db.commit()
            # Done
            print(f"\n{c.rowcount} Data diupdate...")
        
        else:
            print("\nOnly 2 actions available")

        # Close
        db.close()

    def input_2_dsn(self, kode, mk, kls, sks, nip, nama, action, name_tb):
        self.kode = kode
        self.nama_mk = mk
        self.kls = kls
        self.sks = sks
        self.nip = nip
        self.nama_dsn = nama
        self.action = action
        self.name_tb = name_tb

        # Connected
        db = mysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.nama_db
        )
        c= db.cursor()

        if(self.action == 'input'):
            # Input data
            sql_input = f"INSERT INTO {self.name_tb} (nip_dosen, nama_dosen, kode_mk, nama_mk, kelas, sks) VALUES (%s, %s, %s, %s, %s, %s)"
            val_input = (f"{self.nip}", f"{self.nama_dsn}", f"{self.kode}", f"{self.nama_mk}", f"{self.kls}", f"{self.sks}")
            # Execute data
            c.execute(sql_input, val_input)
            # Commit
            db.commit()
            # Done
            print(f"\n{c.rowcount} Data ditambah...")
            # Close
            db.close()

        elif(self.action == 'update'):
            # Input data
            sql_update = f"UPDATE {self.name_tb} SET nama_dosen=%s, kode_mk=%s, nama_mk=%s, kelas=%s, sks=%s WHERE nip_dosen=%s"
            val_update = (f"{self.nama_dsn}", f"{self.kode}", f"{self.nama_mk}", f"{self.kls}", f"{self.sks}", f"{self.nip}")
            # Execute data
            c.execute(sql_update, val_update)
            # Commit
            db.commit()
            # Done
            print(f"\n{c.rowcount} Data diupdate...")
            # Close
            db.close()
        
        else:
            print("\nOnly 2 actions available")
            # Close
            db.close()

    def input_1_mhs(self, kode, mk, kls, sks, npm, nama, action, name_tb):
        self.kode = kode
        self.nama_mk = mk
        self.kls = kls
        self.sks = sks
        self.npm = npm
        self.nama_mhs = nama
        self.action = action
        self.name_tb = name_tb

        # Connected
        db = mysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.nama_db
        )

        c = db.cursor()

        if(self.action == 'input'):
            # Input data
            sql_input = f"INSERT INTO {self.name_tb} (npm_mhs, nama_mhs, kode_mk, nama_mk, kelas, sks) VALUES (%s, %s, %s, %s, %s, %s)"
            val_input = (f"{self.npm}", f"{self.nama_mhs}", f"{self.kode}", f"{self.nama_mk}", f"{self.kls}", f"{self.sks}")
            # Execute data
            c.execute(sql_input, val_input)
            # Commit
            db.commit()
            # Done
            print(f"\n{c.rowcount} Data ditambah...")
            # Close
            db.close()
            
        elif(self.action == 'update'):
            # Input data
            sql_update = f"UPDATE {self.name_tb} SET nama_mhs=%s, kode_mk=%s, nama_mk=%s, kelas=%s, sks=%s WHERE npm_mhs=%s"
            val_update = (f"{self.nama_mhs}", f"{self.kode}", f"{self.nama_mk}", f"{self.kls}", f"{self.sks}", f"{self.npm}")
            # Execute data
            c.execute(sql_update, val_update)
            # Commit
            db.commit()
            # Done
            print(f"\n{c.rowcount} Data diupdate...")
            # Close
            db.close()
        
        else:
            print("\nOnly 2 actions available")
            # Close
            db.close()

    def input_2_mhs(self, kode, mk, kls, sks, npm, nama, action, name_tb):
        self.kode = kode
        self.nama_mk = mk
        self.kls = kls
        self.sks = sks
        self.npm = npm
        self.nama_mhs = nama
        self.action = action
        self.name_tb = name_tb

        # Connected
        db = mysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.nama_db
        )

        c = db.cursor()

        if(self.action == 'input'):
            # Input data
            sql_input = f"INSERT INTO {self.name_tb} (npm_mhs, nama_mhs, kode_mk, nama_mk, kelas, sks) VALUES (%s, %s, %s, %s, %s, %s)"
            val_input = (f"{self.npm}", f"{self.nama_mhs}", f"{self.kode}", f"{self.nama_mk}", f"{self.kls}", f"{self.sks}")
            # Execute data
            c.execute(sql_input, val_input)
            # Commit
            db.commit()
            # Done
            print(f"\n{c.rowcount} Data ditambah...")
            # Close
            db.close()
            
        elif(self.action == 'update'):
            # Input data
            sql_update = f"UPDATE {self.name_tb} SET nama_mhs=%s, kode_mk=%s, nama_mk=%s, kelas=%s, sks=%s WHERE npm_mhs=%s"
            val_update = (f"{self.nama_mhs}", f"{self.kode}", f"{self.nama_mk}", f"{self.kls}", f"{self.sks}", f"{self.npm}")
            # Execute data
            c.execute(sql_update, val_update)
            # Commit
            db.commit()
            # Done
            print(f"\n{c.rowcount} Data diupdate...")
            # Close
            db.close()

        else:
            print("\nOnly 2 actions available")
            # Close
            db.close()
    
    def show_data(self, table, name_tb):
        self.tb = table
        self.name_tb = name_tb
        # Connected
        db = mysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.nama_db
        )
        # Cursor
        c = db.cursor()
        if(self.tb == 'table_1_dsn' or self.tb == 'table_2_dsn'):
            print(f"\nData {self.name_tb}...")
            sql_dsn = f"SELECT * FROM {self.name_tb}"
            # Execute
            c.execute(sql_dsn)
            results1 = c.fetchall()
            list_data1 = ""

            for data in results1:
                list_data1 += f"\nKode MK\t\t: {data[0]} \nNama MK\t\t: {data[1]} \nKelas\t\t: {data[2]} \nSKS\t\t: {data[3]} \nNama Dosen\t: {data[5]} \nNIP Dosen\t: {data[4]}"

            # Show
            print(list_data1)
            
        elif(self.tb == 'table_1_mhs' or self.tb == 'table_2_mhs'):
            print(f"\nData {self.name_tb}...")
            sql_mhs = f"SELECT * FROM {self.name_tb}"
            # Execute
            c.execute(sql_mhs)
            results2 = c.fetchall()
            list_data2 = ""
            
            for data in results2:
                list_data2 += f"\nKode MK\t\t: {data[2]} \nNama MK\t\t: {data[3]} \nKelas\t\t: {data[4]} \nSKS\t\t: {data[5]} \nNama Mahasiswa\t: {data[1]} \nNPM\t\t: {data[0]}"
            # Show
            print(list_data2)
        
        else:
            print("\nError...")

        print()
        # Close
        db.close()
    
    def delete_rows(self, table, name_tb, id):
        self.tb = table
        self.name_tb = name_tb
        self.id = id
        # Connected
        db = mysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.nama_db
        )
        # Cursor
        c = db.cursor()
        if(self.tb == 'table_1_dsn' or self.tb == 'table_2_dsn'):
            # Select the nip dosen to delete from table
            query1 = f"DELETE FROM {self.name_tb} WHERE nip_dosen= {self.id}"
            # Execute
            c.execute(query1)
            # Commit
            db.commit()
            # Done
            print(f"\n{c.rowcount} Data dihapus...")
        
        elif(self.tb == 'table_1_mhs' or self.tb == 'table_2_mhs'):
            # Select the npm mhs to delete from table
            query2 = f"DELETE FROM {self.name_tb} WHERE npm_mhs= {self.id}"
            # Execute
            c.execute(query2)
            # Commit
            db.commit()
            # Done
            print(f"\n{c.rowcount} Data dihapus...")
        
        else:
            print("\nError...")
        
        print()    
        # Close
        db.close()

    def del_table(self, name_tb):
        self.tb = name_tb
        # Connected
        db = mysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.nama_db
        )
        # Cursor
        c = db.cursor()
        # Drop table if exists
        del_tb = f"DROP TABLE IF EXISTS {self.tb};"
        # Execute
        c.execute(del_tb)
        # commit
        db.commit()
        print(f"\nSemua Data {self.tb} Telah Dihapus...")
        # Close
        db.close()

    def del_db(self):
        # Connected
        db = mysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd
        )
        # Cursor
        c = db.cursor()
        # Delete DB if exists
        delete = f"DROP DATABASE IF EXISTS {self.nama_db};"
        # Execute
        c.execute(delete)
        # commit
        db.commit()
        # Close
        db.close()
        print(f"\nDatabase {self.nama_db} Telah Dihapus...")


