# AgeEstimation_Tensorflow_Android

# Install tensorflow

1. $pip3 install tensorflow

2. $git clone https://github.com/tensorflow/tensorflow.git

# Prerequire: 
1. image set

UTKFace image set only for non-commercial research purposes only. The copyright belongs to the original owners. If there are any, please let me know, I will remove it immediately.

reference from original website: (https://susanqq.github.io/UTKFace/) 

2. classify the UTKFace by age 
classifier.py organize the image set into folder = AgeClassifier 

# retrain our model to learn from images
1. our dataset below AgeClassifier (remove less than 20 image folder, this might cause issue)

2. retrain model by using retrain.py

$cd tensorflow/examples/image_retraining

$python3 retrain.py --how_many_training_steps=500 --model_dir=/Users/garyhsu/workspace/git/AgeEstimation_Tensorflow_Android/tf_files --output_graph=/Users/garyhsu/workspace/git/AgeEstimation_Tensorflow_Android/tf_files/retrained_face_age_graph.pb --output_labels=/Users/garyhsu/workspace/git/AgeEstimation_Tensorflow_Android/tf_files/retrained_face_age_labels.txt --image_dir=/Users/garyhsu/workspace/git/AgeEstimation_Tensorflow_Android/AgeClassifier

# Optimize the model

$python3 optimize_for_inference.py --input=/Users/garyhsu/workspace/git/AgeEstimation_Tensorflow_Android/tf_files/retrained_face_age_graph.pb --output=/Users/garyhsu/workspace/git/AgeEstimation_Tensorflow_Android/tf_files/optimized_graph.pb --input_names="Mul" --output_names="final_result"
