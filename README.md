# human_emotion_classification

With over 5000 images in grayscale, grouped into one of the following classes: 'anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutrality', 'sadness', and 'surprise', the task at hand was straightforward:
Build a deep learning model that predicts someone's mood in an image by simply supplying my model with the url of the image. I used a pretrained Xception model to achieve this task.

Here is a breakdown of how to run this project:
1. Clone this repo.
2. In terminal, run 
'''pip install tensorflow'''.
Then,
'''pip install keras-image-helper'''.
Next, run 
'''pip install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime'''.

run 
'''docker build -t emotion-model .'''
Run 
'''pip install awscli'''
Run 
'''aws configure'''. 
Log in to your aws account and get Access ID and key from security credentials. Enter appropriately. Enter <aws region> and 'json' for output.
Next, run 
'''aws ecr create-repository --repository-name emotion-tflite.images'''
 Copy 'repositoryArn' from repositories in Elastic Container Registry on AWS. Then Run 
'''$(aws ecr get-login --no-include-email)'''
Open docker desktop. Run the image.
Run
'''docker tag emotion-model:latest <URI>'''
Then
''' docker push <URI> '''
Search lambda in AWS. Create new function. Test function and invoke it. expose function on API, and delpoy it.
