# Read IBM.json and display the contents as is

import json
from datetime import datetime


file = "IBM.json"

with open(file, "r") as f:
  values = json.load(f)

# print(values)

"""
Stock Symbol: ----
Values Updated: --/--/----
Function type: -----
"""

# print(values["Meta Data"]["1. Information"])
# print(values["Meta Data"]["2. Symbol"])
# print(values["Meta Data"]["3. Last Refreshed"])

print(f"""
Stock Symbol: {values["Meta Data"]["2. Symbol"]}
Values Updated at: {values["Meta Data"]["3. Last Refreshed"]}
Function type: {values["Meta Data"]["1. Information"]}
""")

"""
Date        |  Closing Price
---/--/---  |   $xxxx.xx
---/--/---  |   $xxxx.xx
dd/mm/yyyy  |   $xxxx.xx
.
.
.
.
"""

cl_vs = values["Time Series (Daily)"]

for k,v in cl_vs.items():
  # print(f"{k} : ${float(v["4. close"]):.2f}")
  print(f"{k} : ${float(v["4. close"]):.2f}")