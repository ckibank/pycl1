import xlwings as xw

def main():
  wb = xw.Book("b_book1.xlsm")
  sh = wb.sheets[0]
  sh["A1"].value = "Ran Main from python"

# C:\xlwcl\env4xw\Scripts\python.exe

def hi_from_xl():
  wb = xw.Book.caller()
  wb.sheets["Sheet1"]["A2"].value = "Hi from Python Function"

# RunPython ("import b_book1; b_book1.hi_from_xl()")
