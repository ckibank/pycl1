# Filler code

```python
#    0,   1 ,2
# Lists
d = [1,"Two",3,4.23,"Five"]
```

```python
# Dictionary - { Key : Value, Key2 : Value2 }
e = {
  "id" : 2334,
  "name" : "John",
  "contact": {
    "em1" : "john@em1.com",
    "ph" : "98989686"
  },
  "subj" : ["Fin", "Tech"]
}
```

```python
stock_prices = {
    'AAPL': [150.25, 152.10, 148.75, 151.50, 149.80],
    'MSFT': [280.50, 285.25, 282.75, 278.90, 283.60],
    'AMZN': [3250.00, 3280.50, 3220.75, 3260.25, 3240.10],
    'GOOG': [2750.75, 2780.25, 2760.50, 2770.10, 2765.80],
    'TSLA': [750.00, 760.50, 755.25, 745.80, 752.90]
}
```

### Pacakges to install

```
pandas 
numpy 
matplotlib 
seaborn 
xlwings 
scikit-learn 
tensorflow 
boto3 
requests 
venv 
Flask 
dash 
langchain 
transformers
```

### Html support

```
    <link rel="stylesheet" href="{{ url_for('static', path='styles.css') }}">

<!-- form -->

    <h1>Add Stock</h1>
    <form action="/add">
        <label for="symbol">Stock Symbol:</label>
        <input type="text" id="symbol" name="symbol" required><br><br>
        
        <label for="name">Stock Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="currency">Currency:</label>
        <input type="text" id="currency" name="currency" required><br><br>
        
        <input type="submit" value="Submit">
    </form>

```