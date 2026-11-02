from flask import Flask, render_template, request, jsonify, send_file
from pathlib import Path
from views import views

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024
app.register_blueprint(views, url_prefix = "/views")
#----------------------------------------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')
#----------------------------------------------------------------------------------------------------   
@app.route('/ping')
def ping():
    return 'Pong', 200, {'Cache-Control': 'no-store'}
#----------------------------------------------------------------------------------------------------   

#----------------------------------------------------------------------------------------------------

@app.route('/download')
def download():
    response = send_file(
        Path(app.root_path) / '20MB.png',
        mimetype='application/octet-stream',
        as_attachment=True,
        download_name='20MB.png',
        conditional=False,
        etag=False,
        max_age=0,
    )
    response.headers['Cache-Control'] = 'no-store'
    return response


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file is None or not file.filename:
        return jsonify(error='Select a file to upload.'), 400
    received = 0
    for chunk in iter(lambda: file.stream.read(64 * 1024), b''):
        received += len(chunk)
    return jsonify(bytes_received=received)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=False)
