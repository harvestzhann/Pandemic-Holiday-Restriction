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
   dbname = "number-plate-codes.db"
   tablename = "number_plate_codes"
   sqlcommand = str(
      f"""
         CREATE TABLE number_plate_codes (
            `Wilayah` text,
            `Kode_Wilayah` text,
            `Subkode` text
         );
      """
   )
   CREATETABLE(dbname, tablename, sqlcommand)


if __name__ == "__main__":
   # TODO Create table for the first time
   print("Creating a test table: ", end='')
   CREATE_DEFAULT_TABLE()
