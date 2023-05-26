# licenseplatedetectio
KMITL Robotics Lab 3 Final Project
- [YoloV8(1).ipynb] Run on Google Colab alongside dataset exported from Roboflow to train the model
- [best.pt] Model with best accuracy (https://drive.google.com/file/d/1Hu9AUnyitQUZj5V9SLJfDnWroUx51RR8/view?usp=sharing)
- [Testrun.mp4] Demo video that can be used with the model (https://kmitlthailand-my.sharepoint.com/:v:/g/personal/64110092_kmitl_ac_th/EQ6txxjHYd9GrTv9N4hyB9sBdGJochQPHCjsafOiGl1TFA?e=gYAt6T)

Introduction
This project is about creating a model that can detect cars and motorcycle license plates from images and video footage.

Task 1 – Data Acquisition
We acquire images used in our dataset by combination of saving images from Google Search, YouTube videos, and photos taken by ourselves. The images we gather include the close up of the license plate, image of cars/motorcycle passing by, image of parked cars so the quality, blurriness and sizes of the images may vary but we focused on detecting the license plate. 

Task 2 – Data Preparation
After gathering some images, we uploaded and annotated those images on Roboflow. We then went back and forth between data acquisition, preparation and model training as we train the model based on the dataset we had at that time on Roboflow to see if the quality and quantity of our dataset is enough to train an accurate model. We also use the Label Assist function on Roboflow while Annotating to see if the current model can find the license plate in the images as it was a good way to find blind spots of the model. Every batch of images we upload into the dataset, we split them in 70% Train / 20% Valid / 10% Test. We gather a total of 600 images, which were then are augmented by using shear and blur for example to generate more images for training which we end up with around 1,500 images.

Task 3 – Model Training and deploy 
Since the model trained and its score on Roboflow can be a good indicator for a good dataset, we can check if we need to add more variety to the dataset after finishing training the model one each time and check its accuracy/mean average precision score. After we believe we have gathered enough images to create an accurate model or train a model with high precision, we exported the dataset in YOLOv8 format into Jupyter code so we can import the dataset into Google Colab and custom train our model there. Other than choosing which training model is more accurate, we also need to know which python libraries are needed to be able to use them as well. 

Task 4 – Model Inference 
The footage used in the inference could only be video footage or still image of the car. 

