import dash
import base64
from dash import html , dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import pickle
from dash.dependencies import Input, Output, State
from dash import callback

import warnings
warnings.simplefilter("ignore", UserWarning)
register_page(__name__, path="/model")
#comfama1='comfama1.jpg'
#encoded_comfama1=base64.b64encode(open(comfama1,'rb').read()).decode('ascii')

with open('model_pkl', 'rb') as f:
    clf = pickle.load(f)
    


layout= dbc.Container(
    [
        dbc.Row([
            dbc.Col(html.Label('Cantidad_trabajadores_UP'), width=2),
            dbc.Col(dcc.Input(id='input_Cantidad_trabajadores_UP', type='number', placeholder='12', style={'width': '100%'})),
            dbc.Col(html.Label('Cantidad_PAC_UP'), width=2),
            dbc.Col(dcc.Input(id='input_Cantidad_PAC_UP', type='number', placeholder='10', style={'width': '100%'})),
        ], style={"margin-top": "25px"}),
        
        dbc.Row([
            dbc.Col(html.Label('Cantidad_Conyuges_UP'), width=2),
            dbc.Col(dcc.Input(id='input_Cantidad_Conyuges_UP', type='number', placeholder='10', style={'width': '100%'})),
            dbc.Col(html.Label('Aporte_Pagado_UP'), width=2),
            dbc.Col(dcc.Input(id='input_Aporte_Pagado_UP', type='number', placeholder='85000', style={'width': '100%'})),
        ], style={"margin-top": "25px"}),
        
        dbc.Row([
            dbc.Col(html.Label('Subsidio_Pagado_UP'), width=2),
            dbc.Col(dcc.Input(id='input_Subsidio_Pagado_UP', type='number', placeholder='-35000', style={'width': '100%'})),
            dbc.Col(html.Label('AportesPromedio'), width=2),
            dbc.Col(dcc.Input(id='input_AportesPromedio', type='number', placeholder='34000', style={'width': '100%'})),
        ], style={"margin-top": "25px"}),
        
        dbc.Row([
            dbc.Col(html.Label('SubsidioPromedio'), width=2),
            dbc.Col(dcc.Input(id='input_SubsidioPromedio', type='number', placeholder='-30000', style={'width': '100%'})),
            dbc.Col(html.Label('MesesAfiliado'), width=2),
            dbc.Col(dcc.Input(id='input_MesesAfiliado', type='number', placeholder='36', style={'width': '100%'})),
        ], style={"margin-top": "25px"}),        
        
        dbc.Row([
            dbc.Col(html.Label('AporteMenor'), width=2),
            dbc.Col(dcc.Input(id='input_AporteMenor', type='number', placeholder='1 Si Aporte actual < Aporte periodo anterior, sino 0', style={'width': '100%'})),
            dbc.Col(html.Label('SubsidioMenor'), width=2),
            dbc.Col(dcc.Input(id='input_SubsidioMenor', type='number', placeholder='1 Si Subsidio actual < Subsidio periodo anterior, sino 0', style={'width': '100%'})),
        ], style={"margin-top": "25px"}),
        
        dbc.Row([
            dbc.Col(html.Label('Recompra'), width=2),
            dbc.Col(dcc.Input(id='input_Recompra', type='number', placeholder='1', style={'width': '100%'})),
            dbc.Col(width=2),
            dbc.Col(),
        ], style={"margin-top": "25px"}),    
        
        html.Button(id='submit_button', name='submit_button', n_clicks=0, children='Submit',  style={'width': '30%', "margin-top": "25px"}),
        html.Br(),
        dbc.Row([html.Div(id='prediction_output')])
    ])    
        
@callback(
    Output('prediction_output', 'children'),
    Input('submit_button', 'n_clicks'),
    State('input_Cantidad_trabajadores_UP', 'value'),
    State('input_Cantidad_PAC_UP', 'value'),
    State('input_Cantidad_Conyuges_UP', 'value'),
    State('input_Aporte_Pagado_UP', 'value'),
    State('input_Subsidio_Pagado_UP', 'value'),
    State('input_AportesPromedio', 'value'),
    State('input_SubsidioPromedio', 'value'),
    State('input_MesesAfiliado', 'value'),
    State('input_AporteMenor', 'value'),
    State('input_SubsidioMenor', 'value'),
    State('input_Recompra', 'value'),
)


def update_output(n_clicks, Cantidad_trabajadores_UP, Cantidad_PAC_UP, Cantidad_Conyuges_UP, Aporte_Pagado_UP, Subsidio_Pagado_UP, AportesPromedio, SubsidioPromedio, MesesAfiliado, AporteMenor, SubsidioMenor, Recompra):
    if n_clicks > 0:
        if Cantidad_trabajadores_UP is None:
            Cantidad_trabajadores_UP = 0
        if Cantidad_PAC_UP is None:
            Cantidad_PAC_UP = 0
        if Cantidad_Conyuges_UP is None:
            Cantidad_Conyuges_UP = 0
        if Aporte_Pagado_UP is None:
            Aporte_Pagado_UP = 0
        if Subsidio_Pagado_UP is None:
            Subsidio_Pagado_UP = 0
        if AportesPromedio is None:
            AportesPromedio = 0
        if SubsidioPromedio is None:
            SubsidioPromedio = 0
        if MesesAfiliado is None:
            MesesAfiliado = 0
        if AporteMenor is None:
            AporteMenor = 0
        if SubsidioMenor is None:
            SubsidioMenor = 0
        if Recompra is None:
            Recompra = 0
        prediction = clf.predict([[Cantidad_trabajadores_UP, Cantidad_PAC_UP, Cantidad_Conyuges_UP, Aporte_Pagado_UP, Subsidio_Pagado_UP, AportesPromedio, SubsidioPromedio, MesesAfiliado, AporteMenor, SubsidioMenor, Recompra]])
        return html.Div([html.H4('Prediction: {}'.format('Vigente' if prediction == 1 else 'Retirada'))], style={"margin-top": "25px"})
    else:
        return html.Div([html.H4('Prediction:')], style={"margin-top": "25px"})