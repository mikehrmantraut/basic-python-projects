"""
Setting size and speed of videos.
@author: Mehmet Baran Munar
"""

# to install cv2 >>> pip install opencv-python and pip install cv2
import cv2

class ArrangeVideo:
    def __init__(self):
        # video name sample => "video.mp4" 
        # you can also copy full path of video.
        self.video_name = input("Please enter video name")
        self.video_speed = int(input("Please enter video speed, 25 is default. 25+slow/25-fast"))
    
    def setFrameSize(self):
        self.frameWidth = int(input("Set frame width."))
        self.frameHeight = int(input("Set frame height."))

    def playVideo(self):
        cap = cv2.VideoCapture(self.video_name)

        while True:
            success, img = cap.read()
            img = cv2.resize(img,(self.frameWidth, self.frameHeight))
            cv2.imshow("video1", img)
            # to exit video, press q
            if cv2.waitKey(self.video_speed) & 0xFF == ord('q'):
                break

        cv2.release()
        cv2.destroyAllWindows()

sample1 = ArrangeVideo()
sample1.setFrameSize()
sample1.playVideo()
