import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
df=pd.read_csv(r'formatted_sales_data.csv')
SoulFoods_dash=dash.Dash(__name__)
figure=px.line(df,x='date',y='sales',color='region')
price_increase_date = pd.to_datetime('2021-01-15')
SoulFoods_dash.layout = [html.H1(children="Pink morsel sales data", style={'textAlign':'center', 'fontFamily':'Georgia', 'fontSize':'35px'}),dcc.Graph(figure=figure)]
if __name__=='__main__':
    SoulFoods_dash.run(debug=True)
