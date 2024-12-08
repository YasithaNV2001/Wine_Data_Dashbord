import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

data_path = "notebooks\data\processed\process_wine_data_with_food_pairings.csv"
wine_df = pd.read_csv(data_path)

nlp_data_path = "notebooks\data\processed\process_wine_data.csv"
nlp_wine_df = pd.read_csv(nlp_data_path)

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
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)