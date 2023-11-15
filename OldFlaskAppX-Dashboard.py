import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash()

latitude = [40.7128, 41.8781, 37.7749]
longitude = [-74.0060, -87.6298, -122.4194]
size = [10, 20, 30]

# Define a callback to read the text file and display the number of lines
@app.callback(Output('line-count', 'children'), [Input('text-widget', 'id')])
def display_line_count(widget_id):
    # Read the text file
    with open('OldFlaskAppX-Sample.txt', 'r') as f:
        text = f.read()
    # Split the text into a list of lines
    lines = text.split('\n')
    # Get the number of lines
    line_count = len(lines)
    # Display the number of lines in the widget
    return f'Number of lines: {line_count}'

# Define a callback to read the text file and display the content
@app.callback(Output('text-content', 'children'), [Input('text-content-widget', 'id')])
def display_text_content(widget_id):
    # Read the text file
    with open('OldFlaskAppX-Sample.txt', 'r') as f:
        text = f.read()
    # Display the content of the text file in the widget
    return html.Pre(text)


countries = ['Afghanistan', 'Albania', 'Algeria', 'Pakistan', 'China', 'pakistan', 'china']
counts = {}
for country in countries:
    if country in counts:
        counts[country] += 1
    else:
        counts[country] = 1

# Create a dataframe with the counts
df = pd.DataFrame(list(counts.items()), columns=['Country', 'Count'])

# Create the pie chart using plotly.express
fig = px.pie(df, values='Count', names='Country', title='Number of Times Countries Are Repeated')

def extract_countries(text):
    # Create a list of country names
    countries_list = countries
    counts = {}
    for country in countries:
        if country in counts:
            counts[country] += 1
        else:
            counts[country] = 1    
    # Split the text into a list of words
    words = text.split()
    # Make the words case-insensitive
    words = [word.lower() for word in words]
    # Initialize an empty list for the countries
    countries = []
    # Iterate over the words and extract the countries
    for word in words:
        if word in countries_list:
            countries.append(word)
    # Remove duplicates from the list of countries
    countries = list(set(countries))
    # Return the list of countries
    return countries

def extract_weapons(text):
    # Create a list of weapon names
    weapons_list = ['tank', 'al-khalid tank', 'al-zarrar', 'a-hussein', 'type']
    # Split the text into a list of words
    words = text.split()
    # Make the words case-insensitive
    words = [word.lower() for word in words]
    # Initialize an empty list for the weapons
    weapons = []
    # Iterate over the words and extract the weapons
    for word in words:
        if word in weapons_list:
            temp = words.index(word)
            temp = (words[temp] +  str(words[temp+1]))
            if word.lower() in weapons_list:
                weapons.append(temp)
            else:
                weapons.append(word)
    # Remove duplicates from the list of weapons
    weapons = list(set(weapons))
    # Return the list of weapons
    return weapons

# Define a callback to extract and display the list of countries from the text file
@app.callback(Output('countries-list', 'children'), [Input('countries-widget', 'id')])
def display_countries(widget_id):
    # Read the text file
    with open('SampleText.txt', 'r') as f:
        text = f.read()
    # Extract the list of countries
    countries = extract_countries(text)
    # Display the list of countries in the widget
    return html.Ul([html.Li(country) for country in countries])

# Define a callback to read the text file and display the list of weapons
@app.callback(Output('weapons-list', 'children'), [Input('weapons-widget', 'id')])
def display_weapons(widget_id):
    # Read the text file
    with open('SampleText.txt', 'r') as f:
        text = f.read()
    # Extract the list of weapons
    weapons = extract_weapons(text)
    # Display the list of weapons in the widget
    return html.Ul([html.Li(weapon) for weapon in weapons])

# Set up the layout of the dashboard
app.layout = html.Div([
    # Add a widget for the text file
    html.Div(
        id='text-widget',
        className='widget',
        style={
            'backgroundColor': '#f4f4f4',
            'borderRadius': '5px',
            'boxShadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
            'fontFamily': 'Roboto, sans-serif',
            'padding': '20px'
        },
        children=[
            # Add a titlebar div
            html.Div(
                style={
                    'backgroundColor': '#3498db',
                    'color': '#ffffff',
                    'fontSize': '18px',
                    'fontWeight': 'bold',
                    'padding': '10px'
                },
                children='Text File'
            ),
            # Add a div to display the number of lines in the text file
            html.Div(id='line-count')
        ]
    ),
    # Add a widget to display the content of the text file
    html.Div(
        id='text-content-widget',
        className='widget',
        style={
            'backgroundColor': '#f4f4f4',
            'borderRadius': '5px',
            'boxShadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
            'fontFamily': 'Roboto, sans-serif',
            'padding': '20px'
        },
        children=[
            # Add a titlebar div
            html.Div(
                style={
                    'backgroundColor': '#3498db',
                    'color': '#ffffff',
                    'fontSize': '18px',
                    'fontWeight': 'bold',
                    'padding': '10px'
                },
                children='Text Content'
            ),
            # Add a div to display the content of the text file
            html.Div(id='text-content')
        ]
    ),
    html.Div(
        id='countries-widget',
        className='widget',
        style={
            'backgroundColor': '#f4f4f4',
            'borderRadius': '5px',
            'boxShadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
            'fontFamily': 'Roboto, sans-serif',
            'padding': '20px'
        },
        children=[
            # Add a titlebar div
            html.Div(
                style={
                    'backgroundColor': '#3498db',
                    'color': '#ffffff',
                    'fontSize': '18px',
                    'fontWeight': 'bold',
                    'padding': '10px'
                },
                children='Countries'
            ),
            # Add a div to display the pie chart
            dcc.Graph(
                id='countries-pie-chart',
                figure=fig
            )
        ]
    ),
    html.Div(
        id='weapons-widget',
        className='widget',
        style={
            'backgroundColor': '#f4f4f4',
            'borderRadius': '5px',
            'boxShadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
            'fontFamily': 'Roboto, sans-serif',
            'padding': '20px'
        },
        children=[
            # Add a titlebar div
            html.Div(
                style={
                    'backgroundColor': '#3498db',
                    'color': '#ffffff',
                    'fontSize': '18px',
                    'fontWeight': 'bold',
                    'padding': '10px'
                },
                children='Weapons'
            ),
            # Add a div to display the list of countries
            html.Div(id='weapons-list')
        ]
    ),
    html.Div([
    dcc.Graph(
        id='map',
        figure=px.scatter_mapbox(
            lat=latitude,
            lon=longitude,
            size=size,
            zoom=3,
            mapbox_style='open-street-map'
        )
    )
])
])


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=False)