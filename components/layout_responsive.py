from h2o_wave import ui

def meta_layout(q):
    if (q.args['#'] == 'home') or (q.args['#'] == None):
        layout = ui.meta_card(box='', layouts=[
            ui.layout(
                breakpoint='xs',
                zones=[
                    ui.zone('header', size="80px"),
                    ui.zone('content'),
                    ui.zone('footer')
                ])
        ])
    elif (q.args['#'] == 'dashboard'):
        layout = ui.meta_card(box='', layouts=[
            ui.layout(
                breakpoint='xs',
                zones=[
                    ui.zone('header', size="80px"),
                    ui.zone('body'),
                    ui.zone('footer')
                ]),
            ui.layout(
                breakpoint='m',
                zones=[
                    ui.zone('header', size="80px"),
                    # ui.zone('stats', direction=ui.ZoneDirection.ROW, zones=[
                    #     ui.zone('state_pie', size='25%'),
                    #     ui.zone('ss_body', size='50%'),
                    # ]),
                    ui.zone("ss_mardown"),
                    ui.zone('ss', direction=ui.ZoneDirection.ROW, zones=[
                        ui.zone('ss_sidebar', size='25%'),
                        ui.zone('ss_body', size='75%'),
                    ]),
                    ui.zone("aqi_mardown"),
                    ui.zone('db', direction=ui.ZoneDirection.ROW, size="400px", zones=[
                        ui.zone('sidebar', size='25%'),
                        ui.zone('body', size='75%'),
                    ]),
                    ui.zone('aqi_level_md'),
                    ui.zone("aqi_level"),
                    ui.zone('footer')
                ])
        ])
    elif (q.args['#'] == 'solution'):
        layout = ui.meta_card(box='', layouts=[
            ui.layout(
                breakpoint='xs',
                zones=[
                    ui.zone('header', size="80px"),
                    ui.zone('sol_content'),
                    ui.zone('footer')
                ])
        ])
    elif (q.args['#'] == 'appendix'):
        layout = ui.meta_card(box='', layouts=[
            ui.layout(
                breakpoint='xs',
                zones=[
                    ui.zone('header', size="80px"),
                    ui.zone('app_content'),
                    ui.zone('footer')
                ])
        ])
    return layout