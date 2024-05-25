from ultralytics import YOLO
from constants import *
import os
import pandas as pd

# load best model from training results
# best_model = YOLO(MODEL_WEIGHTS_BEST)
best_model = YOLO("yolov8s.pt") # BIRDeep/test/weights/best.pt

'''df = pd.read_csv(TEST_CSV)

imgs_list = df.transpose().values.tolist()

#new = list(np.concatenate(imgs_list))

# iterate through the sublist using List comprehension
flatList = [element for innerList in imgs_list for element in innerList]'''

best_model.val(
    data = "Detector/birdeep.yaml",
    conf = 0.4,  # confidence threshold
    # iou = 0.6, default = 0.6
    split = "val", # val, test or train
    save_json = True,  # save a COCO-JSON results file
    save_hybrid = True,  # save hybrid grid results
    plots = False, # save plots	of prediction vs ground truth
    save_conf = True  # save results with confidence scores
)

# get predictions on best model
'''results = best_model.predict(
    source=TEST_TXT, #"Dataset/multispecies.jpeg", # (str, optional) source directory for images or videos
    save=True, 
    conf=0.4,
    save_txt = True,  # (bool) save results as .txt file
    save_conf = True,  # (bool) save results with confidence scores
    # save_crop = True,  # (bool) save cropped images with results

    #show = True,  # (bool) show results if possible
    #show_labels = True,  # (bool) show object labels in plots
    #show_conf = True,  # (bool) show object confidence scores in plots

    #visualize = True,  # (bool) visualize model features
    
    
    #vid_stride = 1,  # (int) video frame-rate stride
    #line_width = ,   # (int, optional) line width of the bounding boxes, auto if missing
    #augment = False,  # (bool) apply image augmentation to prediction sources
    #agnostic_nms = False,  # (bool) class-agnostic NMS
    #classes = , # (int | list[int], optional) filter results by class, i.e. classes=0, or classes=[0,2,3]
    #retina_masks = False,  # (bool) use high-resolution segmentation masks
    #boxes = True  # (bool) Show boxes in segmentation predictions
    )'''

# Perform object detection on an image using the model
# results = model('https://ultralytics.com/images/bus.jpg')
'''

# What Manuel wanted :´) -> for classification model, will it work with detection???????????????????
# Run inference on an image
# results = best_model(source='Detector/AM1_20230510_083000.PNG')  # results list'''

'''# View results
for r in results:
    print(r.B)  # print the Probs object containing the detected class probabilities'''