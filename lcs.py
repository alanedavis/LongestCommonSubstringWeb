from flask import Flask, request, render_template, Response

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/lcs', methods=['POST', 'GET'])
def lcs():
    # If the POST body is empty send the proper HTTP response
    if not request.form.get("setOfStrings") and (not request.json or not request.json['setOfStrings']):
        return Response("{'Status': 'empty'}", status=404)

    # HTML form is a POST request
    #   split the string with a blankspace delimeter
    if request.method == 'POST':
        json = request.form['setOfStrings'].split(" ")

    # GET Request
    #   Grab the values from the nested key value pair
    elif request.method == 'GET':
        json = [i['value'] for i in request.json['setOfStrings']]

    # If not all strings are unique send the proper HTTP response
    if not isSet(json):
        return Response("{'Status'} : 'Not A Set'", status=406)

    # Find the longest common substring
    subStr = subStrLcs(json)

    # Create properly formatted JSON
    resDict = {
        "lcs" : [
            {"values" : subStr}
        ]
    }

    return resDict

def subStrLcs(data):
    """
    :param data: list of strings
    :return: string
    """
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]

    return substr

def isSet(data):
    """
    :param data: list of strings
    :return: Boolean
    """
    return len(set(data)) == len(data)

if __name__ == '__main__':
    app.run()