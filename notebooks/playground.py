import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    charges = [10, 20, 30]
    return (charges,)


@app.cell
def _(charges):
    sum(charges)
    return


@app.cell
def _(charges):
    sum(charges)
    return


@app.cell
def _(products):
    import csv
    import os

    os.makedirs("data", exist_ok=True)  # create the data folder if it isn't there yet

    with open("data/products.csv", "w", newline="") as _f:
        _writer = csv.writer(_f)
        _writer.writerow(["product_id", "name", "price"])
        for _row in products:
            _writer.writerow(_row)
    return csv, os


@app.cell
def _():
    products = [
        [101, "Notebook", 4.99],
        [102, "Pen", 1.25],
        [103, "Stapler", 12.50],
        [104, "Backpack", 45.00],
        [105, "Marker", 2.75],
        [106, "Folder", 0.99],
        [107, "Calculator", 15.30],
        [108, "Ruler", 1.50],
        [109, "Eraser", 0.75],
        [110, "Highlighter", 2.20],
    ]
    products
    return (products,)


@app.cell
def _(csv):
    loaded_products = []

    with open("data/products.csv", "r", newline="") as _f:
        _reader = csv.reader(_f)
        next(_reader)  # skip the header row
        for _row in _reader:
            product_id = int(_row[0])
            name = _row[1]
            price = float(_row[2])
            loaded_products.append([product_id, name, price])

    loaded_products
    return (loaded_products,)


@app.cell
def _(os):
    os.getcwd()
    return


@app.cell
def _():
    return


@app.cell
def _(loaded_products):
    total_price = 0
    for _row in loaded_products:
        total_price = total_price + _row[2]

    total_price
    return


if __name__ == "__main__":
    app.run()
