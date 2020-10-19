import os
import numpy as np
import cv2
import time
import datetime

cap = cv2.VideoCapture(0)


frames_per_seconds = 20
save_path='saved-media/timelapse.mp4'
config = CFEVideoConf(cap, filepath=save_path, res='720p')
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)
timelapse_img_dir = 'images/timelapse/'
seconds_duration = 20
seconds_between_shots = .25

if not os.path.exists(timelapse_img_dir):
    os.mkdir(timelapse_img_dir)

now = datetime.datetime.now()
finish_time = now + datetime.timedelta(seconds=seconds_duration)
i = 0
while datetime.datetime.now() < finish_time:
    '''
    Ensure that the current time is still less
    than the preset finish time
    '''
    ret, frame      = cap.read()
    filename        = f"{timelapse_img_dir}/{i}.jpg"
    i               += 1
    cv2.imwrite(filename, frame)
    time.sleep(seconds_between_shots)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
