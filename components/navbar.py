from h2o_wave import ui

def nav():
    header = ui.header_card(
        box='header', 
        title='AQI Forecasting', 
        subtitle='H2O Hackathon',
        image='https://wave.h2o.ai/img/h2o-logo.svg',
        items=[
            ui.link(path='#home', label='Home', width="60px"),
            ui.link(path='#dashboard', label='Dashboard', width="90px"),
            ui.link(path='#solution', label='Solution', width="75px"),
            ui.link(path='#appendix', label='Appendix', width="75px"),
        ])
    return header