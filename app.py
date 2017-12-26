from PIL import Image
import face_recognition

# 输入图片
img_path = input("image path:")
image = face_recognition.load_image_file(img_path)
face_locations = face_recognition.face_locations(image)
print("Found {} face(s) in this photograph.".format(len(face_locations)))
