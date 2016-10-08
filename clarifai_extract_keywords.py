from clarifai.client import ClarifaiApi


def get_keywords_for_image(img_url):
    """ Gets the keyword associated with the image through the Clarifai API """

    clarifai_api = ClarifaiApi() # assumes environment variables are set.
    result = clarifai_api.tag_images(open(img_url, "rb"))
    return result['results'][0]['result']['tag']['classes']

print(get_keywords_for_image("clarifai_test_images/college_party_3.png"))
