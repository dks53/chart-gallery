# three_charts.py

import plotly
import plotly.graph_objs as go

#
# CHART 1 (PIE)
#

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
## PIE CHART EXAMPLE

#labels = ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]
#values = [4500, 2500, 1053, 500]
#
#trace = go.Pie(labels=labels, values=values)
#
#plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

print("----------------")
print("GENERATING PIE CHART...")

labels = []

for i in range(0, len(pie_data)):
    labels.append(pie_data[i]["company"])

values = []

for p in range(0, len(pie_data)):
    values.append(pie_data[p]["market_share"])

#trace = go.Pie(labels=labels, values=values)
#plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)


#
# CHART 2 (LINE)
#

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
## LINE CHART EXAMPLE

#plotly.offline.plot({
#    "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#    "layout": go.Layout(title="hello world")
#}, auto_open=True)

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

print("----------------")
print("GENERATING LINE GRAPH...")

x = []

for r in range(0, len(line_data)):
    x.append(line_data[r]["date"])

y = []

for q in range(0, len(line_data)):
    y.append(line_data[q]["stock_price_usd"])

print(x)
print(y)

#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

print("----------------")
print("GENERATING BAR CHART...")
print(bar_data) # TODO: create a horizontal bar chart based on the bar_data
print("----------------")
