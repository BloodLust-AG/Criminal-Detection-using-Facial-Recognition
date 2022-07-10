import cv2 as cv
import mediapipe as mp
import dlib as dl

#face mesh
face=mp.solutions.face_mesh
mesh=face.FaceMesh()

mp_drawing=mp.solutions.drawing_utils
drawing_spec=mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

#image
ima = cv.imread(r"C:\Users\aksha\Desktop\PROJECT\MAJOR PROJECT\Stuff\gas\407.jpg")
rima = cv.cvtColor(ima,cv.COLOR_BGR2RGB)

#face landmarks
res=mesh.process(ima)
rima=cv.cvtColor(rima,cv.COLOR_RGB2BGR) #after processing

#landmarks in matrix
if res.multi_face_landmarks:
    for face_landmarks in res.multi_face_landmarks:
        print(face_landmarks)
        #location of the landmarks in array
        mp_drawing.draw_landmarks(image=rima, 
                landmark_list=face_landmarks, 
                landmark_drawing_spec=drawing_spec, 
                connection_drawing_spec=drawing_spec)

cv.imshow('a', ima)
cv.imshow('s',rima)
cv.waitKey(0)