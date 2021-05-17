# Access to 'databases\number-plate-codes.db'
import sqlite3


DATABASENAME = r"databases\number-plate-codes.db"
TABLENAME = "number_plate_codes"

INVALID_DESTINATION = {'Kota', 'Kabupaten', 'Administrasi', 'Sebagian', 'Utara', 'Selatan', 'Timur', 'Barat', 'Pusat'}  # Words that are not refering to a region


class AccessControl:
   def __init__(self, filename:str=DATABASENAME):
      self.__filename = filename
      self.__connector = sqlite3.connect(self.__filename, isolation_level=None)  # Auto commit
      self.__curs = self.__connector.cursor()

   def __del__(self):
      self.__connector.close()

   def show_all(self, tablename: str):
      "Show all datas"
      self.__curs.execute(f"SELECT * FROM {tablename}")
      return self.__curs.fetchall()

   def show(self, tablename: str, condition: str, todisplay: str = '*'):
      "Display specific data"
      self.__curs.execute(f"SELECT {todisplay} FROM {tablename} WHERE {condition}")
      return self.__curs.fetchall()

   def insert(self, tablename: str, data: tuple):
      "Insert data"
      self.__curs.execute(f"INSERT INTO {tablename}(Wilayah, Kode_Wilayah, Subkode) VALUES(?, ?, ?)", (data))

   def update(self, tablename: str, data: tuple, condition: str):
      "Update data"
      self.__curs.execute("UPDATE {0} SET Wilayah=?, Kode_Wilayah=?, Subkode=? WHERE {1}".format(tablename, condition), data)

   def delete(self, tablename: str, condition: str):
      "Delete data"
      self.__curs.execute("DELETE FROM {0} WHERE {1}".format(tablename, condition))


def _test():
   "Test 'AccessControl' class without affecting important datas"

   from time import sleep
   numplateCodes = AccessControl()
   
   print("Show all data:\n", numplateCodes.show_all(TABLENAME))
   print()
   sleep(1)
   try: print("Insert data:\n", numplateCodes.insert(TABLENAME, ("Kota Percobaan", "ABCD", "Z")))
   except: print("Insert data:\n", "Error")
   print()
   sleep(1)
   try: print("Show specific data:\n", numplateCodes.show(TABLENAME, "Kode_Wilayah = 'ABCD'"))
   except: print("Show specific data:\n", "Error")
   print()
   sleep(1)
   try: print("Update data:\n", numplateCodes.update(TABLENAME, ("Kota Untuk Percobaan", "ABCD", "Z"), "Subkode = 'Z'"))
   except: print("Update data:\n", "Error")
   print()
   sleep(1)
   print("Show all data:\n", numplateCodes.show_all(TABLENAME))
   print()
   sleep(1)
   try: print("Delete data:\n", numplateCodes.delete(TABLENAME, "Wilayah='Kota Untuk Percobaan'"))
   except: print("Delete data:\n", "Error")
   sleep(1)
   print()
   print("Show all data:\n", numplateCodes.show_all(TABLENAME))
   print()

   del numplateCodes


if __name__ == '__main__':
   _test()
   pass
