import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go


# Data Loading
data_path = "https://raw.githubusercontent.com/YasithaNV2001/Wine_Data_Dashbord/refs/heads/main/notebooks/data/processed/process_wine_data.csv"
wine_df = pd.read_csv(data_path)

nlp_data_path = "https://raw.githubusercontent.com/YasithaNV2001/Wine_Data_Dashbord/refs/heads/main/HuggingFaceModel/wine_data_reviews_with_labels.csv"
nlp_wine_df = pd.read_csv(nlp_data_path)


category_counts = nlp_wine_df["talks_about"].value_counts()

# NLP Bar Chart
nlp_bar_fig = go.Figure([go.Bar(
    x=category_counts.index,
    y=category_counts.values,
    marker=dict(color='skyblue')
)])
nlp_bar_fig.update_layout(
    title="Distribution of Review Categories from NLP",
    xaxis_title="Category",
    yaxis_title="Count"
)



# App Initialization
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Wine Analytics Dashboard"



# Layout with header
app.layout = html.Div(
    children=[
        # Header section
        html.Div(
            children=[
                html.Img(
                    src="assets/rb_118902.png",
                    style={"height": "100px", "width" : "100px", "marginBottom": "30px"} 
                ),
                html.Div(
                    children=[
                        html.H1(
                            "Wine Analytics Dashboard",
                            style={
                                'color': '#ffffff',
                                'fontWeight': 'bold',
                                'margin': '0'
                            }
                        ),
                        html.P(
                            "Explore insights and visualizations on wine analytics.",
                            style={
                                'color': '#ffffff',
                                'margin': '0'
                            }
                        ),
                    ],
                    style={
                        "flex": "1",
                        "textAlign": "center"
                    }
                )
            ],
            style={
                "display": "flex",
                "alignItems": "center",
                "flexDirection": "column",
                "justifyContent": "center",
                "padding": "20px 20px 20px 20px",
                "background": "#00072D",
                "borderRadius": "10px",
                "margin": "10px 30px 20px 30px",
                "width": "96.5vw",  # Full viewport width
                # "boxSizing": "border-box",
            }
        ),
        
        # Filter Section
        html.Div([   
            html.Button("Toggle Filters", id="filter-toggle", style={
                "backgroundColor": "#007bff", "color": "white", "padding": "10px", "border": "none",
                "borderRadius": "5px", "cursor": "pointer" ,"margin": "10px"
            }),
            html.Div(
                id="filter-panel",
                children=[
                    # Filter Inputs
                    html.Div([
                        html.Label("Select Country:", style={'fontWeight': 'bold'}),
                        dcc.Dropdown(
                            id='country-dropdown',
                            options=[{'label': c, 'value': c} for c in sorted(wine_df['Country'].unique())],
                            value=[],
                            placeholder="Select one or more countries",
                            multi=True
                        ),
                    ], style={'padding': '10px'}),
                    
                    html.Div([
                        html.Label("Select Wine Style:", style={'fontWeight': 'bold'}),
                        dcc.Dropdown(
                            id='wine-style-dropdown',
                            options=[{'label': s, 'value': s} for s in sorted(wine_df['Wine style'].unique())],
                            value=[],
                            placeholder="Select wine style(s)",
                            multi=True
                        ),
                    ], style={'padding': '10px'}),
                    
                    html.Div([
                        html.Label("Price Range (USD):", style={'fontWeight': 'bold'}),
                        dcc.RangeSlider(
                            id='price-slider',
                            min=wine_df['Price'].min(),
                            max=wine_df['Price'].max(),
                            marks={int(p): f"${int(p)}" for p in range(0, int(wine_df['Price'].max()), 10)},
                            step=1,
                            value=[wine_df['Price'].min(), wine_df['Price'].max()]
                        ),
                    ], style={'padding': '10px'}),
                ],
                style={'background': 'linear-gradient(to bottom, #33ccff 0%, #ff99cc 100%)',"display": "block", "border": "1px solid #ccc", "padding": "10px", "borderRadius": "5px", "margin": "10px 30px 20px 30px"}
            )
        ]),

        html.Footer(
            "Dashboard by Team Name",
            style={
                "display": "flex",
                "alignItems": "center",
                "textColor": "#ffffff",
                "flexDirection": "column",
                "justifyContent": "center",
                "width": "96.5vw",
                "padding": "20px 20px 20px 20px",
                'textAlign': 'center',
                'marginTop': '100vh',
                "marginLeft": "30px",
                "marginRight": "30px",
                "borderRadius": "10px",
                'backgroundColor': '#00072D'}
        )

    ],
    style={
        "fontFamily": "Akrobat, sans-serif",
        "maxWidth": "900px",
        "margin": "0",
        "paddingBottom": "20px"
    }
),





# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)