import os

from  flask import render_template, request, redirect
from werkzeug.utils import secure_filename

from app import app

app.config['IMAGE_DIR'] = 'C:/Users/INVENTAR/Desktop/web apps/flask-upload/app/static/image/uploads'
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ['JPG', 'JPEG', 'PNG', 'GIF']

def allowed_image(filename):

    if not '.' in filename:
        return False
    
    ext = filename.rsplit('.', 1)[1]

    if ext.upper() in app.config['ALLOWED_IMAGE_EXTENSIONS']:
        return True
    else:
        return False


@app.route('/upload_image', methods=['POST', 'GET'])
def upload_image():

    if request.method == 'POST':
        if request.files:
            image = request.files['image']
            # check if image has a file name
            if image.filename == '':
                print('Image must have a file name')
                return redirect(request.url)
            # check if image is of allowe extension
            if not allowed_image(image.filename):
                print('The image extention is not allowed')
                return redirect(request.url)
            else:
                filename = secure_filename(image.filename)

            image.save(os.path.join(app.config['IMAGE_DIR'], filename))
            print('Image saved')
            return redirect(request.url)

    return render_template('upload_image.html')


