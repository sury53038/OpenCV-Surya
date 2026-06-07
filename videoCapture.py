import cv2

cap = cv2.VideoCapture(0)

def videoCap():
    
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Could not fetch image")
            break

        cv2.imshow("Video Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quiting...")
            break

    cap.release()
    cv2.destroyAllWindows()

def recVideo():
        
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    recorded = cv2.VideoWriter('myvideo1.mp4', fourcc, 20.0, (frame_width, frame_height))
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        recorded.write(frame)
        cv2.imshow("Recording", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    recorded.release()
    cv2.destroyAllWindows()


# videoCap()
# recVideo()
