# LongestCommonSubstringWeb

## Windows Installation:
1. Python
- Install the latest version of Python 3 from the following link:
https://www.python.org/downloads/

1. Flask
- Using python's "pip" install the Flask web framework. Run the following command in the terminal: ```$ pip install Flask```

## Running Code
1. Start Server
- While in the same directory as the file ```lcs.py```. Run the following command in the terminal: ```$ python lcs.py```

2. Web Form
- Enter the following URL in your web browser to access the string form: http://localhost:5000/
- Add any number of strings with spaces in between in the form text box
- Click "Post" in order to see the result (You will automatically be redirected to the "/lcs" page)

3. HTTP Requests Only
- A web form alternative that will produce the same result
- In order to post directly to the api please enter the raw body in the following JSON format:
```
{
  "setOfStrings": [
    {"value": "comcast"},
    {"value": "caster"},
    {"value": "broadcaster"}
  ]
}
```
- *Must enter a key value pair with the key being 'setOfStrings' with a list as it's value. The list must be another key value pair, with the key being 'value' and its value as any single string.*
- *Possible resources to post: Python's Request Library, Postman Collabrative API, etc.*

4. Testing
- If you would like to test preset test cases run the ```test.py``` file while the server is running
- For modifications please edit the file named above