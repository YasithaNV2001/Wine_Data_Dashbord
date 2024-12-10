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

        # Tabs for Analysis
        dcc.Tabs([
            dcc.Tab(label="Price Analysis", children=[
                dbc.Row([
                    dbc.Col(dcc.Graph(id='price-histogram', style={'padding': '20px'})),
                    dbc.Col(dcc.Graph(id='ratings-scatter', style={'padding': '20px'})),
                ])
            ]),
            dcc.Tab(label="Food & Alcohol Analysis", children=[
                dbc.Row([
                    dbc.Col(dcc.Graph(id='food-pairings-bar', style={'padding': '20px'})),
                    dbc.Col(dcc.Graph(id='alcohol-boxplot', style={'padding': '20px'})),
                ])
            ]),
            dcc.Tab(label="Wine Styles", children=[
                dbc.Row([
                    dbc.Col(dcc.Graph(id='wine-style-pie', style={'padding': '20px'})),
                ])
            ]),
            dcc.Tab(label="NLP Analysis", children=[
                dbc.Row([
                    dbc.Col(dcc.Graph(id='nlp-bar-chart', figure=nlp_bar_fig, style={'padding': '20px'})),
                ])
            ])
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

# Callback for Filter Panel Toggle
@app.callback(
    Output("filter-panel", "style"),
    Input("filter-toggle", "n_clicks"),
    prevent_initial_call=True
)
def toggle_filters(n_clicks):
    if n_clicks % 2 == 0:
        return {"display": "block", "border": "1px solid #ccc", "padding": "10px", "borderRadius": "5px"}
    else:
        return {"display": "none"}

# Callback for Chart Updates
@app.callback(
    [Output('price-histogram', 'figure'),
     Output('ratings-scatter', 'figure'),
     Output('food-pairings-bar', 'figure'),
     Output('alcohol-boxplot', 'figure'),
     Output('wine-style-pie', 'figure')],
    [Input('country-dropdown', 'value'),
     Input('wine-style-dropdown', 'value'),
     Input('price-slider', 'value')]
)
def update_charts(selected_countries, selected_styles, price_range):
    filtered_df = wine_df[
        (wine_df['Price'] >= price_range[0]) & (wine_df['Price'] <= price_range[1])
    ]
    if selected_countries:
        filtered_df = filtered_df[filtered_df['Country'].isin(selected_countries)]
    if selected_styles:
        filtered_df = filtered_df[filtered_df['Wine style'].isin(selected_styles)]

    # Price Distribution Chart
    hist_fig = px.histogram(
        filtered_df, x='Price', color='Country',
        title="Price Distribution by Country",
        nbins=30, color_discrete_sequence=px.colors.sequential.Agsunset
    )

    # Ratings vs Price Scatter Plot
    scatter_fig = px.scatter_3d(
        filtered_df, x='Price', y='Rating', z='Number of Ratings',
        color='Country', title="Ratings vs Price",
        hover_name='Name'
    )
    # Popular Food Pairings Bar Chart
    food_counts = filtered_df['Food pairings'].explode().value_counts()
    bar_fig = px.bar(
        food_counts, x=food_counts.index, y=food_counts.values,
        title="Popular Food Pairings", labels={'x': 'Food', 'y': 'Count'},
        text_auto=True, color=food_counts.values, color_continuous_scale='Viridis'
    )
    # Alcohol Content Box Plot
    box_fig = px.box(
        filtered_df, x='Country', y='Alcohol content', color='Country',
        title="Alcohol Content by Country", color_discrete_sequence=px.colors.qualitative.Safe
    )
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)