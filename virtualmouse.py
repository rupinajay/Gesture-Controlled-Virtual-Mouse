import math
import cv2
import mediapipe as mp
import pyautogui as pag
import time

# Get the size of the screen
screen_width, screen_height = pag.size()

# Initialize mediapipe modules
mpDraw = mp.solutions.drawing_utils
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)

# Open the default camera
cap = cv2.VideoCapture(0)
										#sanjay
def main():
    # Initialize variables for tracking time and frame rate
    ct = 0
    pt = 0
    while True:
        # Read frame from camera
        success, img = cap.read()

        # Flip the frame horizontally to avoid mirrored display
        img = cv2.flip(img, 1)

        # Normalize the pixel values to the range [0, 255]
        cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX)

        # Get the dimensions of the frame
        vidh, vidw, vidz = img.shape
										#raya		
        # Convert the color space of the frame from BGR to RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Use mediapipe to detect hand landmarks in the frame
        data = hands.process(imgRGB)

        # Calculate and display the frame rate
        ct = time.time()
        fps = int(round(1 / (ct - pt)))
        pt = ct
        cv2.putText(img, "FPS : {}".format(fps), (0, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)

        # Initialize a flag to break out of the loop if necessary
        break_out = False
										#rudra
        # If one or more hands are detected in the frame
        if data.multi_hand_landmarks:
            # Loop over all detected hands
            for x in data.multi_hand_landmarks:
                # Get the x and y coordinates of the index finger tip, middle finger tip, and thumb tip
                pointx = x.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].x
                pointy = x.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y
                middlex = x.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].x
                middley = x.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y
                thumbx = x.landmark[mpHands.HandLandmark.THUMB_TIP].x
                thumby = x.landmark[mpHands.HandLandmark.THUMB_TIP].y
										#thava
                # Draw circles around the index finger tip and thumb tip
                cv2.circle(img, (int(pointx * vidw), int(pointy * vidh)), 10, (0, 0, 255),-1)
                cv2.circle(img, (int(thumbx * vidw), int(thumby * vidh)), 10, (0, 0, 255),-1)

                # Move the mouse cursor to the position of the middle finger tip
                pag.moveTo(middlex * screen_width * 1.3, middley * screen_height * 1.3)
										#sukrith
                # If the distance between the thumb tip and middle finger tip is less than 50 pixels,
                # set the break_out flag and break out of the loop
                if abs(math.sqrt((middlex * screen_width - thumbx * screen_width) ** 2 + (
                        middley * screen_height - thumby * screen_height) ** 2)) < 50:
                    break_out = True
                    break

                # click if thumb finger is close to index finger
                if abs(math.sqrt((pointx * screen_width - thumbx * screen_width) ** 2 + (
                        pointy * screen_height - thumby * screen_height) ** 2)) < 50:
                    pag.click()
                    break
            if break_out:
                break
										#thava                   
	# Display the resulting image with the detected hand landmarks and FPS
        cv2.imshow('Gesture Controlled Mouse', img)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()

