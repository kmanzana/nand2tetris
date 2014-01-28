#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ PY01
# FILENAME:....... Main.py
# PYTHON VERSION:. 3.3.3
#============================================================

from Header import Header

class Main:
  def main(self):
    header = Header()

    header.setDividerLength(60)
    header.setValueColumn(20)
    header.setUserID("ADET_ID")
    header.setProgrammer("Lname, Fname MI.")
    header.setCourse("CSCI-400")
    header.setTerm("SP14")
    header.setProject("01")
    header.setPython("3.3.3")

    print("******************************************")
    print("*** Header Format Examples ***")
    print("******************************************")
    print('')

    for ext in ["hack","xml","hdl","asm","vm","jack","py"]:
      print("---------------")
      print(ext.upper())
      print("---------------")
      print(header.gen("AnExample." + ext))

    print("******************************************")
    print("*** End of Header Format Examples ***")
    print("******************************************")
