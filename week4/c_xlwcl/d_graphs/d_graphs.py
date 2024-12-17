import xlwings as xw
import random
import pandas as pd
import matplotlib.pyplot as plt


def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    if sheet["A1"].value == "Hello xlwings!":
        sheet["A1"].value = "Bye xlwings!"
    else:
        sheet["A1"].value = "Hello xlwings!"

@xw.func
def gen_lists(num_of_cols, num_of_rows):
  num_of_cols = int(num_of_cols)
  num_of_rows = int(num_of_rows)
  rnd_nums = [[random.randint(0, 100) for _ in range(num_of_cols)] for _ in range(num_of_rows)]
  return rnd_nums


def mat_plt_graph():
  wb = xw.Book.caller()
  sheet = wb.sheets["data"]
  sh = wb.sheets["Sheet1"]

  data = sheet.range('A1:B10').value

  df = pd.DataFrame(data, columns=['A', 'B'])
  graph_type = sh.range('B1').value

  print(f"---- matPlotLibPY Plot as {graph_type} graph")
  print(df)

  plt.figure()
  plt.scatter(df['A'], df['B'])
  
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title(f'{graph_type.capitalize()} Plot')
  plt.savefig(r"C:\xlwcl\d_graphs\temp_file.png")

  sh.pictures.add(r"C:\xlwcl\d_graphs\temp_file.png", name="PyPlot", update=True, anchor=sh["B7"])


@xw.func
def hello(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    xw.Book("d_graphs.xlsm").set_mock_caller()
    main()
