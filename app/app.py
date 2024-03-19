import json
import os
import ssl
from flask import Flask, request, render_template
import urllib.request


from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
url = os.getenv('API_URL')


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context


# this line is needed if you use self-signed certificate in your scoring service.
allowSelfSignedHttps(True)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    joke = ''
    deployment = ''
    if request.method == 'POST':
        topic = request.form.get('topic')
        joke, deployment = get_joke(topic)
    return render_template('home.html', joke=joke, deployment=deployment)


def get_joke(topic):

    data = {
        "topic": topic
    }

    body = str.encode(json.dumps(data))

    # api_key = ''
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    headers = {
        'Content-Type':'application/json',
        'Authorization':('Bearer '+ api_key),
        # 'azureml-model-deployment': 'mutaza-0073-romam-languages'
        }

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(response.headers['azureml-model-deployment'])
        deployment = response.headers['azureml-model-deployment']
        print('\n')
        # Assuming `result` contains the JSON response
        response_dict = json.loads(result)
        print(response_dict['joke'])
        return response_dict['joke'], deployment

    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))
        return error.read().decode("utf8", 'ignore')


if __name__ == '__main__':
    app.run(debug=True)
