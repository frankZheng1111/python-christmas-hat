"""
python为图片拼接圣诞帽
"""

import face_recognition
from PIL import Image

class ChristmasHatService:
    """
    ChristmasHat
    """
    def __init__(self, img_path):
        self.img_path = img_path
        self.face_locations = ()
        self.human_img = ''

    def recognize_faces(self):
        """
        recognize faces in base img
        """
        image = face_recognition.load_image_file(self.img_path)
        self.face_locations = face_recognition.face_locations(image)

    def face_count_in_base_img(self):
        """
        recognize faces in base img
        """
        face_count = len(self.face_locations)
        return face_count

    def wear_hats_for_people_in_img(self):
        """
        wear hats for people in img
        """
        hat_distance = 10
        human_img = Image.open(self.img_path)
        human_img = human_img.convert("RGBA")

        hat_img = Image.open("./public/hat.png")
        hat_img = hat_img.convert("RGBA")

        for face_location in self.face_locations:
            top, right, bottom, left = face_location
            top -= hat_distance
            print("A face is located at pixel location")
            print(f"Top: {top}, Left: {left}, Bottom: {bottom}, Right: {right}")
            head_h = bottom-top # hight of head
            head_l = right-left # length of head
            hat_img = hat_img.resize((head_l, head_h)) # convert size of hat
            hat_region = hat_img
            human_region = (left, top-head_h, right, top)
            human_img.paste(hat_region, human_region, mask=hat_img)
        self.human_img = human_img

IMG_PATH = input("Please input base image path: ")
CHRISTMAS_HAT_SERVICE = ChristmasHatService(IMG_PATH)
CHRISTMAS_HAT_SERVICE.recognize_faces()
print(f"Found {CHRISTMAS_HAT_SERVICE.face_count_in_base_img()} face(s) in this photograph.")
CHRISTMAS_HAT_SERVICE.wear_hats_for_people_in_img()

CHRISTMAS_HAT_SERVICE.human_img.show()
