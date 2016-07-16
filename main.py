from time import sleep

from flask import Flask, render_template, Response
from lib.camera import Camera

app = Flask(__name__)


def generate_stock_table():
    with app.app_context():
        yield render_template("stock_table.html")
        for x in range(0, 5):
            name = 'Row {0}'.format(x)
            stock = {
                'id': x,
                'name': name
            }
            yield render_template("stock_row.html", stock=stock)
        yield render_template("stock_table_footer.html")


def stream_video(camera):
    while True:
        sleep(5)
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video-feed')
def video_feed():
    camera = Camera()
    mime_type = 'multipart/x-mixed-replace; boundary=frame'
    return Response(stream_video(camera), mimetype=mime_type)


@app.route('/')
def stock_table():
    return Response(generate_stock_table())


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
