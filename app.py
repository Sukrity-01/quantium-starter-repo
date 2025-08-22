import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Load and prepare data
df = pd.read_csv(r'formatted_sales_data.csv')
df['date'] = pd.to_datetime(df['date'])

# Initialize app
SoulFoods_dash = dash.Dash(__name__)

# Layout
SoulFoods_dash.layout = html.Div([
    html.H1(
        children="Pink Morsel Sales",
        style={
            'textAlign': 'center',
            'fontFamily': 'Georgia',
            'fontSize': '35px',
            'color': '#99B3F7',
            'padding': '10px',
            'marginBottom': '20px',
        }
    ),

    html.Div([
        html.Label('Select Region:', style={'fontWeight': 'bold', 'fontSize': '16px'}),
        dcc.RadioItems(
            id='region',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'North'},
                {'label': 'South', 'value': 'South'},
                {'label': 'East', 'value': 'East'},
                {'label': 'West', 'value': 'West'},
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'marginRight': '15px',
                        'fontWeight': 'bold', 'fontSize': '16px'},
        )
    ], style={'textAlign': 'center', 'marginBottom': '20px'}),

    dcc.Graph(id='sales-graph'),
],
    style={'backgroundColor': '#f8f9fa',
           'padding': '20px',
           'borderRadius': '12px'}
)

# Callback
@SoulFoods_dash.callback(
    Output('sales-graph', 'figure'),
    Input('region', 'value')
)
def update_graph(region):
    df['region'] = df['region'].str.strip().str.title()
    # Filter by region
    if region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == region]

    # Build figure
    figure = px.line(filtered_df, x='date', y='sales', color='region')

    # Add price increase marker (convert to numpy datetime to avoid warning)
    price_increase_date = pd.to_datetime('2021-01-15').to_pydatetime().timestamp()
    figure.add_vline(
        x=price_increase_date,
        line_width=2,
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase",
        annotation_position="top right"
    )

    # Layout styling
    figure.update_layout(
        template="plotly_dark",
        font=dict(family="Georgia", size=14),
        title=dict(x=0.5, text="Sales Over Time"),
        xaxis=dict(
            title="Date",
            type="date",
            range=[filtered_df['date'].min(), filtered_df['date'].max()]
        ),
        yaxis=dict(title="Sales")
    )

    return figure


if __name__ == '__main__':
    SoulFoods_dash.run(debug=True)
