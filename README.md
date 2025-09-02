**# Stratification-of-Garbage-using-Deep-Learning**

In many countries recycling became the paramount of this decade. The easiest way to recycle the garbage is to classify them into several categories. In this article we will detect the single waste object which are classified into glass, paper, steel, plastic etc. by 
giving the dataset of images and videos. We use several deep learning algorithms such as SVM, CNN in order to classify the garbage. The accuracy provided by this algorithms is so efficient and quick and the best way.

**1.1 SOCIAL OUTCOMES**
Improved waste management: A garbage classification system using deep learning can improve waste management by enabling efficient sorting of garbage based on their type. 
This can help in reducing the amount of waste sent to landfills and promote recycling and reuse of materials.Reduced environmental impact: Improper disposal of waste can have a significant impact on the environment, such as water and soil pollution, greenhouse gas emissions, and depletion of natural resources. By accurately classifying garbage using deep learning, the project can contribute to reducing the environmental impact of waste.Enhanced public health and hygiene: Unsorted garbage can lead to the proliferation of 
pests and diseases, which can have adverse effects on public health and hygiene. A garbage classification system can help in minimizing the risk of such problems by ensuring proper disposal of waste.Employment opportunities: A garbage classification project can create employment opportunities for individuals involved in garbage collection, sorting, and processing. This can help in promoting economic development and reducing poverty in the community.

**1.2 HARDWARE REQUIREMENTS**
First, the hardware specifications were determined. High processing power is needed by the deep learning models used for semantic segmentation of biological pictures. Thus, a 
server equipped with a GPU was necessary to manage the computing demands. The server utilised for this research has an Intel Xeon CPU, 32GB of RAM, and an NVIDIA Quadro RTX 
8000 GPU as part of its hardware requirements.Our project's hardware specifications are essential since they affect how well our 
application performs. The required hardware parts are as follows:
CPU: To guarantee the application runs well, we advise using a processor with at least 2 
cores and a clock speed of 2.5 GHz.
GPU: A dedicated GPU with at least 4GB of VRAM, such as the Nvidia GeForce GTX 1050 
Ti or above, is advised because the DRS-UNET model demands a lot of computing power. 
This will allow for quicker segmentation and inference.
Memory: The computer should have at least 8GB of RAM in order to guarantee that the 
application runs well and that the model can be loaded without any issues.
Storage: It is advised to have at least 500GB of storage available to keep the dataset, 
model, and other pertinent information.
Network: The system requires a consistent internet connection with a minimum speed of 
10 Mbps for best performance.
These hardware specifications are necessary to ensure that the application can manage 
the segmentation of medical pictures without any delay and provide accurate findings in 
real-time.
**1.2 SOFTWARE REQUIREMENTS**
Next, the software requirements were looked at. The deep learning models were Stratification of Garbage using Deep Learning
developed using Python and many libraries, such as TensorFlow and Keras. The web application was created using the JavaScript frontend framework Angular and the Flask web framework. On a Linux server, the application was set up, and MySQL was used to manage the database.
The project's software needs are as follows:
● Python: Python is an interpreted high-level programming language used for a wide 
range of applications, including web development, scientific computing, data 
analysis, and artificial intelligence. From the official website, open-source software 
can be downloaded and installed.
● Google created the open-source TensorFlow software library for dataflow and 
differentiable programming across a variety of workloads. Applications involving 
deep learning and machine learning use it. The Python package management 
system pip can be used to install TensorFlow.
● An open-source software library called Keras is used to create and train deep 
learning models. It offers a high-level API for creating and training deep learning 
models and is developed in Python. Pip may be used to install Keras.
● Scikit-image: Scikit-image is free software for computer vision and image 
processing. It offers techniques for feature extraction, segmentation, filtering, and 
image processing. Pip can be used to install Scikit-image.
● Scikit-fuzzy is an open-source software toolkit for fuzzy logic. It offers algorithms 
for fuzzy image processing, fuzzy clustering, and fuzzy control systems. Pip can be 
used to install Scikit-fuzzy.
● Flask: A simple Python web framework used to create the application's back end. 
Small to medium-sized web applications can be created with Flask without the 
need for a larger framework's scalability.
● The online application uses MySQL, a well-liked open-source relational database 
management system, to store and manage its data. The aforementioned software 
tools and frameworks were chosen for the project requirement
