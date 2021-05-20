import os, sys
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(path)


from accessDatabase import RegionCodeAccess as regcode


def main():
   numplate = input("Your plate: ").capitalize()

   print()

   access = regcode.AccessControl()

   # Exact destination that allows 'numplate'
   fixallowed = access.show(f"Region_Code = '{numplate.split()[0]}' AND Subcode LIKE '%{numplate.split()[-1][0]}%'", 'Region')[0][0]
   print("Fix destination to be:", fixallowed)

   # Destinations that might allows 'numplate'
   allowed = access.show(f"Region_Code = '{numplate.split()[0]}'", 'Region')
   print("Possible destinations allowed:")

   for every_tuple in allowed:
      for region in every_tuple:
         print(f"  - {region}")


if __name__ == '__main__':
   main()
