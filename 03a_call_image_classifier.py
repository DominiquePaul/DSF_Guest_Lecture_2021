import os

from google.cloud import automl


# Some specifications
project_id = "1025551338418"
model_id = "ICN5998708941750534144"

file_path = "./images/banana3.png"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./gcp_credentials/dscs2020-b20a630b58a2.json"

def load_image_as_bytes(file_path):
    # Read the file.
    with open(file_path, "rb") as content_file:
        content = content_file.read()

    return content

def classify_image_with_automl(image_as_bytes):

    prediction_client = automl.PredictionServiceClient()

    # Get the full path of the model.
    model_full_id = automl.AutoMlClient.model_path(
        project_id, "us-central1", model_id
    )

    image = automl.Image(image_bytes=image_as_bytes)
    payload = automl.ExamplePayload(image=image)

    request = automl.PredictRequest(
        name=model_full_id,
        payload=payload
    )

    result = prediction_client.predict(request=request)
    result = result.payload[0]

    return(result.display_name, result.classification.score)


# if __name__ == "__main__":

img = load_image_as_bytes(file_path)
prediction, score = classify_image_with_automl(img)

print(prediction)
print(score)
