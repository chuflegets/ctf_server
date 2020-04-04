from base64 import b64encode
from json import dumps
from flask import Flask


application = Flask(__name__)
data = [{'letter': 'g', 'position': 1, 'code': 'Y29yb25hLXZpcnVzdXMuY29t'}, {'letter': '3', 'position': 2, 'code': 'Y29yb25hdmlydXMubWVkcy5jb20%3D'}, {'letter': 't', 'position': 3, 'code': 'Y29yb25hdmlydXNjb250YWluLmNvbQ%3D%3D'}, {'letter': '_', 'position': 4, 'code': 'Y29yb25hdmlydXNjb250YWluZWQuY29t'}, {'letter': 't', 'position': 5, 'code': 'Y29yb25hdmlydXNmZWVkYmFjay5jb20%3D'}, {'letter': '3', 'position': 6, 'code': 'Y29yb25hdmlydXNoYXJtLmNvbQ%3D%3D'}, {'letter': 's', 'position': 7, 'code': 'Y29yb25hdmlydXNoYXphcmQuY29t'}, {'letter': 't', 'position': 8, 'code': 'Y29yb25hdmlydXNtZXNzYWdlLmNvbQ%3D%3D'}, {'letter': '3', 'position': 9, 'code': 'Y29yb25hdmlydXN0cm91YmxlLmNvbQ%3D%3D'}, {'letter': 'd', 'position': 10, 'code': 'ZmlnaHRjb3ZpZC5wcm9maXRhYml0LmNsdWI%3D'}, {'letter': '_', 'position': 11, 'code': 'bWFzay5jb3JvbmFwcm90ZWN0aXZlLnN0b3Jl'}, {'letter': 'f', 'position': 12, 'code': 'Y29yb25hdmlydXMtZ3VpZGFuY2UuY29t'}, {'letter': '0', 'position': 13, 'code': 'bnljb3ZpZC0xOWNhc2VzLmNvbQ%3D%3D'}, {'letter': 'r', 'position': 14, 'code': 'Y292aWRuZXdzdXBkYXRlLm9ubGluZQ%3D%3D'}, {'letter': '_', 'position': 15, 'code': 'Y292aWR2b2ljZXBvcnRhbC5jb20%3D'}, {'letter': 'd', 'position': 16, 'code': 'cG9ydGFsLWNvdmlkLTE5Lm1s'}, {'letter': '4', 'position': 17, 'code': 'cG9ydGFsLWNvdmlkLTE5Lmdh'}, {'letter': '_', 'position': 18, 'code': 'YXlhbmdhcnRzLm9yLmty'}, {'letter': 'v', 'position': 19, 'code': 'Y292aWQtMTlkb25vci5jb20%3D'}, {'letter': '1', 'position': 20, 'code': 'Y292aWQxOWdyYW50b3IuY29t'}, {'letter': 'r', 'position': 21, 'code': 'Y292aWQtMTlkb25hdG9yLmNvbQ%3D%3D'}, {'letter': 'u', 'position': 22, 'code': 'Y3VyZWNvcm9uYXZpcnVzLmxpZmU%3D'}, {'letter': '5', 'position': 23, 'code': 'Y29yb25hdmlydXNyZXNvbmFuY2VjdXJlLmNvbQ%3D%3D'}]



@application.route('/ctf/iocs/<str:ioc_code>', methods=['GET'])
def get_ioc(ioc_code):
    responses = [b64encode('{}:{}'.format(obj['position'], obj['letter']).encode()).decode() for obj in data if obj['code'] == ioc_code]
    if len(responses) == 0:
        return ioc_code
    return responses[0]


@application.route('/ctf/prevent', methods=['POST'])
def prevent(measure):
    if not request.json or not 'measure' in request.json:
        abort(400)
    if request['measure'] == 'g3t_t3st3d_f0r_d4_v1ru5':
        return 'G00d j0b, hunt3r. Y0ur gl0r10u5 4ct10n s4v3d l1f35. G0 c3l3br4t3 h3r3 --> https://www.youtube.com/watch?v=t5kzdf8kUeM&t=12m0s', 201
    else:
        return 'Qu3ry th3 s3rv3r 1n 0rd3r t0 kn0w wh1ch 4ct10n mu5t b3 t4k3n. Y0u h4v3 n0t f0und th3 fl4g.'


if __name__ == '__main__':
    application.run(host='0.0.0.0')

