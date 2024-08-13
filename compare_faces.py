from deepface import DeepFace

def compare_faces(id_card_image_path, face_image_path):
    result = DeepFace.verify(id_card_image_path, face_image_path)
    return "Face is Verified" if result["verified"] else "Face is Not Verified"
