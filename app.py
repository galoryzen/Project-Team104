#libraries
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
import os
import pickle

#from callbacks import register_callbacks
    
# Dash instance declaration
dash_app = dash.Dash(__name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.LUX],)
app = dash_app.server

#Top menu, items get from all pages registered with plugin.pages
navbar = dbc.NavbarSimple([

    dbc.NavItem(dbc.NavLink( "Storytelling - EDA", href='/')),
    dbc.NavItem(dbc.NavLink( "Model", href='/model')), 
    ],
    brand="DS4A Project - Team 104",
    color="primary",
    dark=True,
    className="mb-2",
)

#Main layout
dash_app.layout = dbc.Container(
    [
        navbar,
        dl.plugins.page_container,
    ],
    className="dbc",
    fluid=True,
)

# Call to external function to register all callbacks
#register_callbacks(app)


#This call will be used with Gunicorn server
#server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    dash_app.run_server(debug=False)
    
    