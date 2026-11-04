import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import requests

    return (requests,)


@app.cell
def _(requests):
    reply = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": "Wellesley"},
    )
    reply.status_code
    return (reply,)


@app.cell
def _(reply):
    reply.json() 
    return


@app.cell
def _():
    reply_2 = {
        "count": 2,
        "data": [
            {"name": "Carla", "city": "Boston", "age": 34},
            {"name": "Hiro", "city": "Austin", "age": 29},
        ],
    }
    return (reply_2,)


@app.cell
def _(reply_2):
    len(reply_2['data'][0])
    return


@app.cell
def _(reply_2):
    reply_2['data'][1]['age']
    return


@app.function
def make_label(name, county):
    label = f"{name}, {county}"
    return label


@app.cell
def _():
    result = make_label("Wellesley", "Norfolk")
    print(f'I live in {result}.')

    shubham = make_label('Newton', 'Middlesex')
    print(f'Shubham lives in {shubham}.')
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
