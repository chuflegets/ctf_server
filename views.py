from aiohttp import web
from base64 import b64encode
from json import dumps, load, loads
from pathlib import Path


base_dir = Path(__file__).resolve().parent
with open(base_dir / 'data.json', mode='r') as data_file:
    data = load(data_file)
with open(base_dir / 'index.html', mode='r') as html_file:
    html = ''.join(html_file.readlines())
successful_measure = 'g3t_t3st3d_f0r_d4_v1ru5'
successful_measure_message = ''.join([
    'G00d j0b, hunt3r. Y0ur gl0r10u5 4ct10n s4v3d l1f35.',
    'G0 c3l3br4t3 h3r3 --> https://www.youtube.com/watch?v=t5kzdf8kUeM&t=12m0s'])
failed_measure_message = bytes.fromhex(data['failed_measure_message']).decode(encoding='UTF-8')
allowed_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/95.0'


async def index(request):
    return web.Response(body=html, content_type='text/html')


async def get_piece(request):
    obj = {}
    headers = request.headers
    if 'User-Agent' in headers:
        if headers['User-Agent'] == allowed_user_agent:
            code = request.match_info.get('code')
            results = [
                b64encode(f"{element['position']}:{element['letter']}".encode()).decode()
                for element in data['iocs'] if element['code'] == code
            ]
            if len(results) == 0:
                piece = code
            else:
                piece = results[0]

            status = 200
            obj['piece'] = piece
        else:
            status = 403
            obj['error'] = '403 Forbidden'
            obj['message'] = 'Your HTTP client is not allowed'
    else:
        status = 400
        obj['error'] = '400 Bad Request'
        obj['message'] = 'HTTP client identity not revealed'

    return web.Response(text=dumps(obj), status=status)


async def prevent(request):
    obj = {}
    if request.can_read_body:
        body = loads(await request.content.read())
        if 'measure' in body:
            status = 200
            if body['measure'] == successful_measure:
                obj['message'] = successful_measure_message
            else:
                obj['message'] = failed_measure_message
        else:
            status = 400
            obj['error'] = '400 Bad Request'
            obj['message'] = 'Your request body has no \'measure\' key'
    else:
        status = 400
        obj['error'] = '400 Bad Request'
        obj['message'] = 'Your request has no body'
    return web.Response(text=dumps(obj), status=status)
