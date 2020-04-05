from argparse import ArgumentParser
from aiohttp import web
from routes import setup_routes


def main(host='127.0.0.1', port=1337):
    app = web.Application()
    setup_routes(app)
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    web.Request
    parser = ArgumentParser()
    parser.add_argument('--host', help='IP or hostname of the server')
    parser.add_argument('--port', help='port of the server (default: 1337)')
    parser.parse_args()
    main()
