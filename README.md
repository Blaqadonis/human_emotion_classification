# human_emotion_classification


![image](https://user-images.githubusercontent.com/100685852/208330166-d93d1c4f-c160-4923-83ce-cd8fb4e317d0.png)




With over 5000 images, grouped into one of the following classes: 'anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutrality', 'sadness', and 'surprise', the task at hand was straightforward:
Build a deep learning model that predicts someone's emotion in an image by simply supplying my model with the url of the image. I used a pretrained Xception model to achieve this task.

Here is a breakdown of how to run this project:
1. Clone this repo.

2. In terminal, run 
'''pip install tensorflow'''.

3. Then,
'''pip install keras-image-helper'''.

4. Next, run 
'''pip install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime'''.

5. run 
'''docker build -t emotion-model .'''

6. run 
'''pip install awscli'''

7. run 
'''aws configure'''. 

8. Log in to your aws account and get Access ID and key from security credentials. Enter appropriately. Enter <aws region> and 'json' for output.
Next, run 
'''aws ecr create-repository --repository-name emotion-tflite.images'''

 9. Copy 'repositoryArn' from repositories in Elastic Container Registry on AWS. Then Run 
'''$(aws ecr get-login --no-include-email)'''

10. Open docker desktop. Run the image.
Run
'''docker tag emotion-model:latest <URI>'''

11. Then
''' docker push <URI> '''

12. Search lambda in AWS. Create new function. Test function and invoke it. expose function on API, and delpoy it.
