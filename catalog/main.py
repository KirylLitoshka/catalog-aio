from aiohttp import web
from catalog import setting, routes
import aiohttp_debugtoolbar
import aiohttp_jinja2
import jinja2


async def init_app():
    app = web.Application()
    app['config'] = setting.get_config(setting.CONFIG_PATH)
    routes.setup_routes(app)
    aiohttp_debugtoolbar.setup(app)

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(setting.TEMPLATE_DIR))
    return app
