from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from datetime import date, timedelta

from . import ids


def render(app: Dash) -> html.Div:

    return html.Div(
        children=[
            html.H6("Date region"),
            dcc.DatePickerRange(
                id=ids.DATES,
                min_date_allowed=date(2012, 5, 1),
                max_date_allowed=date.today(),
                # initial_visible_month=date.today(),
                start_date=date.today() - timedelta(days=30),
                end_date=date.today(),
            )
        ]
    )
