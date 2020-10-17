from flask_restx import Resource, Namespace, reqparse
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from app.utils import allowed_file, ALLOWED_EXTENSIONS

ns = Namespace('upload-file', description='Загрузка фотографии')

upload_parser = ns.parser()
upload_parser.add_argument('file', type=FileStorage, location='files',
                           required=True)

parser = reqparse.RequestParser()
parser.add_argument('file', required=True)


@ns.route("")
class UploadFile(Resource):

    @ns.expect(upload_parser)
    @ns.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Неизвестная ошибка'})
    def post(self):
        """
        Загрузка фотографии
        """

        args = upload_parser.parse_args()
        uploaded_file = args['file']

        if not allowed_file(uploaded_file.filename):
            return {
                "message": {"Можно загрузить только файлы в формате {}".format(ALLOWED_EXTENSIONS)}
            }

        if uploaded_file:
            filename = secure_filename(uploaded_file.filename)

            # магия с file

            return {
                "message": "Фото успешно загружено"
            }
