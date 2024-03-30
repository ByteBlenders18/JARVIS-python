import cv2


def loopgui(video_path):

    output_path = 'features/reco_face/looped_video.mp4'

    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = 800
    frame_height = 800
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    frames_to_loop = 1

    while frames_to_loop > 0:
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        out.write(frame)
        cv2.imshow('Looping Video', frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            pass
            # frames_to_loop -= 1

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def gui_speak():
    loopgui(r"python gui/jarvis2.gif")
