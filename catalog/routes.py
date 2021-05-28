from catalog import views, setting


def setup_routes(app):
    app.router.add_get('/', views.index)
    app.router.add_static('/static/', path=setting.STATIC_DIR, name='static')
