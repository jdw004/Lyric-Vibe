import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from taipy.gui import Gui, notify
import pandas as pd

my_theme = {
  "palette": {
    "background": {"default": "#4682b4"},
    "primary": {"main": "#4682b4"}
  },
  ".blue": {
    "color": "blue"
  }
}

stylekit = {
  "color_primary": "#BADA55",
  "color_secondary": "#C0FFE",
  "font-family": "Space Grotesk"
}


cities = [
    {"name": "United States", "lat": 37.09024, "lon": -95.712891, "population": 90210},
    {"name": "United Kingdom", "lat": 55.378051, "lon": -3.435973, "population": 90210},
    {"name": "Andorra", "lat": 42.546245, "lon": 1.601554, "population": 90210},
    {"name": "Argentina", "lat": -38.416097, "lon": -63.616672, "population": 90210},
    {"name": "Australia", "lat": -25.274398, "lon": 133.775136, "population": 90210},
    {"name": "Austria", "lat": 47.516231, "lon": 14.550072, "population": 90210},
    {"name": "Belarus", "lat": 53.709807, "lon": 27.953389, "population": 90210},
    {"name": "Belgium", "lat": 50.503887, "lon": 4.469936, "population": 90210},
    {"name": "Bolivia", "lat": -16.290154, "lon": -63.588653, "population": 90210},
    {"name": "Brazil", "lat": -14.235004, "lon": -51.92528, "population": 90210},
    {"name": "Bulgaria", "lat": 42.733883, "lon": 25.48583, "population": 90210},
    {"name": "Canada", "lat": 56.130366, "lon": -106.346771, "population": 90210},
    {"name": "Chile", "lat": -35.675147, "lon": -71.542969, "population": 90210},
    {"name": "Colombia", "lat": 4.570868, "lon": -74.297333, "population": 90210},
    {"name": "Costa Rica", "lat": 9.748917, "lon": -83.753428, "population": 90210},
    {"name": "Cyprus", "lat": 35.126413, "lon": 33.429859, "population": 90210},
    {"name": "Czech Republic", "lat": 49.817492, "lon": 15.472962, "population": 90210},
    {"name": "Denmark", "lat": 56.26392, "lon": 9.501785, "population": 90210},
    {"name": "Dominican Republic", "lat": 18.735693, "lon": -70.162651, "population": 90210},
    {"name": "Ecuador", "lat": -1.831239, "lon": -78.183406, "population": 90210},
    {"name": "Egypt", "lat": 26.820553, "lon": 30.802498, "population": 90210},
    {"name": "El Salvador", "lat": 13.794185, "lon": -88.89653, "population": 90210},
    {"name": "Estonia", "lat": 58.595272, "lon": 25.013607, "population": 90210},
    {"name": "Finland", "lat": 61.92411, "lon": 25.748151, "population": 90210},
    {"name": "France", "lat": 46.227638, "lon": 2.213749, "population": 90210},
    {"name": "Germany", "lat": 51.165691, "lon": 10.451526, "population": 90210},
    {"name": "Greece", "lat": 39.074208, "lon": 21.824312, "population": 90210},
    {"name": "Guatemala", "lat": 15.783471, "lon": -90.230759, "population": 90210},
    {"name": "Honduras", "lat": 15.199999, "lon": -86.241905, "population": 90210},
    {"name": "Hong Kong", "lat": 22.396428, "lon": 114.109497, "population": 90210},
    {"name": "Hungary", "lat": 47.162494, "lon": 19.503304, "population": 90210},
    {"name": "Iceland", "lat": 64.963051, "lon": -19.020835, "population": 90210},
    {"name": "India", "lat": 20.593684, "lon": 78.96288, "population": 90210},
    {"name": "Indonesia", "lat": -0.789275, "lon": 113.921327, "population": 90210},
    {"name": "Ireland", "lat": 53.41291, "lon": -8.24389, "population": 90210},
    {"name": "Israel", "lat": 31.046051, "lon": 34.851612, "population": 90210},
    {"name": "Italy", "lat": 41.87194, "lon": 12.56738, "population": 90210},
    {"name": "Japan", "lat": 36.204824, "lon": 138.252924, "population": 90210},
    {"name": "Kazakhstan", "lat": 48.019573, "lon": 66.923684, "population": 90210},
    {"name": "Latvia", "lat": 56.879635, "lon": 24.603189, "population": 90210},
    {"name": "Lithuania", "lat": 55.169438, "lon": 23.881275, "population": 90210},
    {"name": "Luxembourg", "lat": 49.815273, "lon": 6.129583, "population": 90210},
    {"name": "Malaysia", "lat": 4.210484, "lon": 101.975766, "population": 90210},
    {"name": "Malta", "lat": 35.937496, "lon": 14.375416, "population": 90210},
    {"name": "Mexico", "lat": 23.634501, "lon": -102.552784, "population": 90210},
    {"name": "Netherlands", "lat": 52.132633, "lon": 5.291266, "population": 90210},
    {"name": "New Zealand", "lat": -40.900557, "lon": 174.885971, "population": 90210},
    {"name": "Nicaragua", "lat": 12.865416, "lon": -85.207229, "population": 90210},
    {"name": "Nigeria", "lat": 9.081999, "lon": 8.675277, "population": 90210},
    {"name": "Norway", "lat": 60.472024, "lon": 8.468946, "population": 90210},
    {"name": "Pakistan", "lat": 30.375321, "lon": 69.345116, "population": 90210},
    {"name": "Panama", "lat": 8.537981, "lon": -80.782127, "population": 90210},
    {"name": "Paraguay", "lat": -23.442503, "lon": -58.443832, "population": 90210},
    {"name": "Peru", "lat": -9.189967, "lon": -75.015152, "population": 90210},
    {"name": "Philippines", "lat": 12.879721, "lon": 121.774017, "population": 90210},
    {"name": "Poland", "lat": 51.919438, "lon": 19.145136, "population": 90210},
    {"name": "Portugal", "lat": 39.399872, "lon": -8.224454, "population": 90210},
    {"name": "Romania", "lat": 45.943161, "lon": 24.96676, "population": 90210},
    {"name": "Russia", "lat": 61.52401, "lon": 105.318756, "population": 90210},
    {"name": "Saudi Arabia", "lat": 23.885942, "lon": 45.079162, "population": 90210},
    {"name": "Singapore", "lat": 1.352083, "lon": 103.819836, "population": 90210},
    {"name": "Slovakia", "lat": 48.669026, "lon": 19.699024, "population": 90210},
    {"name": "South Africa", "lat": -30.559482, "lon": 22.937506, "population": 90210},
    {"name": "South Korea", "lat": 35.907757, "lon": 127.766922, "population": 90210},
    {"name": "Spain", "lat": 40.463667, "lon": -3.74922, "population": 90210},
    {"name": "Sweden", "lat": 60.128161, "lon": 18.643501, "population": 90210},
    {"name": "Switzerland", "lat": 46.818188, "lon": 8.227512, "population": 90210},
    {"name": "Taiwan", "lat": 23.69781, "lon": 120.960515, "population": 90210},
    {"name": "Thailand", "lat": 15.870032, "lon": 100.992541, "population": 90210},
    {"name": "Turkey", "lat": 38.963745, "lon": 35.243322, "population": 90210},
    {"name": "Ukraine", "lat": 48.379433, "lon": 31.16558, "population": 90210},
    {"name": "United Arab Emirates", "lat": 23.424076, "lon": 53.847818, "population": 90210},
    {"name": "Uruguay", "lat": -32.522779, "lon": -55.765835, "population": 90210},
    {"name": "Venezuela", "lat": 6.42375, "lon": -66.58973, "population": 90210},
    {"name": "Vietnam", "lat": 14.058324, "lon": 108.277199, "population": 90210}
]

# Convert to Pandas DataFrame
data = pd.DataFrame(cities)


data["size"] = 10

# Add a column holding the bubble hover texts
# Format is "<city name> [<population>]"
data["text"] = data.apply(lambda row: f"{row['name']} [{row['population']}]", axis=1)

data["color"] = 'rgb(255,255,255)'

marker = {
    # Use the "size" column to set the bubble size
    "size": "size",
    "color": data["color"].tolist()
}

layout = {
    "geo": {
        "showland": True,
        "landcolor": "4A4"
    }
}


page = """
<page|layout|columns=300px 1fr|
<|sidebar|
### **Filters 🔎**{: .blue}
<|{x_selected}|selector|gap=30px|lov={select_x}|dropdown|label=Select x|>
<|{x_selected}|selector|gap=30px|lov={select_x}|dropdown|label=Select x|>
<br/>

|>

<|container|
# **Lyric**{: .blue} Vibe ✨🎶

Tune into your emotions.

<br/>

<|layout|columns=1 1 1|gap=30px|class_name=card|
<placeholder|
## **Placeholder**{: .blue}

<|{placeholder}|input|label=Placeholder|>
|placeholder>

<mood|
## **Mood**{: .blue}

<|{mood}|input|label=How do you think you feel?|>
|mood>

<style|
## **Spotify**{: .blue} Handle

<|{style}|input|label=Type your Spotify Handle...|>
|style>

<|Generate text|button|label=Generate Your Vibe!|>
|>

<br/>

---
### Global Map of **Happiness**{: .blue}
<|{data}|chart|type=scattergeo|mode=markers|lat=lat|lon=lon|marker={marker}|text=text|layout={layout}|>
---
<br/>

### Generated **Information**{: .blue}

<|{tweet}|input|multiline|label=Results|class_name=fullwidth|>

|>
<br/>



"""

Gui(page).run(theme=my_theme, stylekit=stylekit)


