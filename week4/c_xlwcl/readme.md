### Install XLWings

```
cd \
mkdir xwcl
cd xwcl
python -m venv env4xw
pip install xlwings
pip install pandas
pip install matplotlib
xlwings addin install
```

# Create d_graphs

1. ```xlwings quickstart d_graphs```
2. Open excle file
3. In Excel Wings context menu, set PYTHONPATH to the exact folder name where the Python file exists. It should not end with a \ Eg.
  ```C:\xlwcl\d_graphs```

4. In Excel > Developer > Visual Basic > Module1
  ```
  Sub GenPltGraph()
    mymodule = Left(ThisWorkbook.name, (InStrRev(ThisWorkbook.name, ".", -1, vbTextCompare) - 1))
    RunPython "import " & mymodule & ";" & mymodule & ".mat_plt_graph()"
End Sub
  ```