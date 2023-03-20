import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from .coincap_api import get_coin_price, coin_symbol2id

from . import ids

COINS_DROPDOWN = get_coin_price()


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [Input(ids.COINS_DROPDOWN, "value"),
        Input(ids.DATES, "start_date"),
        Input(ids.DATES, "end_date")
        ]
    )
    def update_bar_chart(coin: str, start_date, end_date) -> html.Div:
        data = get_coin_price(coin_symbol=coin, start=start_date, end=end_date)

        if data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.BAR_CHART)

        fig = px.bar(data, x="date", y="priceUsd")

        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)