

def generate():
    # grab global references to the output frame and lock variables
    global jpg_buffer, lock

    while True:
        # wait until the lock is acquired
        with lock:

            rpi_name, jpg_buffer = imagehub.recv_jpg()

            if jpg_buffer is None:
                continue

            image = cv2.imdecode(np.frombuffer(jpg_buffer, dtype='uint8'), -1)

            imagehub.send_reply(b'OK')

        # yield the output frame in the byte format
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(image) + b'\r\n')


@app.route("/video_feed")
def video_feed():
    return Response(generate(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")