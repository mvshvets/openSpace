from app.map import bp


@bp.route('/map')
def hello_world():


    return {'value': 'Hello, World!'}
