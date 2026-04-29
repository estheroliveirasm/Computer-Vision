import cv2 as cv

# Initialize the webcam (0 is usually the default camera)
cap = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    # 'ret' is a boolean (True if the frame was read correctly)
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Processing the live feed:
    # Convert to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Apply a binary threshold (pixels > 100 become white)
    _, th = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)

    # Display the resulting frame in a window
    cv.imshow("Live Binary Filter", th)
    
    # Wait for 1ms and check if the 'q' key is pressed to exit
    if cv.waitKey(1) == ord("q"):
        break

# Release the capture and close all windows
cap.release()
cv.destroyAllWindows()