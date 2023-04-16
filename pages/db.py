import io 
import base64
import pandas as pd
import matplotlib.pyplot as plt
from h2o_wave import ui, data

from utils.load_data import load_data

# Load dataset
df = load_data("train.csv")
df.dropna(inplace=True)
df.sort_values(by=['StateCode', 'StationId', 'Date'], inplace=True)
df.StationId = df.StationId.astype('str')
df.Date = df.Date.astype('str')
state_count = df.StateCode.value_counts(normalize=True)
state_count = state_count.reset_index()
state_count['color'] = ['#FF0000', '#FFA500', '#5B616A', '#008000', '#0000FF', '#800080']
df.set_index(["StateCode", "StationId"], inplace=True)
df.rename(columns={'PM2.5': 'PM2_5'}, inplace=True)

aqi_levels = pd.DataFrame({'AQI_Levels': [50, 100, 200, 300, 400, 500], 'column': ['AQI', 'AQI', 'AQI', 'AQI', 'AQI', 'AQI'], 'level': ['Good', 'Satisfactory', 'Moderately polluted', 'Poor', 'Very Poor', 'Severe']})

state_dict = { 'AS': 'Assam', 'DL': 'Delhi', 'KA': 'Karnataka', 'MH': 'Maharastra', 'TN': 'Tamil Nadu', 'WB': 'West Bengal' }
state_count['state'] = state_count['StateCode'].map(state_dict)

states = [
    ui.choice('AS', 'Assam'),
    ui.choice('DL', 'Delhi'),
    ui.choice('KA', 'Karnataka'),
    ui.choice('MH', 'Maharastra'),
    ui.choice('TN', 'Tamil Nadu'),
    ui.choice('WB', 'West Bengal')
]

stations = {'AS': [4],
            'DL': [4, 6, 8, 12, 13, 18, 19, 21, 23, 25, 26, 27, 29, 30, 32, 35, 38, 39, 40, 41],
            'KA': [7, 9, 10, 11, 14],
            'MH': [10, 11, 12, 13, 14, 15, 16, 17],
            'TN': [5, 8],
            'WB': [12, 13, 14, 16]}

cols = [
    ui.choice('SO2', 'SO2'),
    ui.choice('O3', 'O3'),
    ui.choice('CO', 'CO'),
    ui.choice('PM10', 'PM10'),
    ui.choice('PM2_5', 'PM2.5'),
    ui.choice('AQI', 'AQI')
]

color_palette = {
    'SO2': '#FF0000',
    'O3': '#FFA500',
    'CO': '#5B616A',
    'PM10': '#008000',
    'PM2_5': '#0000FF',
    'AQI': '#800080'
}

def state_pie_chart(q):
    pie_list = [ui.pie(label=f"{value['index']}", value=f"", fraction=value['StateCode'], color=value['color']) for key, value in state_count.iterrows()]
    state_pie = ui.wide_pie_stat_card(
        box='state_pie',
        title='State Distribution',
        pies=pie_list,
    )
    return state_pie

def state_aqi_chart(q):
    tb = df.reset_index()

    # aqi_level_bar = ui.plot_card(
    #     box = 'state_aqi',
    #     title='State-AQI Levels',
    #     data=data(fields=aqi_levels.columns.tolist(), rows=aqi_levels.values.tolist()),
    #     plot=ui.plot([
    #         ui.mark(type='interval', x='=AQI_Levels', y='=column', label='=level', color='level', stack='auto', label_position='middle', x_nice=True),
    #         ]))
    # return aqi_level_bar

## ------------------ AQI Plot ------------------ ##
def aqi_level_bar(q):
    aqi_level_bar = ui.plot_card(
        box = 'aqi_level',
        title='AQI Levels',
        data=data(fields=aqi_levels.columns.tolist(), rows=aqi_levels.values.tolist()),
        plot=ui.plot([
            ui.mark(type='interval', x='=AQI_Levels', y='=column', label='=level', color='level', stack='auto', label_position='middle', x_nice=True),
            ]))
    return aqi_level_bar

## ------------------ All Features Plot ------------------ ##
def ss_state_bar_menu(q):
    ss_state_bar = ui.form_card(
            box = ui.box('ss_sidebar'),
            items=[
                ui.dropdown(name='ss_state', label='State (Single)', value=f'{q.client.ss_state}', required=True, choices=states, trigger=True),
            ])
    return ss_state_bar

def ss_station_bar_menu(q):
    ss_station_bar = ui.form_card(
        box = ui.box('ss_sidebar'),
        items=[
            ui.dropdown(name='ss_station', label='Station (Single)', value=q.client.ss_station, required=True, choices=[ui.choice(str(stn), str(stn)) for stn in stations[q.client.ss_state]], trigger=True)
        ])
    return ss_station_bar

def ss_col_bar_menu(q):
    ss_col_bar = ui.form_card(
        box = ui.box('ss_sidebar'),
        items=[
            ui.dropdown(name='ss_col', label='Feature (Multiple)', values=q.client.ss_col, required=True, choices=cols, trigger=True)
        ])
    return ss_col_bar

def plot_ss_cols(q):
    tb =  df.loc[(q.client.ss_state, q.client.ss_station), ['Date'] + q.client.ss_col]
    tb.reset_index(inplace=True)
    lines = [ui.mark(type='line', x='=Date', y=f'={column}', x_scale='time', color=color_palette[column], label=column.replace("_", "."), size="100%") for column in tb.columns[3:]]
    ss_aqi_plot = ui.plot_card(
            box = 'ss_body', 
            title = 'Distribution Plot', 
            data = data(
                    fields = tb.columns.tolist(), 
                    rows = tb.values.tolist()),
            plot = ui.plot(lines))
    return ss_aqi_plot

## ---------------------------- State Station Plot ---------------------------- ##

def state_bar_menu(q):
    state_bar = ui.form_card(
            box = ui.box('sidebar'),
            items=[
                ui.dropdown(name='state', label='State (Single)', value=f'{q.client.state}', required=True, choices=states, trigger=True),
            ])
    return state_bar

def station_bar_menu(q):
    station_bar = ui.form_card(
        box = ui.box('sidebar'),
        items=[
            ui.dropdown(name='station', label='Station (Multiple)', values=q.client.station, required=True, choices=[ui.choice(str(stn), str(stn)) for stn in stations[q.client.state]], trigger=True)
        ])
    return station_bar


def plot_aqi(q):
    tb =  df.loc[(q.client.state, list(q.client.station)), ['Date', 'AQI']]
    tb.reset_index(inplace=True)
    aqi_plot = ui.plot_card(
            box = 'body', 
            title = 'AQI Plot', 
            data = data(
                    fields = tb.columns.tolist(), 
                    rows = tb.values.tolist()),
            plot = ui.plot([ui.mark(type='path', x='=Date', y='=AQI', x_scale='time', color='=StationId', size="100%")]))
    return aqi_plot


## ---------------------------- Markdown ---------------------------- ##
ss_md = '''=
## Distribution of Different Features in the Dataset
<hr/>
This section shows the distribution of different features in the dataset. The features are selected from the dropdown menu on the left. The plot shows the distribution of the selected features for the selected state and station.
'''

aqi_md = '''=
## AQI Dsitribution for State-Station Pairs
<hr/>
This section shows the AQI distribution for the selected state and station. The stations are selected from the dropdown menu on the left. The plot shows the AQI distribution for the multiple selected stations and the selected state.
'''

aqi_level_md = '''=
## AQI Levels
<hr/>
This section shows the AQI levels and their corresponding health impacts.

| AQI Level | Health Impacts |
|:---------|:--------------|
| 0 - 50 (Good)    | Minimal Impact           |
| 51 - 100 (Satisfactory)  | May cause minor breathing discomfort to sensitive people.   |
| 101 - 200 (Moderately Polluted) | May cause breathing discomfort to people with lung disease such as asthma, and discomfort to people with heart disease, children and older adults. |
| 201 - 300 (Poor) | May cause breathing discomfort to people on prolonged exposure, and discomfort to people with heart disease           |
| 301 - 400 (Very Poor) | May cause respiratory illness to the people on prolonged exposure. Effect may be more pronounced in people with lung and heart diseases.      |
| 401 - 500 (Severe) | May cause respiratory effects even on healthy people and serious health impacts on people with lung/heart diseases. The health impacts may be experienced even during light physical activity         |
'''

ss_md_zone = ui.markdown_card(
    box = 'ss_mardown',
    title = '',
    content = ss_md
)

aqi_md_zone = ui.markdown_card(
    box = 'aqi_mardown',
    title = '',
    content = aqi_md
)

aqi_level_md_zone = ui.markdown_card(
    box = 'aqi_level_md',
    title = '',
    content = aqi_level_md
)


'''
    # plt.figure(figsize=(10,10))
    # plt.pie(state_count.StateCode, labels=state_count.state, autopct='%1.2f%%')
    # # Convert to base64.
    # pic_IObytes = io.BytesIO()
    # plt.savefig(pic_IObytes,  format='png')
    # pic_IObytes.seek(0)
    # image = base64.b64encode(pic_IObytes.read()).decode()
    # state_pie = ui.image_card(box='state_pie', title='Statewise Distribution', image=image, type='png')
    # return state_pie
'''