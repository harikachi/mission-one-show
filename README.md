# mission-one-show

Python program which accepts an image from the local computer and identified the type of vehicle and made of vehicle along with pre configured insurance for each of the type of the car.

Prerequisites

Python 3.12.5

pip3 install azure-cognitiveservices-vision-computervision

pip3 install load_dotenv

Create a resources with type as Custom Vision under market place of Azure portal and grab the API key and endpoint URL.
Carate another resource with type as Computer Vision under market place of Azure portal and grab the API key and endpoint URL.

Store these values in .env file in your local with the environment variable names as below.
  Computer vision API key and endpoint
    SUBSCRIPTION_KEY
    COMPUTER_VISION_END_POINT
  Customised Vision API key and endpoint
    PREDICTION_KEY
    PREDICTION_END_POINT

Run the AnalyzeImage.py program and upload a sample image from your local machine.
