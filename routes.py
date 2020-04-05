from views import index, get_piece, prevent


def setup_routes(app):
    app.router.add_get('/ctf', index)
    app.router.add_get('/ctf/pieces/{code}', get_piece)
    app.router.add_post('/ctf/prevent', prevent)
