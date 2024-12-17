import xlwings as xw

@xw.func
def myhi(your_name):
  return f"My Hi to {your_name}"