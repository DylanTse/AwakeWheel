import cv2

def crop_eyes(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Load pre-trained face and eye cascade classifiers
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # For each face, detect eyes and crop the image around the eyes
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        
        # Detect eyes in the face region
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        # Crop the image around each eye
        for (ex, ey, ew, eh) in eyes:
            # Adjust cropping region to include some margin around the eyes
            margin = 10
            eye_roi_color = roi_color[ey-margin:ey+eh+margin, ex-margin:ex+ew+margin]
            cv2.imwrite(f'cropped_eye_{ex}.jpg', eye_roi_color)

# Example usage
image_path = 'image10.jpg'
crop_eyes(image_path)
