import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_EXPOSURE, 0.3)
cap.set(cv2.CAP_PROP_ISO_SPEED, 2500)
# Increase brightness by 50 units
cap.set(cv2.CAP_PROP_FRAME_WIDTH, cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# Check if camera is opened successfully
if not cap.isOpened():
    print("Unable to open the camera")
else:
    # Capture frame-by-frame
    ret, frame = cap.read()
    brightness = 50
    contrast = 4.0

    enhanced_image = cv2.convertScaleAbs(frame, alpha = contrast , beta=brightness)
    # Release the VideoCapture object
    cap.release()

    # Add a delay to give the camera time to adjust to the lighting conditions
    cv2.waitKey(1000)

    # Save the captured image
    cv2.imwrite('captured_image.jpg', enhanced_image)

    # Display the captured image
    cv2.imshow('Captured Image', enhanced_image)
    cv2.waitKey(0)

