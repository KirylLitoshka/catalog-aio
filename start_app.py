from catalog import main
from aiohttp import web


def start():
    app = main.init_app()
    web.run_app(app, host='localhost', port=8000)


if __name__ == '__main__':
    start()
