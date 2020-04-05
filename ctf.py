#!/usr/bin/env python
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
    parser.add_argument('-H', '--host', help='IP or hostname of the server')
    parser.add_argument('-P', '--port', help='port of the server (default: 1337)')
    args = parser.parse_args()
    main(args.host, args.port)
