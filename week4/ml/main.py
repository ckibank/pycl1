# Basic Python template
# First install Sklearn from packager manually
# Search sklearn and install ***** sklearn-pandas *****
#                  ***** IMPORTANT ^^^^^^^^^^^^^^
# Once installed run the code

import pandas as pd
# import sklearn
from sklearn.naive_bayes import GaussianNB

# print(pd)
# print(sklearn)

# Dictionary for Predictive answer
InvType = {
  1: "Invest_ESG",
  2: "Monitor_ESG",
  3: "Prof_Non_ESG",
  4: "No_Prof_No_ESG"
}

# Reading data using pandas
# df = pd.read_csv("ESG-Classifier.csv")
df = pd.read_csv("ESG-less-data.csv")
print(df.head())

# --- Train model ---
# All features
x = df[df.columns[0:4]]
# Label
y = df.Type

# print(x)
# print("-"*20)
# print(y)

print("**** Training GB ****")
gb = GaussianNB()
gb.fit(x,y)
gbs = gb.score(x,y)*100

print("Score:", gbs)

# predict using a loop
for i in range(0,16):
  int_to_binary=f"{i:b}"
  inp=f"{int_to_binary:0>4}"

  data = {
    "EP": inp[0],
    "EI": inp[1],
    "DB": inp[2],
    "PR": inp[3]
  }

  pdt = pd.DataFrame(data, columns=["EP","EI","DB","PR"], index=[0])
  g = gb.predict(pdt)
  
  # print(f"{inp}: {InvType[g[0]]}")
  print(f"{inp[0]},{inp[1]},{inp[2]},{inp[3]}:{g[0]}-{InvType[g[0]]}")
  # print(f"{inp[0]},{inp[1]},{inp[2]},{inp[3]},{g[0]}")

# Show the output label for  all different combination of features that are possible 