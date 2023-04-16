from h2o_wave import ui

def foot():
    caption = '''Made with 💛 by DCoderz.'''
    footer = ui.footer_card(
        box='footer', 
        caption=caption,
        items=[
            ui.inline(justify='end', items=[
                ui.links(label='Sagar Thacker', width='200px', items=[
                    ui.link(label='LinkedIn', path='https://www.linkedin.com/in/sagar-thacker/', target='_blank'),
                    ui.link(label='GitHub', path='https://www.github.com/sagar118', target='_blank'),
                ]),
                ui.links(label='Shuchita Mishra', width='200px', items=[
                    ui.link(label='LinkedIn', path='https://www.linkedin.com/in/shuchitamishra/', target='_blank'),
                    ui.link(label='GitHub', path='https://github.com/shuchita28', target='_blank'),
                ]),
            ]),
        ])
    return footer