import sqlite3


def CREATETABLE(dbname:str, tablename:str, sqlcommand:str):
   with sqlite3.connect(dbname, isolation_level=None) as conn:
      curs = conn.cursor()
      try:
         curs.execute(sqlcommand)
         print(f"Creating '{tablename}' is done")
      except sqlite3.OperationalError:
         print(f"Table '{tablename}' already exists")


def CREATE_DEFAULT_TABLE():
   "Creating default table for the first time"
   dbname = r"databases\number-plate-codes.db"
   tablename = "number_plate_codes"
   sqlcommand = str(
      f"""
         CREATE TABLE number_plate_codes (
            `Region` TEXT,
            `Region_Code` TEXT,
            `Subcode` TEXT
         );
      """
   )
   CREATETABLE(dbname, tablename, sqlcommand)


def INSET_DEFAULT_RECORDS():
   "Creating default table for the first time"
   dbname = r"databases\number-plate-codes.db"
   tablename = "number_plate_codes"
   sqlcommand = str(
      f"""
         INSERT INTO number_plate_codes(Region, Region_Code, Subcode) VALUES 
            ('Kota Serang','A','A, B, C, D'),
            ('Kabupaten Serang','A','E, F, G, H, I'),
            ('Kabupaten Pandeglang','A','J, K, L, M, N'),
            ('Kota Cilegon','A','O, U'),
            ('Kabupaten Lebak','A','P, R, S, T'),
            ('Kabupaten Tangerang','A','V, W, X, Y, Z'),
            ('Kota Administrasi Jakarta Barat','B','B'),
            ('Kota Tangerang','B','C, V'),
            ('Kota Depok','B','E, Z'),
            ('Kabupaten Bekasi','B','F'),
            ('Kota Bekasi','B','K'),
            ('Kota Administrasi Jakarta Pusat','B','P'),
            ('Kota Administrasi Jakarta Selatan','B','S'),
            ('Kota Administrasi Jakarta Timur','B','T'),
            ('Kota Administrasi Jakarta Utara','B','U'),
            ('Kota Tangerang Selatan','B','W'),
            ('Kota Bandung','D','A, B, C, D, E, F, M, N, O, P, R, G, H, I, J, K, L'),
            ('Kota Cimahi','D','S, T'),
            ('Kabupaten Bandung Barat','D','U, X, Z'),
            ('Kabupaten Bandung','D','V, W, Y'),
            ('Kota Cirebon','E','A, B, C, D, E, F, G'),
            ('Kabupaten Cirebon','E','H, I, J, K, L, M, N, O'),
            ('Kabupaten Indramayu','E','P, Q, R, S, T'),
            ('Kabupaten Majalengka','E','U, V, W, X'),
            ('Kabupaten Kuningan','E','Y,Z'),
            ('Kota Bogor','F','A, B, C, D, E'),
            ('Kabupaten Bogor','F','F, G, H, I, J, K, L, M, N, O, P, R'),
            ('Kabupaten Sukabumi','F','Q, U, V'),
            ('Kota Sukabumi','F','S, T'),
            ('Kabupaten Cianjur','F','W, X, Y, Z'),
            ('Kabupaten Purwakarta','T','A, B, C'),
            ('Kabupaten Karawang','T','D, E, F, G, H, O, P, Q, R, S, I, J, K, L, M, N'),
            ('Subang','T','T, U, V, W, X, Y, Z'),
            ('Kabupaten Sumedang','Z','Z – A, B, C'),
            ('Kabupaten Garut','Z','D, E, F, G'),
            ('Kota Tasikmalaya','Z','H, I, J'),
            ('Kabupaten Tasikmalaya','Z','K, L, M, N, O, P, Q, R, S'),
            ('Kabupaten Ciamis','Z','T, U, V'),
            ('Kabupaten Pangandaran','Z','W'),
            ('Kota Banjar','Z','X, Y, Z');
      """
   )
   CREATETABLE(dbname, tablename, sqlcommand)


if __name__ == "__main__":
   # TODO Create table for the first time
   print("Creating a test table: ", end='')
   CREATE_DEFAULT_TABLE()
   INSET_DEFAULT_RECORDS()
