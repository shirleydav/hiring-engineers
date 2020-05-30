from datadog import initialize, api

options = {
    'api_key': '**',
    'app_key': '**'
}

initialize(**options)

title = 'Rollup sum of my metric'
widgets = [{
    'definition': {
        'type': 'timeseries',
        'requests': [
            {'q': 'sum:my_metric{host:shirleyswork}.rollup(sum,60)'}
        ],
        'title': 'Roll up sum of metric'
    }
}]

layout_type = 'ordered'
description = 'A dashboard with memory info.'
is_read_only = True
notify_list = ['davila.shirl@gmail.com']
template_variables = [{
    'name': 'host1',
    'prefix': 'host',
    'default': 'my-host'
}]

saved_views = [{
    'name': 'Saved views for hostname 2',
    'template_variables': [{'name': 'host', 'value': '<HOSTNAME_2>'}]}
]

api.Dashboard.create(title=title,
                     widgets=widgets,
                     layout_type=layout_type,
                     description=description,
                     is_read_only=is_read_only,
                     notify_list=notify_list,
                     template_variables=template_variables,
                     template_variable_presets=saved_views)
