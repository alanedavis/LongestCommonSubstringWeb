import requests

"""
Using the requests library send a 
get request to the servers POST page 
with the proper and improper JSON files
"""

try:
    r = requests.get(
        "http://localhost:5000/lcs",
        json= {"setOfStrings": []}
    )

    assert r.status_code == 404, "Status code should be 404"

    r = requests.get(
        "http://localhost:5000/lcs",
        json= {
        "setOfStrings": [
            {"value": "comcast"},
            {"value": "cast"},
            {"value": "broadcaster"}
        ]}
    )

    assert r.status_code == 200, "Status code should be 200"

    r = requests.get(
        "http://localhost:5000/lcs",
        json= {
        "setOfStrings": [
            {"value": "comcast"},
            {"value": "communicate"},
            {"value": "commutation"}
        ]}
    )

    assert r.status_code == 200, "Status code should be 200"

    r = requests.get(
        "http://localhost:5000/lcs",
        json= {
        "setOfStrings": [
            {"value": "comcast"},
            {"value": "comcast"},
            {"value": "commutation"}
        ]}
    )

    assert r.status_code == 406, "Status code should be 406"

    r = requests.get(
        "http://localhost:5000/lcs",
        json= {}
    )

    assert r.status_code == 404, "Status code should be 404"

    print("Passed All Tests")

except AssertionError:
    raise "Test Failed"