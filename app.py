from h2o_wave import app, main, Q
from components.navbar import nav
from components.footer import foot
from components.layout_responsive import meta_layout
from pages import db, appendix, home, solution

@app('/site')
async def server(q: Q):
    q.page['meta'] = await q.run(meta_layout, q)
    q.page['header'] = await q.run(nav)
    q.page['footer'] = await q.run(foot)
    
    hash = q.args['#']
    
    if (hash is None) or (hash == "home"):
        q.page['home_page'] = home.home_page
    elif hash == "dashboard":
        # q.page['state_pie'] = await q.run(db.state_pie_chart, q)
        q.page['ss_mardown'] = db.ss_md_zone
        q.page['aqi_mardown'] = db.aqi_md_zone
        q.page['aqi_level_md'] = db.aqi_level_md_zone

        ## ------------------ AQI Level Distribution ------------------ ##
        q.page['aqi_level'] = await q.run(db.aqi_level_bar, q)

        ## ------------------ Cache the State-Station Pairs ------------------ ##
        if q.client.ss_state is None:
            q.client.ss_state = 'AS'
            q.client.ss_station = None
        if q.client.ss_col is None:
            q.client.ss_col = ['O3']

        if q.args.ss_state:
            if q.client.ss_state != q.args.ss_state:
                q.args.ss_station = None
            q.client.ss_state = q.args.ss_state
            q.client.ss_station = None
        
        if q.args.ss_station:
            q.client.ss_station = q.args.ss_station
        if q.args.ss_col or q.args.ss_col == []:
            q.client.ss_col = q.args.ss_col       

        ## ------------------ Distribution of Different Features in the Dataset ------------------ ##
        q.page['ss_sidebar1'] = await q.run(db.ss_state_bar_menu, q)
        q.page['ss_sidebar2'] = await q.run(db.ss_station_bar_menu, q)
        q.page['ss_sidebar3'] = await q.run(db.ss_col_bar_menu, q)

        if q.client.ss_station:
            q.page['ss_body'] = await q.run(db.plot_ss_cols, q)

        ## ------------------ AQI Dsitribution for State-Station Pairs ------------------ ##
        if q.client.state is None:
            q.client.state = 'AS'
            q.client.station = []

        if q.args.state:
            if q.client.state != q.args.state:
                q.args.station = []
            q.client.state = q.args.state
            q.client.station = []
        
        if q.args.station:
            q.client.station = q.args.station.copy()

        q.page['sidebar1'] = await q.run(db.state_bar_menu, q)
        q.page['sidebar2'] = await q.run(db.station_bar_menu, q)

        if q.client.station:
            q.page['body'] = await q.run(db.plot_aqi, q)

    elif hash == "solution":
        q.page['solution'] = solution.sol_md
    elif hash == "appendix":
        q.page['appendix'] = appendix.appendix
    await q.page.save()