# installation needed for running object detection
# python 3.8.6 required
# pip3 install tensorflow==1.13.1
# pip3 install opencv-python
# pip3 install keras==2.2.4
# pip3 install numpy==1.16.1

from datetime import datetime
import csv
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox


def perMinute():
    # global variable
    global start_minute
    global frames_with_objects
    global empty_frames
    global average_output_count

    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    wine_glass = average_output_count.get('wine_glass', "0")
    cup = average_output_count.get('cup', "0")
    bowl = average_output_count.get('bowl', "0")
    bottle = average_output_count.get('bottle', "0")
    spoon = average_output_count.get('spoon', "0")
    knife = average_output_count.get('knife', "0")
    fork = average_output_count.get('fork', "0")

    with open('objectrecognition/objects.csv', 'a', newline='') as csvfile:
        fieldnames = ['current_time', 'avg_wine_glass', 'avg_cup', 'avg_bowl',
                      'avg_spoon', 'avg_knife', 'avg_fork']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'current_time': current_time,
                         'avg_wine_glass': wine_glass, 'avg_cup': cup, 'avg_bowl': bowl, 'avg_bottle': bottle, 'avg_spoon': spoon,
                         'avg_knife': knife, 'avg_fork': fork})


def perFrame(labels):
    global starting_second
    global total_output_count
    global average_output_count
    global total_frame_count

    current_second = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    total_frame_count += 1

    for item in labels:
        if item == 'wine_glass':
            total_output_count['wine_glass'] += 1
        if item == 'cup':
            total_output_count['cup'] += 1
        if item == 'bowl':
            total_output_count['bowl'] += 1
        if item == 'bottle':
            total_output_count['bottle'] += 1
        if item == 'spoon':
            total_output_count['spoon'] += 1
        if item == 'knife':
            total_output_count['knife'] += 1
        if item == 'fork':
            total_output_count['fork'] += 1

    difference = datetime.strptime(current_second, '%d-%m-%Y %H:%M:%S') - datetime.strptime(starting_second, '%d-%m-%Y %H:%M:%S')
    if difference.total_seconds() >= 60:
        average_output_count = {'wine_glass': total_output_count['wine_glass'] / total_frame_count,
                                'cup': total_output_count['cup'] / total_frame_count,
                                'bowl': total_output_count['bowl'] / total_frame_count,
                                'bottle': total_output_count['bottle'] / total_frame_count,
                                'spoon': total_output_count['spoon'] / total_frame_count,
                                'knife': total_output_count['knife'] / total_frame_count,
                                'fork': total_output_count['fork'] / total_frame_count}
        total_output_count = {'wine_glass': 0, 'cup': 0, 'bowl': 0, 'bottle': 0, 'spoon': 0, 'knife': 0, 'fork': 0}
        perMinute()


def main(camera):
    # global variable
    global start_minute
    global frames_with_objects
    global empty_frames
    global starting_second
    global total_output_count
    global average_output_count
    global total_frame_count

    start_minute = 0
    frames_with_objects = 0
    empty_frames = 0
    process_this_frame = True
    starting_second = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    total_output_count = {'wine_glass': 0, 'cup': 0, 'bowl': 0, 'bottle': 0, 'spoon': 0, 'knife': 0, 'fork': 0}
    average_output_count = total_output_count
    total_frame_count = 0

    with open('objectrecognition/objects.csv', 'w', newline='') as csvfile:
        fieldnames = ['current_time', 'avg_wine_glass', 'avg_cup', 'avg_bowl', 'avg_bottle', 'avg_spoon', 'avg_knife', 'avg_fork']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


    while True:
        # Grab a single frame of video
        ret, frame = camera.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)

        if process_this_frame:
            bbox, label, conf = cv.detect_common_objects(small_frame, confidence=0.25, model='yolov3-tiny')
            if 'wine_glass' in label or 'cup' in label or 'bowl' in label or 'bottle' in label or 'spoon' in label or 'knife' in label or 'fork' in label:
                perFrame(label)

        process_this_frame = not process_this_frame

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
