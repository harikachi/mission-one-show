import tkinter as tk
from tkinter import filedialog, messagebox, Label, Button, Text
import requests
import os

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv

load_dotenv()

# Custom Vision API credentials
PREDICTION_KEY = os.getenv("PREDICTION_KEY")
PREDICTION_END_POINT = os.getenv("PREDICTION_END_POINT")
#Cognitive computer vision AIP credentials
SUBSCRIPTION_KEY = os.getenv("SUBSCRIPTION_KEY")
COMPUTER_VISION_END_POINT = os.getenv("COMPUTER_VISION_END_POINT")

def analyze_image(image_path=None, image_url=None):
    headers = {
        "Prediction-Key": PREDICTION_KEY,
        "Content-Type": "application/octet-stream" if image_path else "application/json"
    }
    
    if image_path:
        with open(image_path, "rb") as image_file:
            response = requests.post(PREDICTION_END_POINT, headers=headers, data=image_file)
        with open(image_path, "rb") as vision_file:
            computervision_client = ComputerVisionClient(COMPUTER_VISION_END_POINT, CognitiveServicesCredentials(SUBSCRIPTION_KEY))
            brand_response = computervision_client.analyze_image_in_stream(vision_file, visual_features=[VisualFeatureTypes.brands], max_candidates=1)
    try:
        response.raise_for_status()
        analysis = response.json()
        predictions = analysis["predictions"]
        result_text.delete("1.0", tk.END)

        car_type = predictions[0]['tagName'].upper()
        result_text.insert(tk.END, f" Type of the car is: {car_type}\n\n")
        if(len(brand_response.brands) >= 1):
            result_text.insert(tk.END, f" Brand of the car is: {brand_response.brands[0].name}\n")
        else:
            result_text.insert(tk.END, f" Brand of the car is Unidentified \n")
        # Calculate the insurance
        insurance_cost = calculate_insurance(car_type)

        if insurance_cost:
            result_text.insert(tk.END, f"\nInsurance cost for your vehicle type {car_type} is ${insurance_cost}.")
        else:
            result_text.insert(tk.END, f"\nSorry, we don't have insurance rates for this.")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("API Error", f"An error occurred: {e}")

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        analyze_image(image_path=file_path)

# Set up the UI
root = tk.Tk()
root.title("API Client with Image Upload")

label = Label(root, text="Upload an Image:")
label.pack(pady=10)

upload_button = Button(root, text="Upload and Analyze Image", command=upload_image)
upload_button.pack(pady=10)

result_text = Text(root, wrap="word", width=60, height=15)
result_text.pack(pady=10)

# Define base insurance rates for different car types
insurance_rates = {
    'sedan': 1500,
    'suv': 2000,
    'hatchback': 1200,
    'truck': 2500,
    'van': 1800
}

def calculate_insurance(car_type):
    car_type = car_type.lower()  # Convert to lowercase to handle case-insensitive input
    if car_type in insurance_rates:
        return insurance_rates[car_type]
    else:
        return None

root.mainloop()