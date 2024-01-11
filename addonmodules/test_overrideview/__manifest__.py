# -*- coding: utf-8 -*-
{
    'name': "Override Test",
    'summary': "Defines the 'gallery' view",
    'description': """
        Defines a new type of view ('awesome_gallery') which allows to visualize images.
    """,

    'version': '0.1',
    'depends': ['web'],
    'data': [
        'test_overrideview/views/views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'test_overrideview/static/src/**/*',
        ],
    },
    'license': 'AGPL-3'
}