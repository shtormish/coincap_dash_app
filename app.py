from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP, SLATE
from werkzeug.debug import DebuggedApplication

from src.components.layout import create_layout

# from src.components.data import 


def main() -> None:
    app = Dash(external_stylesheets=[SLATE])
    app.title = "Coin Prices"
    app.layout = create_layout(app)
    app.run_server(debug=True)
    return app
    
app = main()


if __name__ == "__main__":
    main()