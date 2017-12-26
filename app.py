from PIL import Image
import face_recognition

# 输入图片
img_path = input("image path:")
image = face_recognition.load_image_file(img_path)
face_locations = face_recognition.face_locations(image)
face_count = len(face_locations)

print(f"Found {face_count} face(s) in this photograph.")
