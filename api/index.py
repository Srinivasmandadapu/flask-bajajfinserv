from flask import Flask, jsonify, request
import json
import base64
import mimetypes
app = Flask(_name_)


@app.route('/bfhl', methods=['GET'])
def get_function():
    return jsonify({
        'operation_code': 1
    }), 200


@app.route('/bfhl', methods=['POST'])
def post_function():
    request_body = request.get_json()
    data = request_body['data']
    file_b64 = request_body['file_b64']
    numbers = []
    alphabets = []
    highest_lowercase = None

    for item in data:
        # Check if the item is numeric and add it to the numbers list
        if item.isdigit():
            numbers.append(item)
        # Check if the item is an alphabetic character and add it to the alphabets list
        elif item.isalpha():
            alphabets.append(item)
            # Check if the item is lowercase and update highest_lowercase
            if item.islower():
                if highest_lowercase is None or item > highest_lowercase:
                    highest_lowercase = item
    file_valid = True
    try:
        file_data = base64.b64decode(file_b64)
    except:
        file_valid = False
        return jsonify({
            "is_success": True,
            "user_id": "SrinivasMandadapu_27052004",
            "email": "srinivas_mandadapu@srmap.edu.in",
            "roll_number": "AP21110010180",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lower_case_alphabet": [highest_lowercase] if highest_lowercase else [],
            "file_valid": file_valid
        })
    file_size_kb = len(file_data)
    file_mime_type = mimetypes.guess_type("file")[0]

    return jsonify({
        "is_success": True,
        "user_id": "SrinivasMandadapu_27052004",
        "email": "srinivas_mandadapu@srmap.edu.in",
        "roll_number": "AP21110010180",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lower_case_alphabet": [highest_lowercase] if highest_lowercase else [],
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": file_size_kb
    })
