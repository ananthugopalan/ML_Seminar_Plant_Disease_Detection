import csv

# Define the disease information as a list of dictionaries
disease_info = [
    {
        "Disease Name": "Apple___Apple_scab",
        "Symptoms": "Apple scab typically presents as gray to black scabs on leaves and fruit. In advanced stages, you may notice a velvety texture on the underside of leaves.",
        "Causes": "The disease is caused by the fungus Venturia inaequalis. It spreads through water splashes during rainfall or irrigation.",
        "Treatments": "Control measures include the use of fungicides specifically designed for apple scab, implementing proper pruning to improve air circulation, and maintaining good sanitation in the orchard. Avoid overhead watering to reduce disease spread."
    },
    {
        "Disease Name": "Apple___Black_rot",
        "Symptoms": "Black rot manifests as black circular lesions on fruit and leaves. Infected fruit may shrivel and become mummified.",
        "Causes": "Black rot is caused by the fungus Botryosphaeria obtusa. The fungus thrives in wet conditions, making proper drainage crucial.",
        "Treatments": "Effective control measures include the application of fungicides, regular pruning to remove infected branches, and the removal of infected fruit to prevent the disease's spread."
    },
    {
        "Disease Name": "Apple___Cedar_apple_rust",
        "Symptoms": "Bright orange spots appear on leaves and fruit. In some cases, the disease may also affect cedar trees near the apple orchard.",
        "Causes": "Cedar apple rust is caused by the fungus Gymnosporangium juniperi-virginianae. It requires both apple and cedar hosts for its life cycle.",
        "Treatments": "Control methods involve the use of fungicides, the removal of nearby cedar trees if possible, and other cultural practices."
    },
    {
        "Disease Name": "Apple___healthy",
        "Symptoms": "Apple trees labeled as 'healthy' show no signs of disease symptoms, with leaves and fruit looking normal.",
        "Causes": "No specific disease is affecting the tree.",
        "Treatments": "Maintain the health of the apple tree through general tree care and maintenance practices, which include proper pruning, pest control, and disease prevention."
    },
    {
        "Disease Name": "Blueberry___healthy",
        "Symptoms": "Blueberry plants labeled as 'healthy' exhibit no disease symptoms, with leaves and fruit appearing normal.",
        "Causes": "The blueberry plants are not affected by any specific diseases.",
        "Treatments": "Maintain healthy blueberry plants through proper pruning, fertilization, and effective pest control practices."
    },
    {
        "Disease Name": "Cherry_(including_sour)___Powdery_mildew",
        "Symptoms": "Powdery mildew is characterized by the presence of white, powdery spots on leaves. Severe infestations can lead to leaf distortion and reduced fruit quality.",
        "Causes": "The disease is caused by various species of the fungus Podosphaera, and it thrives in conditions of high humidity.",
        "Treatments": "Control methods include the application of appropriate fungicides, regular pruning to improve air circulation, and spacing cherry trees adequately to reduce humidity."
    },
    {
        "Disease Name": "Cherry_(including_sour)___healthy",
        "Symptoms": "Cherry trees labeled as 'healthy' do not exhibit any disease symptoms, with leaves and fruit appearing normal.",
        "Causes": "The cherry trees are not affected by any specific diseases.",
        "Treatments": "Maintain the health of the cherry trees through proper pruning, effective pest control, and disease prevention practices."
    },
    {
        "Disease Name": "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
        "Symptoms": "Cercospora leaf spot, also known as gray leaf spot, appears as gray to tan lesions on the leaves. The disease can cause significant damage if not managed.",
        "Causes": "Cercospora zeae-maydis is the fungus responsible for this disease, and it thrives in warm and humid conditions.",
        "Treatments": "Control methods involve the use of fungicides designed to combat Cercospora leaf spot, crop rotation to reduce disease pressure, and planting resistant corn varieties."
    },
    {
        "Disease Name": "Corn_(maize)___Common_rust",
        "Symptoms": "Common rust is identified by reddish-brown pustules that develop on the leaves, reducing photosynthesis and overall plant health.",
        "Causes": "The fungus Puccinia sorghi is responsible for common rust. It thrives in warm, humid conditions.",
        "Treatments": "Control measures include the application of fungicides specific to common rust, and in some cases, planting resistant corn varieties can help reduce the impact of the disease."
    },
    {
        "Disease Name": "Corn_(maize)___Northern_Leaf_Blight",
        "Symptoms": "Northern leaf blight is characterized by long, gray-green lesions on the leaves. Severe infections can reduce yield and quality.",
        "Causes": "The disease is caused by the fungus Exserohilum turcicum, and it thrives in warm and humid conditions.",
        "Treatments": "Control strategies include the use of appropriate fungicides, crop rotation to reduce disease pressure, and planting resistant corn varieties where available."
    },
    {
        "Disease Name": "Corn_(maize)___healthy",
        "Symptoms": "Corn plants labeled as 'healthy' do not display any disease symptoms, with leaves and fruit looking normal.",
        "Causes": "The corn plants are not affected by any specific diseases.",
        "Treatments": "Maintain the health of the corn crops through proper planting and crop management practices, which include timely planting, effective pest control, and disease prevention measures."
    },
    {
        "Disease Name": "Grape___Black_rot",
        "Symptoms": "Black rot causes black circular lesions that can extend to the stems and may affect the entire grape cluster.",
        "Causes": "The disease is caused by the fungus Guignardia bidwellii, which thrives in warm and humid conditions.",
        "Treatments": "Control measures include the application of fungicides specific to black rot, regular pruning to improve air circulation, and the removal of infected fruit to prevent disease spread."
    },
    {
        "Disease Name": "Grape___Esca (Black Measles)",
        "Symptoms": "Esca, also known as black measles, leads to yellowing of leaves and black streaks in the wood of grapevines.",
        "Causes": "Esca is caused by various Phaeoacremonium species and other fungi. The disease is often associated with stress on the vine.",
        "Treatments": "Control strategies involve pruning to reduce stress on the vine and proper vineyard management to minimize disease pressure."
    },
    {
        "Disease Name": "Grape___Leaf_blight (Isariopsis Leaf Spot)",
        "Symptoms": "Leaf blight, also known as Isariopsis leaf spot, appears as circular, brown lesions on the leaves, which can affect grape health and yield.",
        "Causes": "The disease is caused by various species of the fungus Isariopsis. It thrives in conditions of high humidity.",
        "Treatments": "Control measures include the application of specific fungicides, regular pruning to improve air circulation, and ensuring proper vine spacing to reduce humidity and disease pressure."
    },
    {
        "Disease Name": "Grape___healthy",
        "Symptoms": "Grapevines labeled as 'healthy' do not exhibit any disease symptoms, with leaves and fruit appearing normal.",
        "Causes": "The grapevines are not affected by any specific diseases.",
        "Treatments": "Maintain the health of the grapevines through proper pruning, effective pest control, and disease prevention practices."
    },
    {
        "Disease Name": "Orange___Haunglongbing (Citrus greening)",
        "Symptoms": "Haunglongbing, also known as citrus greening, leads to deformed, bitter fruit and leaf mottling.",
        "Causes": "The disease is caused by various Candidatus Liberibacter species and is primarily transmitted by citrus psyllids.",
        "Treatments": "Control methods include the application of pesticides, the removal of infected trees to prevent disease spread, and the management of psyllid vectors."
    },
    {
        "Disease Name": "Peach___Bacterial_spot",
        "Symptoms": "Bacterial spot manifests as small, dark lesions on the leaves and fruit, causing cosmetic damage.",
        "Causes": "The disease is caused by the bacterium Xanthomonas arboricola pv. pruni, and it can spread through rain splashes and wind.",
        "Treatments": "Control strategies involve the use of copper-based fungicides, pruning to remove infected branches, and the removal of infected fruit to prevent disease spread."
    },
    {
        "Disease Name": "Peach___healthy",
        "Symptoms": "Peach trees labeled as 'healthy' show no signs of disease symptoms, with leaves and fruit looking normal.",
        "Causes": "No specific disease is affecting the tree.",
        "Treatments": "Maintain the health of the peach trees through general tree care and maintenance practices, which include proper pruning, pest control, and disease prevention."
    },
    {
        "Disease Name": "Pepper,_bell___Bacterial_spot",
        "Symptoms": "Bacterial spot is characterized by small, water-soaked lesions on the leaves and fruit, which can lead to reduced fruit quality.",
        "Causes": "The disease is caused by various Xanthomonas species, and it can spread through rain splashes and wind.",
        "Treatments": "Control methods involve the use of copper-based fungicides, pruning to remove infected plants, and the implementation of measures to reduce disease spread, such as proper plant spacing."
    },
    {
        "Disease Name": "Pepper,_bell___healthy",
        "Symptoms": "Bell pepper plants labeled as 'healthy' do not display any disease symptoms, with leaves and fruit looking normal.",
        "Causes": "The bell pepper plants are not affected by any specific diseases.",
        "Treatments": "Maintain the health of the bell pepper plants through proper pruning, effective pest control, and disease prevention practices."
    },
    {
        "Disease Name": "Potato___Early_blight",
        "Symptoms": "Early blight is characterized by small, dark lesions on the leaves, which can reduce the plant's photosynthetic capacity.",
        "Causes": "The disease is caused by the fungus Alternaria solani, and it is favored by warm and humid conditions.",
        "Treatments": "Control strategies involve the use of fungicides designed for early blight, proper crop rotation to reduce disease pressure, and the removal of infected leaves to limit disease spread."
    },
    {
        "Disease Name": "Potato___Late_blight",
        "Symptoms": "Late blight presents as large, dark lesions on the leaves, which can lead to rapid defoliation and yield loss.",
        "Causes": "Late blight is caused by the oomycete Phytophthora infestans, and it thrives in cool and moist conditions.",
        "Treatments": "Control methods include the application of fungicides specific to late blight, planting resistant potato varieties if available, and ensuring proper plant spacing for air circulation."
    },
    {
        "Disease Name": "Potato___healthy",
        "Symptoms": "Potato plants labeled as 'healthy' do not show any disease symptoms, with leaves and tubers appearing normal.",
        "Causes": "No specific disease is affecting the plants.",
        "Treatments": "Maintain the health of the potato plants through proper planting, effective pest control, and disease prevention practices."
    },
    {
        "Disease Name": "Raspberry___healthy",
        "Symptoms": "Raspberry plants labeled as 'healthy' do not exhibit any disease symptoms, with leaves and fruit appearing normal.",
        "Causes": "The raspberry plants are not affected by any specific diseases.",
        "Treatments": "Maintain the health of the raspberry plants through proper pruning, effective pest control, and disease prevention practices."
    },
    {
        "Disease Name": "Soybean___healthy",
        "Symptoms": "Soybean plants labeled as 'healthy' do not display any disease symptoms, with leaves and pods looking normal.",
        "Causes": "The soybean plants are not affected by any specific diseases.",
        "Treatments": "Maintain the health of the soybean plants through proper planting and crop management practices, which include timely planting, effective pest control, and disease prevention measures."
    },
    {
        "Disease Name": "Squash___Powdery_mildew",
        "Symptoms": "Powdery mildew is characterized by white, powdery spots on the leaves, which can reduce photosynthesis and hinder growth.",
        "Causes": "The disease is caused by various species of the fungus Podosphaera, and it thrives in dry and warm conditions.",
        "Treatments": "Control methods involve the use of appropriate fungicides, ensuring proper plant spacing for air circulation, and conducting pruning to remove infected leaves."
    },
    {
        "Disease Name": "Strawberry___Leaf_scorch",
        "Symptoms": "Leaf scorch presents as brown, scorched areas on the leaves, affecting the overall health and yield of the strawberry plant.",
        "Causes": "The disease is caused by the fungus Diplocarpon earlianum, and it thrives in conditions of high humidity.",
        "Treatments": "Control measures include the application of specific fungicides, ensuring proper plant spacing for air circulation, and conducting pruning to remove infected leaves."
    },
    {
        "Disease Name": "Strawberry___healthy",
        "Symptoms": "Strawberry plants labeled as 'healthy' do not show any disease symptoms, with leaves and fruit looking normal.",
        "Causes": "The strawberry plants are not affected by any specific diseases.",
        "Treatments": "Maintain the health of the strawberry plants through proper pruning, effective pest control, and disease prevention practices."
    },
    {
        "Disease Name": "Tomato___Bacterial_spot",
        "Symptoms": "Bacterial spot is characterized by small, water-soaked lesions on the leaves and fruit, which can lead to reduced fruit quality.",
        "Causes": "The disease is caused by the bacterium Xanthomonas campestris pv. vesicatoria, and it can spread through rain splashes and wind.",
        "Treatments": "Control methods involve the use of copper-based fungicides, proper plant spacing to reduce humidity, and the removal of infected leaves to prevent disease spread."
    },
    {
        "Disease Name": "Tomato___Early_blight",
        "Symptoms": "Early blight is identified by small, dark lesions on the leaves, which can reduce the plant's photosynthetic capacity.",
        "Causes": "The disease is caused by the fungus Alternaria solani, and it is favored by warm and humid conditions.",
        "Treatments": "Control strategies involve the use of fungicides specific to early blight, proper plant spacing for air circulation, and the removal of infected leaves to limit disease spread."
    },
    {
        "Disease Name": "Tomato___Late_blight",
        "Symptoms": "Late blight presents as large, dark lesions on the leaves, which can lead to rapid defoliation and yield loss.",
        "Causes": "Late blight is caused by the oomycete Phytophthora infestans, and it thrives in cool and moist conditions.",
        "Treatments": "Control methods include the application of fungicides specific to late blight, planting resistant tomato varieties if available, and ensuring proper plant spacing for air circulation."
    },
    {
        "Disease Name": "Tomato___Leaf_Mold",
        "Symptoms": "Leaf mold is characterized by brown, felt-like patches on the leaves, which can hinder photosynthesis and fruit production.",
        "Causes": "The disease is caused by the fungus Passalora fulva, and it thrives in conditions of high humidity.",
        "Treatments": "Control measures include the application of specific fungicides, proper plant spacing for adequate ventilation, and the removal of infected leaves to limit disease spread."
    },
    {
        "Disease Name": "Tomato___Septoria_leaf_spot",
        "Symptoms": "Septoria leaf spot presents as small, circular lesions on the leaves, which can lead to leaf loss and reduced yield.",
        "Causes": "The disease is caused by the fungus Septoria lycopersici, and it is favored by moisture and warm conditions.",
        "Treatments": "Control strategies involve the use of appropriate fungicides, proper plant spacing for air circulation, and the removal of infected leaves to reduce disease pressure."
    },
    {
        "Disease Name": "Tomato___Spider_mites Two-spotted spider mite",
        "Symptoms": "Infestations of two-spotted spider mites can cause stippling on leaves, webbing, and reduced plant growth.",
        "Causes": "The pest, Tetranychus urticae, can proliferate rapidly in dry and warm conditions.",
        "Treatments": "Control methods include the introduction of predatory mites, the application of insecticidal soap, and the use of miticides to manage spider mite populations."
    },
    {
        "Disease Name": "Tomato___Target_Spot",
        "Symptoms": "Target spot is characterized by dark lesions with concentric rings on the leaves, which can hinder photosynthesis and reduce plant health.",
        "Causes": "The disease is caused by the fungus Corynespora cassiicola, and it can spread in warm and humid conditions.",
        "Treatments": "Control measures involve the application of specific fungicides, proper plant spacing for air circulation, and the removal of infected leaves to reduce disease pressure."
    },
    {
        "Disease Name": "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
        "Symptoms": "Tomato yellow leaf curl virus leads to the curling and yellowing of leaves, reduced fruit quality, and stunted plant growth.",
        "Causes": "The virus, Tomato yellow leaf curl virus, is primarily transmitted by whiteflies.",
        "Treatments": "Control methods include planting resistant tomato varieties, effective pest control to manage whiteflies, and the removal of infected plants to prevent further spread."
    },
    {
        "Disease Name": "Tomato___Tomato_mosaic_virus",
        "Symptoms": "Mottled leaves and reduced fruit quality are common symptoms of tomato mosaic virus.",
        "Causes": "The virus, Tomato mosaic virus, can be transmitted by various means, including contaminated tools and plant sap.",
        "Treatments": "Control strategies involve planting resistant tomato varieties, effective pest control, and the removal of infected plants to prevent disease spread."
    },
    {
        "Disease Name": "Tomato___healthy",
        "Symptoms": "Tomato plants labeled as 'healthy' do not display any disease symptoms, with leaves and fruit appearing normal.",
        "Causes": "The tomato plants are not affected by any specific diseases.",
        "Treatments": "Maintain the health of the tomato plants through proper planting and care practices, including timely planting, effective pest control, and disease prevention measures."
    }
]


# Specify the CSV file path
csv_file = "disease_information.csv"

# Create and write the data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    fieldnames = ["Disease Name", "Symptoms", "Causes", "Treatments"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Write the disease information
    for info in disease_info:
        writer.writerow(info)

print(f"Disease information has been written to {csv_file}")
