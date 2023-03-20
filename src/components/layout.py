from dash import Dash, html
import dash_bootstrap_components as dbc

from . import bar_chart, coins_dropdown, dates


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title, style={'textAlign': 'center'}),
            html.Hr(),
            dbc.Row([
                dbc.Col([
                    dbc.Row(
                        html.Div(
                            className="dropdown-container",
                            children=[
                                coins_dropdown.render(app),
                            ]
                        )
                    ),
                    dbc.Row(
                        html.Div(
                            className="date-range-selector",
                            children=[
                                dates.render(app),
                            ]
                        ),
                    )
                ], width=4),
                dbc.Col([
                    bar_chart.render(app),
                ], width=8)
            ])
        ],
    )
