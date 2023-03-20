from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from .coincap_api import coin_symbol2id
from . import ids


def render(app: Dash) -> html.Div:
    coins = list(coin_symbol2id.keys())

    @app.callback(
        Output(ids.COINS_DROPDOWN, "value"),
        Input(ids.COINS_DROPDOWN, "value"),
    )
    def select_coin(_: str) -> str:
        return _

    return html.Div(
        children=[
            html.H6("Coin"),
            dcc.Dropdown(
                id=ids.COINS_DROPDOWN,
                options=coins,
                value='BTC',
                multi=False,
                placeholder="Select a coin"
            )
        ]
    )
