import requests

try:
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

except AssertionError:
    raise "Test Failed"

print("Passed All Tests")