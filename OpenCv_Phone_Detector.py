import numpy as np 
import cv2 as cv 
from ultralytics import YOLO


coco_file = open("coco_List/thing.names", "r")
data = coco_file.read()
classlist = data.split("\n")
coco_file.close()


def is_overlapping(box1, box2):
    x1_min, y1_min, x1_max, y1_max = box1
    x2_min, y2_min, x2_max, y2_max = box2
    
    if x1_max < x2_min or x2_max < x1_min:
        return False
    
 
    if y1_max < y2_min or y2_max < y1_min:
        return False
    
   
    return True


model = YOLO("yolov10n.pt")


cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)


while True:
    ret, video = cap.read()
    if not ret:
        break

    
    detect_params = model.predict(source=[video], conf=0.5, save=False)
    DP = detect_params[0].numpy()

    person_box = None
    phone_box = None

    if len(DP) != 0:
        for i in range(len(detect_params[0])):
            boxes = detect_params[0].boxes
            box = boxes[i]  
            clsID = box.cls.numpy()[0]
            conf = box.conf.numpy()[0]
            bb = box.xyxy.numpy()[0]
            
            if clsID == 0:  
                person_box = bb
                
            
            elif clsID == 67:  
                phone_box = bb
            
            
            if person_box is not None and phone_box is not None:
                if is_overlapping(person_box, phone_box):
                   
                    cv.rectangle(
                        video,
                        (int(person_box[0]), int(person_box[1])),
                        (int(person_box[2]), int(person_box[3])),
                        color=(227, 34, 20), thickness=3,
                    )
                   
                    font = cv.FONT_HERSHEY_COMPLEX
                    cv.putText(
                        video,
                        "Using Phone",
                        (int(person_box[0]), int(person_box[1]) - 10),
                        font,
                        1,
                        (0, 0, 0),
                        2,
                    )

        
        cv.imshow("ObjectDetection", video)

   
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()

