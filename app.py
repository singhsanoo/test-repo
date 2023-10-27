from flask import Flask, render_template, redirect
from flask import Response
# from werkzeug.datastructures import Headers
# from bs4 import BeautifulSoup
# from flask_restful import Resource, Api

import asyncio

import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)


cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cap.set(cv2.CAP_PROP_FPS, 10)


def cv_video():
    while True:
        ret, frame = cap.read()

        if ret:
            # Process the frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Encode the processed frame as a JPEG image
            _, buffer = cv2.imencode('.jpeg', frame)
            frame_bytes = buffer.tobytes()

            # Yield the frame as a byte stream with appropriate headers
            yield (b'--frame\r\n' b'Content-type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

            # Clean up the buffer
            del buffer

        # await asyncio.sleep(0.1) # Adjust the delay as needed
        # ret, frame = cap.read()
    # cap.release()





#############################################################
# BEGIN FLASK ROUTING
#############################################################

app = Flask(__name__)
# app.config["JSON_SORT_KEYS"] = False
# app.config["SEND_FILE_MAX_PAGE_DEFAULT"] = 0

#############################################################
# Index endpoint
#############################################################

@app.route("/")
def index():
    
    return render_template("index.html")     

#############################################################

@app.route("/opt1")
def new1():
    return redirect("/", code=302)    
    # return render_template("map.html")    http://127.0.0.1:5000/opt1

# @app.route("/opt2")
# def new2():
#     return render_template("new.html")

@app.route("/opt2")
def new2():
   return render_template("volcano.html")

@app.route("/opt3")
def new3():
   return render_template("year.html")

#############################################################

@app.route('/video_feed')
def video_feed():
    return Response(cv_video(), mimetype= 'multipart/x-mixed-replace; boundary=frame')


# @app.route('/video_feed')
# def video_feed():
#     return Response(cv_video(), mimetype= 'multipart/x-mixed-replace; boundary=frame')






#############################################################
# END FLASK ROUTING
#############################################################
    
if __name__ == "__main__":

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.gather(cv_video()))

    app.run(host='0.0.0.0', port='5000')


#https://stackoverflow.com/questions/39724687/bootstrap-tabs-without-anchors

# import cv2
# import numpy
# from flask import Flask, render_template, Response, stream_with_context, Request

# video = cv2.VideoCapture(0)
# app = Flask(__name__)

# def video_stream():
#     while(True):
#         ret, frame = video.read()
#         if not ret:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpeg',frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n' b'Content-type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/siteTest')

# def siteTest():
#     return render_template('siteTest.html')

# @app.route('/video_feed')

# def video_feed():
#     return Response(video_stream(), mimetype= 'multipart/x-mixed-replace; boundary = frame')

# app.run(host ='0.0.0.0', port= '5000', debug=False)