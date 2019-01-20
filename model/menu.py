response.logo = A(B('web', SPAN(2), 'py'),XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

response.menu = [
    (T('Home'), False, URL('products', 'view'), [])
]

DEVELOPMENT_MENU = True

def _():
    #shortcuts
    app = request.application
    ctr = request.controller
    #useful links to internal and external resources
    response.menu += [
        (T('Post'), False, URL('products', 'post')),
        (T('Profile'), False, URL('profile', 'save'))
]