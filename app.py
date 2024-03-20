from flask import Flask, request, render_template, jsonify, redirect, url_for
from PIL import Image
import io
import os
import torch
from torchvision import transforms
import torch.nn as nn
import numpy as np
import csv


app = Flask(__name__)
# Dictionary of disease names to descriptions

disease_info = {
    'Apple___Apple_scab': 'Apple scab is a fungal disease that appears as gray to black scabs on the leaves, fruit, and twigs of apple trees. It can cause significant damage to apple crops.',
    'Apple___Black_rot': 'Black rot is a common disease that affects apple trees. It causes black circular lesions on the fruit and leaves, leading to fruit decay and reduced yield.',
    'Apple___Cedar_apple_rust': 'Cedar apple rust is a fungal disease that affects apple trees. It causes bright orange spots on leaves and fruit, often in conjunction with cedar trees.',
    'Apple___healthy': 'Healthy apple trees exhibit no signs of disease and have vibrant leaves and fruit.',
    'Blueberry___healthy': 'Healthy blueberry plants are free from disease and exhibit vigorous growth with no signs of leaf or fruit issues.',
    'Cherry_(including_sour)___Powdery_mildew': 'Powdery mildew is a common disease in cherry trees. It appears as white, powdery spots on leaves, leading to reduced fruit quality.',
    'Cherry_(including_sour)___healthy': 'Healthy cherry trees show no signs of disease and produce high-quality fruit.',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': 'Cercospora leaf spot, also known as gray leaf spot, is a fungal disease that affects corn (maize) plants. It causes small, gray to tan lesions on the leaves.',
    'Corn_(maize)___Common_rust_': 'Common rust is a fungal disease of corn (maize) that leads to the formation of reddish-brown pustules on the leaves.',
    'Corn_(maize)___Northern_Leaf_Blight': 'Northern leaf blight is a common fungal disease of corn (maize). It results in long, gray-green lesions on the leaves.',
    'Corn_(maize)___healthy': 'Healthy corn (maize) plants show no signs of disease and produce high-quality ears of corn.',
    'Grape___Black_rot': 'Black rot is a devastating fungal disease that affects grapevines. It leads to black, circular lesions on leaves and fruit, causing significant crop loss.',
    'Grape___Esca_(Black_Measles)': 'Esca, also known as black measles, is a disease that affects grapevines. It causes yellowing of leaves and black streaks in the wood.',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 'Leaf blight, also known as Isariopsis leaf spot, is a fungal disease that affects grapevines. It results in circular, brown lesions on the leaves.',
    'Grape___healthy': 'Healthy grapevines exhibit no signs of disease and produce high-quality grapes.',
    'Orange___Haunglongbing_(Citrus_greening)': 'Haunglongbing, also known as citrus greening, is a severe bacterial disease that affects citrus trees. It causes deformed, bitter fruit and eventual tree decline.',
    'Peach___Bacterial_spot': 'Bacterial spot is a common disease that affects peach trees. It leads to small, dark lesions on the leaves and fruit, resulting in reduced crop quality.',
    'Peach___healthy': 'Healthy peach trees show no signs of disease and produce high-quality peaches.',
    'Pepper,_bell___Bacterial_spot': 'Bacterial spot is a disease that affects bell peppers. It causes small, water-soaked lesions on the leaves and fruit.',
    'Pepper,_bell___healthy': 'Healthy bell pepper plants exhibit no signs of disease and produce vibrant, high-quality fruit.',
    'Potato___Early_blight': 'Early blight is a fungal disease that affects potato plants. It results in small, dark lesions on the leaves, leading to reduced yield.',
    'Potato___Late_blight': 'Late blight is a severe disease that affects potato plants. It leads to large, dark lesions on leaves and can cause crop devastation.',
    'Potato___healthy': 'Healthy potato plants show no signs of disease and produce high-quality tubers.',
    'Raspberry___healthy': 'Healthy raspberry plants are free from disease and produce high-quality fruit.',
    'Soybean___healthy': 'Healthy soybean plants show no signs of disease and produce healthy, high-yield crops.',
    'Squash___Powdery_mildew': 'Powdery mildew is a fungal disease that affects squash plants. It appears as white, powdery spots on the leaves, leading to reduced fruit quality.',
    'Strawberry___Leaf_scorch': 'Leaf scorch is a disease that affects strawberry plants. It results in brown, scorched areas on the leaves.',
    'Strawberry___healthy': 'Healthy strawberry plants are free from disease and produce high-quality fruit.',
    'Tomato___Bacterial_spot': 'Bacterial spot is a common disease that affects tomato plants. It leads to small, water-soaked lesions on the leaves and fruit, reducing crop quality.',
    'Tomato___Early_blight': 'Early blight is a fungal disease that affects tomato plants. It results in small, dark lesions on the leaves and can cause yield reduction.',
    'Tomato___Late_blight': 'Late blight is a severe disease that affects tomato plants. It leads to large, dark lesions on leaves and can cause significant crop loss.',
    'Tomato___Leaf_Mold': 'Leaf mold is a fungal disease that affects tomato plants. It appears as brown, felt-like patches on the leaves.',
    'Tomato___Septoria_leaf_spot': 'Septoria leaf spot is a common disease in tomato plants. It results in small, circular lesions on the leaves.',
    'Tomato___Spider_mites Two-spotted_spider_mite': 'Spider mites, including the two-spotted spider mite, are common pests that can damage tomato plants. They suck sap from the leaves, leading to stippling and reduced growth.',
    'Tomato___Target_Spot': 'Target spot is a fungal disease that affects tomato plants. It results in dark lesions with concentric rings on the leaves.',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 'Tomato yellow leaf curl virus is a viral disease that affects tomato plants. It causes curling and yellowing of leaves, leading to reduced fruit quality.',
    'Tomato___Tomato_mosaic_virus': 'Tomato mosaic virus is a viral disease that affects tomato plants. It causes mottled leaves and can reduce fruit quality.',
    'Tomato___healthy': 'Healthy tomato plants show no signs of disease and produce high-quality fruit.'
}
def read_disease_information():
    disease_information = {}
    with open('disease_information.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            disease_name = row['Disease Name']
            disease_information[disease_name] = {
                'Symptoms': row['Symptoms'],
                'Causes': row['Causes'],
                'Treatments': row['Treatments'],
                'Description': disease_info.get(disease_name, 'No information available')
            }
    return disease_information


def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
    ])
    image = transform(image).unsqueeze(0)
    return image

def predict_disease(image, model):
    with torch.no_grad():
        image = preprocess_image(image)
        output = model(image)
        _, predicted_class = torch.max(output, 1)
        class_labels = [
            'Apple___Apple_scab',
            'Apple___Black_rot',
            'Apple___Cedar_apple_rust',
            'Apple___healthy',
            'Blueberry___healthy',
            'Cherry_(including_sour)___Powdery_mildew',
            'Cherry_(including_sour)___healthy',
            'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
            'Corn_(maize)___Common_rust_',
            'Corn_(maize)___Northern_Leaf_Blight',
            'Corn_(maize)___healthy',
            'Grape___Black_rot',
            'Grape___Esca_(Black_Measles)',
            'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
            'Grape___healthy',
            'Orange___Haunglongbing_(Citrus_greening)',
            'Peach___Bacterial_spot',
            'Peach___healthy',
            'Pepper,_bell___Bacterial_spot',
            'Pepper,_bell___healthy',
            'Potato___Early_blight',
            'Potato___Late_blight',
            'Potato___healthy',
            'Raspberry___healthy',
            'Soybean___healthy',
            'Squash___Powdery_mildew',
            'Strawberry___Leaf_scorch',
            'Strawberry___healthy',
            'Tomato___Bacterial_spot',
            'Tomato___Early_blight',
            'Tomato___Late_blight',
            'Tomato___Leaf_Mold',
            'Tomato___Septoria_leaf_spot',
            'Tomato___Spider_mites Two-spotted_spider_mite',
            'Tomato___Target_Spot',
            'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
            'Tomato___Tomato_mosaic_virus',
            'Tomato___healthy'
        ]
        predicted_disease = class_labels[predicted_class.item()]
        return predicted_disease

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        try:
            # Load the saved ResNet-50 model
            class block(nn.Module):
                def __init__(self, in_channels, intermediate_channels, identity_downsample=None, stride=1):
                    super().__init__()
                    self.expansion = 4
                    self.conv1 = nn.Conv2d(in_channels, intermediate_channels, kernel_size=1, stride=1, padding=0, bias=False)
                    self.bn1 = nn.BatchNorm2d(intermediate_channels)
                    self.conv2 = nn.Conv2d(intermediate_channels, intermediate_channels, kernel_size=3, stride=stride, padding=1, bias=False)
                    self.bn2 = nn.BatchNorm2d(intermediate_channels)
                    self.conv3 = nn.Conv2d(intermediate_channels, intermediate_channels * self.expansion, kernel_size=1, stride=1, padding=0, bias=False)
                    self.bn3 = nn.BatchNorm2d(intermediate_channels * self.expansion)
                    self.relu = nn.ReLU()
                    self.identity_downsample = identity_downsample
                    self.stride = stride

                def forward(self, x):
                    identity = x.clone()

                    x = self.conv1(x)
                    x = self.bn1(x)
                    x = self.relu(x)
                    x = self.conv2(x)
                    x = self.bn2(x)
                    x = self.relu(x)
                    x = self.conv3(x)
                    x = self.bn3(x)

                    if self.identity_downsample is not None:
                        identity = self.identity_downsample(identity)

                    x += identity
                    x = self.relu(x)
                    return x

            class ResNet(nn.Module):
                def __init__(self, block, layers, image_channels, num_classes):
                    super(ResNet, self).__init__()
                    self.in_channels = 64
                    self.conv1 = nn.Conv2d(image_channels, 64, kernel_size=7, stride=2, padding=3, bias=False)
                    self.bn1 = nn.BatchNorm2d(64)
                    self.relu = nn.ReLU()
                    self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

                    # Essentially the entire ResNet architecture are in these 4 lines below
                    self.layer1 = self._make_layer(block, layers[0], intermediate_channels=64, stride=1)
                    self.layer2 = self._make_layer(block, layers[1], intermediate_channels=128, stride=2)
                    self.layer3 = self._make_layer(block, layers[2], intermediate_channels=256, stride=2)
                    self.layer4 = self._make_layer(block, layers[3], intermediate_channels=512, stride=2)

                    self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
                    self.fc = nn.Linear(512 * 4, num_classes)

                def forward(self, x):
                    x = self.conv1(x)
                    x = self.bn1(x)
                    x = self.relu(x)
                    x = self.maxpool(x)
                    x = self.layer1(x)
                    x = self.layer2(x)
                    x = self.layer3(x)
                    x = self.layer4(x)

                    x = self.avgpool(x)
                    x = x.reshape(x.shape[0], -1)
                    x = self.fc(x)

                    return x

                def _make_layer(self, block, num_residual_blocks, intermediate_channels, stride):
                    identity_downsample = None
                    layers = []

                    if stride != 1 or self.in_channels != intermediate_channels * 4:
                        identity_downsample = nn.Sequential(
                            nn.Conv2d(self.in_channels, intermediate_channels * 4, kernel_size=1, stride=stride, bias=False),
                            nn.BatchNorm2d(intermediate_channels * 4),
                        )

                    layers.append(block(self.in_channels, intermediate_channels, identity_downsample, stride))

                    self.in_channels = intermediate_channels * 4

                    for i in range(num_residual_blocks - 1):
                        layers.append(block(self.in_channels, intermediate_channels))

                    return nn.Sequential(*layers)

            def ResNet50(img_channel=3, num_classes=38):  # Adjust the number of classes as needed
                return ResNet(block, [3, 4, 6, 3], img_channel, num_classes)

            model = ResNet50(3, 38)  # Ensure to provide the correct number of classes
            model.load_state_dict(torch.load('plant-disease-model.pth', map_location=torch.device('cpu')))
            model.eval()

            image = Image.open(file)
            image.save('static/uploaded_image.jpg')  # Save the uploaded image on the server

            predicted_disease = predict_disease(image, model)

            # Redirect to the result page with the prediction
            return redirect(url_for('display_result', result=predicted_disease))
        except Exception as e:
            return jsonify({'error': str(e)})

@app.route('/result/<result>', methods=['GET'])
def display_result(result):
    # Assuming you have stored the uploaded image on the server
    # You can change 'image_filename' to the actual filename of the uploaded image
    image_filename = 'uploaded_image.jpg'
    image_url = url_for('static', filename=image_filename)
    # Read the combined disease information from the CSV and the disease_info dictionary
    combined_disease_information = read_disease_information()

    if result in combined_disease_information:
        disease_description = combined_disease_information[result]
    else:
        disease_description = {
            'name': 'Unknown',
            'Symptoms': 'No information available',
            'Causes': 'No information available',
            'Treatments': 'No information available',
            'Description': 'No information available'
        }
    return render_template('result.html', result=result, disease_description=disease_description, image_url=image_url)


if __name__ == '__main__':
    app.run(debug=True)
