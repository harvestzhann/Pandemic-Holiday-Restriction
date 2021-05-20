import os, sys
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(path)


from accessDatabase import RegionCodeAccess as regcode


def main():
   numplate = input("Your plate: ").capitalize()

   print()

   access = regcode.AccessControl()
   fixallowed = access.show(f"Region_Code = '{numplate.split()[0]}' AND Subcode LIKE '%{numplate.split()[-1][0]}%'", 'Region')[0][0]
   print("Fix destination to go:", fixallowed)
   allowed = access.show(f"Region_Code = '{numplate.split()[0]}'", 'Region')  # TODO: Return only region names
   print("Destinations you might can go to:", allowed)


if __name__ == '__main__':
   main()
