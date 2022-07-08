import dash
import base64
from dash import html , dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page


register_page(__name__, path="/")
#comfama1='comfama1.jpg'
#encoded_comfama1=base64.b64encode(open(comfama1,'rb').read()).decode('ascii')

layout= dbc.Container(
    [
        dbc.Row([
            dbc.Col([
            html.H3(['Storytelling: COMFAMA and the microbusiness withdrawal'],id="div_title_storytelling")]
                , lg=12)]
                )
        ,    
        dbc.Row([
            dbc.Col([
            dcc.Markdown(
            ''' *The dawn of a great story*
            
            It's the beautiful summer of 1963 (?). Antioquia, the
            beautiful mountainous region in the center-west of
            Colombia is enjoying one of its most beautiful periods
            ever, with a bunch of buoyant and skillful people
            trying to draw out the very best of their 
            fields and their newly-acquired tech, which came due 
            to the efforts of the very-loved yet controversial 
            dictator Rojas Pinilla. Deep within the still 
            precarious town of La Estrella, a real star for
            Antioquia is about to be born. It is not merely a 
            recognized singer, an acclaimed politician or a 
            famous football icon. It is the very first welfare 
            fund that this amazing region will ever have: Caja de
            Compensación Familiar de Antioquia, COMFAMA.
                       
                       
                      
            '''
            )] , lg=6),
            
            dbc.Col([
            html.Img(src='assets/comfama1.jpg')
        ],md=6)
        
       
        ]),
        
        dbc.Row([
            
            dbc.Col([
            html.Img(src='assets/comfama2.jpg'),
        ],md=6,style={'textAlign': 'center'}),
            
                dbc.Col([
            dcc.Markdown(
            ''' *An unseen threat to COMFAMA's services*
            
            
            During many years, COMFAMA has been the glue for 
            Antioquia's many businesses, providing services to 
            their employees and allowing them to enjoy several 
            benefits that did not have before at reasonable 
            prices. This was, of course, an excellent way into
            everyone's hearts.
            
            And yet, an unseen enemy has threated COMFAMA's
            continued welldoing for the middle class: desertion. 
            
            Since 2017, COMFAMA has noted that different kinds
            of microbusinesses have been withdrawing, and it is
            certainly counter-intuitive that anyone would leave
            COMFAMA on its own. But then, why would any business
            finish this beautiful relationship? And more
            importantly, is it possible to predict if anyone is
            about to break-up with COMFAMA? What can be those
            signals that alert a possible withdrawal?
            
            That's where *we* come in. Our story is not 
            important, for the time being. We are four different
            people, gathered together by destiny (and DS4A, of 
            course) in an working group to help COMFAMA, the
            microbusinesses,and Antioquia. We're here to 
            understand the behavior of data and to predict 
            dropouts before they occur. We have a fierce will,
            lots of knowledge acquired during and before DS4A,
            and a strong desire to see this project through.
            We are Team 104.
                       
                      
            '''
            )] , lg=6)]
                ),
        
         dbc.Row([
                dbc.Col([
            dcc.Markdown(
            ''' *Data delivered: what we know about this phantom menace*
            
            
            We have obtained a full dataset that seeks to
            describe the relationship between microbusinesses
            of all Antioquia who are affiliated to COMFAMA. For
            these, we can observe three kinds of variables:
            
            1. Categorical variables: such as our dependent 
            variable (*Estado*) to check if they have retired 
            or not, Economic sector, Municipality.
            
            2. Continuous variables: Integers or rational 
            numbers concerning variables such as contributions 
            paid to COMFAMA, subsidies paid to he microbusiness,
            number of workers, number of affiliated months,
            etc.
            
            3. Others: such as retirement dates and
            microbusiness ID.
            
            Before jumping to any conclusion about our model,
            we will look at the behavior of this data to 
            understand relationships between variables.
                      
            '''
            )] , lg=6),
            
            dbc.Col([
            html.Img(src='assets/comfama3.jpg')
        ],md=6)]
                ),
        
       
        
        
        dbc.Row([
            
            dbc.Col([
            html.Img(src='assets/EDA1.png'),
        ],md=6,style={'textAlign': 'center'}),
            
                dbc.Col([
            dcc.Markdown(
            ''' *Foreseeing modelling issues*
            
            Starting at our main response variable
            During many years, COMFAMA has been the glue for 
            Antioquia's many businesses, providing services to 
            their employees and allowing them to enjoy several 
            benefits that did not have before at reasonable 
            prices. This was, of course, an excellent way into
            everyone's hearts.
            
            
                       
                      
            '''
            )] , lg=6)]
                ),
        
         dbc.Row([
                dbc.Col([
            dcc.Markdown(
            ''' *Data delivered: what we know about this phantom menace*
            
            
            We have obtained a full dataset that seeks to
            describe the relationship between microbusinesses
            of all Antioquia who are affiliated to COMFAMA. For
            these, we can observe three kinds of variables:
            
            1. Categorical variables: such as our dependent 
            variable (*Estado*) to check if they have retired 
            or not, Economic sector, Municipality.
            
            2. Continuous variables: Integers or rational 
            numbers concerning variables such as contributions 
            paid to COMFAMA, subsidies paid to he microbusiness,
            number of workers, number of affiliated months,
            etc.
            
            3. Others: such as retirement dates and
            microbusiness ID.
            
            Before jumping to any conclusion about our model,
            we will look at the behavior of this data to 
            understand relationships between variables.
                      
            '''
            )] , lg=6),
            
            dbc.Col([
            html.Img(src='assets/EDA2.png')
        ],md=6)]
                ),
        
        dbc.Row([
            
            dbc.Col([
            html.Img(src='assets/EDA3.png'),
        ],md=6,style={'textAlign': 'center'}),
            
                dbc.Col([
            dcc.Markdown(
            ''' *An unseen threat to COMFAMA's services*
            
            
            During many years, COMFAMA has been the glue for 
            Antioquia's many businesses, providing services to 
            their employees and allowing them to enjoy several 
            benefits that did not have before at reasonable 
            prices. This was, of course, an excellent way into
            everyone's hearts.
            
            And yet, an unseen enemy has threated COMFAMA's
            continued welldoing for the middle class: desertion. 
            
            Since 2017, COMFAMA has noted that different kinds
            of microbusinesses have been withdrawing, and it is
            certainly counter-intuitive that anyone would leave
            COMFAMA on its own. But then, why would any business
            finish this beautiful relationship? And more
            importantly, is it possible to predict if anyone is
            about to break-up with COMFAMA? What can be those
            signals that alert a possible withdrawal?
            
            That's where *we* come in. Our story is not 
            important, for the time being. We are four different
            people, gathered together by destiny (and DS4A, of 
            course) in an working group to help COMFAMA, the
            microbusinesses,and Antioquia. We're here to 
            understand the behavior of data and to predict 
            dropouts before they occur. We have a fierce will,
            lots of knowledge acquired during and before DS4A,
            and a strong desire to see this project through.
            We are Team 104.
                       
                      
            '''
            )] , lg=6)]
                ),
        
        dbc.Row([
            dbc.Col([
            dcc.Markdown(
            ''' *The dawn of a great story*
            
            It's the beautiful summer of 1963 (?). Antioquia, the
            beautiful mountainous region in the center-west of
            Colombia is enjoying one of its most beautiful periods
            ever, with a bunch of buoyant and skillful people
            trying to draw out the very best of their 
            fields and their newly-acquired tech, which came due 
            to the efforts of the very-loved yet controversial 
            dictator Rojas Pinilla. Deep within the still 
            precarious town of La Estrella, a real star for
            Antioquia is about to be born. It is not merely a 
            recognized singer, an acclaimed politician or a 
            famous football icon. It is the very first welfare 
            fund that this amazing region will ever have: Caja de
            Compensación Familiar de Antioquia, COMFAMA.
                       
                       
                      
            '''
            )] , lg=6),
            
            dbc.Col([
            html.Img(src='assets/EDA4.png')
        ],md=6)
        
       
        ])
        
        
    ])    
        
    

