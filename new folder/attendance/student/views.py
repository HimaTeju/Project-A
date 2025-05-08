from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import json  # Import your Student model

def home(request):
    return render(request, "student/scan_qr.html")

@csrf_exempt  # Use if you want to disable CSRF for this view (not recommended in production)
def scan_qr_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        image_data = data.get('image')
        print("Hello from scan_qr_code")
        
        # Process the image
        try:
            # Decode the base64 image data
            header, encoded = image_data.split(',', 1)
            img_data = base64.b64decode(encoded)
            np_array = np.frombuffer(img_data, np.uint8)
            image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

            # Decode the QR code
            decoded_objects = decode(image)
            if decoded_objects:
                qr_data = decoded_objects[0].data.decode('utf-8')
                print("Decoded QR Code Data:", qr_data)
        finally:
            # Clean up resources if needed
            pass
