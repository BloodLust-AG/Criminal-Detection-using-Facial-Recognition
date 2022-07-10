# Criminal-Detection-using-Facial-Recognition
To identify Human faces in a frame from a blacklist of faces, using MediaPipe - Face Mask

![image](https://user-images.githubusercontent.com/109036254/178157487-4257e20f-018a-4cb1-80b5-9a14226a4600.png)


In this project, I am tasked with building a algorithm using the MediPipe - Face Mask, and Recalibrating the same to Identify 468 3D face landmarks (Face Mesh) in real-time.
I am also Building a SVM Algorithm that uses 2 Face Meshes to classify if the faces are similar or dissimilar.

This project is a combined effort of 4, with me as the Acting Scrum master and the technical lead. I was also working very closely alongside the literature surveyor to identify technologies relevent to the project, assign it to the team for experimentation period. I compared the techniques and assigned them other roles related to front end development.

After we decided to follow the geometric Feature based Facial Recognition approach. We found the face mask pipeline by MediaPipe used in Instagram for agumented reality feature a perfect fit for the SVM method of classification.

Architecture followed:

![image](https://user-images.githubusercontent.com/109036254/178157517-dea474e1-82f2-4499-8e6d-bc48d4ac34ec.png)

Example of the Face Mesh extracted:

![image](https://user-images.githubusercontent.com/109036254/178156885-aa22e461-d01a-4868-853c-8c696e280796.png)

Example of the 3D landmarks generated with a laptop webcam without depth sensor:

![image](https://user-images.githubusercontent.com/109036254/178156995-e70e7d1c-c93c-42c0-8dd2-af9bfee3f2a6.png)

Example of the working SVM, before and after Image Manuplation:

![image](https://user-images.githubusercontent.com/109036254/178157094-09a7e46b-b266-446c-823b-507bd9f110f6.png)

The reason for usage of a Face Mesh is also to turn the project into a research study, as the technology hasn't been used in the field before. and the 3D landmarks can also be used in GANS to generate a front facing face even if there is partial coverage in the face.

Example of Face Mesh generation with partially visible face:

![image](https://user-images.githubusercontent.com/109036254/178157388-fddcd415-470e-4603-95c1-c2fff30a16bd.png)

And the simplicity of SVM allows for flexible and real-time application.

Research paper in process of submition. :)
