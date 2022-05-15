from flask import Flask, request, jsonify
import BodyPerformance


app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def api_predict_request():
    if request.method == 'POST':
        params = {"age": request.json['age'], "gender": request.json['gender'], "height_cm": request.json['height_cm'],
                  "weight_kg": request.json['weight_kg'], "bodyfat": request.json['bodyfat'],
                  "diastolic": request.json['diastolic'], "systolic": request.json['systolic'],
                  "gripForce": request.json['gripForce'],"sit_and_bend" : request.json['sit_and_bendforward_cm'],
                  "sit_ups" : request.json['sit_ups_count'],"broad_jump_cm" : request.json['broad_jump_cm']}
        obj = BodyPerformance.BodyPerformace(params)
        grade = obj.predict()
        print(grade)
        result = 'all received successfully!'
        return jsonify(result)


if __name__ == '__main__':
    app.run()