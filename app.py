from jupyter_dash import JupyterDash
import dash_bootstrap_components as dbc

app = JupyterDash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server