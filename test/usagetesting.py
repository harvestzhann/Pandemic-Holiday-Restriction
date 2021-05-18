# Test if all files are working

import os, sys
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(path)


from accessDatabase import RegionCodeAccess as regcode


def validestination(destination):
   "Check if destination is a valid"
   destination = destination.capitalize()
   valid = set(destination.split()).difference(regcode.INVALID_DESTINATION)

   if len(valid) == 0:
      return False, destination
   return True, destination


def isAllowed(numplate, destination):
   "Check whether vehicle is allowed"
   output = {
      'allowed' : 1,
      'not allowed' : 0,
      'not found' : -1,
      'compound reference' : -2
   }

   destination = validestination(destination)

   if not destination[0]:
      return output['compound reference']

   numplateFrontCode = numplate.split()[0]
   numplateBackCode = numplate.split()[-1]

   regionCodeAccess = regcode.AccessControl()

   regionCode = regionCodeAccess.show(f"Wilayah LIKE '%{destination[1]}%'", 'Kode_Wilayah, Subkode')   # Getting region code from destination

   if len(regionCode) > 1:
      return output['compound reference']  # Many region has that word
   elif len(regionCode) == 0:
      return output['not found']
   
   regionFrontCode = [i[0] for i in regionCode]
   regionBackCode = [i[1] for i in regionCode]

   if numplateFrontCode in regionFrontCode and numplateBackCode in regionBackCode:
      return output['allowed']
   return output['not allowed']


def main():
   numplate = "B 1976 FKJ" 
   print(numplate)

   while True:
      destination = input("Your destination: ")
      if isAllowed(numplate, destination) == 1:
         print("Allowed")
      elif isAllowed(numplate, destination) == 0:
         print("Not Allowed")
      else:
         print(f"'{destination.capitalize()}' refers to many region")


if __name__ == '__main__':
   main()
