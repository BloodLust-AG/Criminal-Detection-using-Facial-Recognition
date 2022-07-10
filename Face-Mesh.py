import cv2
import mediapipe as mp
import time

mp_drawing=mp.solutions.drawing_utils
mp_face_mesh=mp.solutions.face_mesh

drawing_spec=mp_drawing.DrawingSpec(thickness=0, circle_radius=2)

cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(min_detection_confidence=0.5,min_tracking_confidence=0.5) as face_mesh:

    while True:
        suc, image = cap.read()
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable=False
        results=face_mesh.process(image)
        #print(results)
        image.flags.writeable=True
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(image=image, 
                landmark_list=face_landmarks, 
                landmark_drawing_spec=drawing_spec, 
                connection_drawing_spec=drawing_spec)
        cv2.imshow("d", image)
        k=cv2.waitKey(1)
        if k ==ord('q'):
            break
cap.release
cv2.destroyAllWindows()