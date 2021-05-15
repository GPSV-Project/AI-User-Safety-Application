# AI User Safety Application
## Class: CMPE 295B Major Project
## University: San Jose State University 
## Advisor: Professor Vijay Eranti

| Team Members | LinkedIn Details |
| ------------ | ----- |
| Gulnara Timokhina | https://www.linkedin.com/in/gtimokhina/ |
|Mirsaeid Abolghasemi | https://www.linkedin.com/in/saeedabi/ |
| Varun Bhaseen | https://www.linkedin.com/in/varun-bhaseen/ |

# 1. Introduction

Phishing is a security vulnerability that aims to trick unsuspecting users by mixing social engineering and website spoofing techniques into stealing their sensitive details (e.g., password, bank, or financial details). A typical phishing attack's lifecycle begins with the receipt of a fake e-mail, SMS, or instant message from scammers trying to make users think and believe that it comes from a legitimate source. The messages typically use persuasive claims and a link pointing to a fake web page that mimics the legitimate web page of the target brand.

![Application_Overview](/E-Images/Application_Overview.jpg)

Here in this project, we use an ensemble model of Char-CNN and YOLOv3 Object Detection for phishing detection and aim to create an AI agent which users can use to detect the current web page status. 


Following are the key objectives that are achieved from the AI User Safety Application:  
*  Combining object detection techniques YOLOv3 with NLP (Natural Language Processing) using Char-CNN.
*  Deploying an ensemble model on a web browser application framework optimized for performance and speed without compromising on CPU/GPU usage and memory footprint at runtime.

#2. Model Architecture

We are using an Ensemble model of YOLO and Char-CNN. Both the models are trained on Custom Dataset which can be seen in B-Dataset Folder above.

Below is the model Architecture

![Model_Architecture](/E-Images/Model_Architecture.jpg)


#3. Model Performance

Below is the Performance of YOLO Model

![YOLO_Performance](/E-Images/YOLO_Model_Performance.jpg)

Below is the performance of Char-CNN

![Char-CNN_Performance](/E-Images/Char-CNN_Model_Performance.png)

Key Points:

* The YOLOv3 and Char-CNN model is trained and evaluated over a custom dataset.
* The overall mAP score for the YOLO model is 90 (out of 100) and can accurately predict the objects as a logo. 
* The ROC curve for the Char-CNN model is 97.5% which means the model is not overfitting

#4. Final Application Screens:

Below is the Application image after running SourceCode Application.

Refer 10-Final Project Report for detailed installation instructions

![GMV AI User Safety Application Chrome Plugin Screen Shot](/E-Images/GMV_AI_USER_Safety_Application.jpg)

##Conclusion:

For full details and References refer Project report
