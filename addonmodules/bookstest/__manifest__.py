{
    'name': "Book test",
    'version': '1.0',
    'depends': ['base'],
    'author': "Martin",
    'category': 'Technichal',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'views/mymodule_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo/demo_data.xml',
    ],
    'installable':True,
    'auto_install':False,
    'module_type':'official',
}