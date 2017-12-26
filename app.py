"""
python为图片拼接圣诞帽
"""

import face_recognition
# from PIL import Image

class ChristmasHatService:
    """
    ChristmasHat
    """
    def __init__(self):
        self.img_path = input("Please input base image full path:")
        self.face_locations = []

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

CHRISTMAS_HAT_SERVICE = ChristmasHatService()
CHRISTMAS_HAT_SERVICE.recognize_faces()
print(f"Found {CHRISTMAS_HAT_SERVICE.face_count_in_base_img()} face(s) in this photograph.")
