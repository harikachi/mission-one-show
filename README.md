# mission-one-show

Python program which accepts an image from the local computer and identified the type of vehicle and made of vehicle along with pre configured insurance for each of the type of the car.

Prerequisites

Python 3.12.5

pip3 install azure-cognitiveservices-vision-computervision

pip3 install load_dotenv

Create two resource types as Cognitive computer vision api and customised vision api on Azure and capture the keys and end point urls.

Store these values in .env file in your local with the environment variable names as below.
  Computer vision API key and endpoint
    SUBSCRIPTION_KEY
    COMPUTER_VISION_END_POINT
  Customised Vision API key and endpoint
    PREDICTION_KEY
    PREDICTION_END_POINT
