from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# HTML模板
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Gender Prediction</title>
</head>
<body>
    <h2>Gender Prediction</h2>
    <form method="post">
        First Name: <input type="text" name="name">
        <input type="submit" value="Predict Gender">
    </form>
    {% if gender %}
        <p>Gender: {{ gender }}</p>
        <p>Possibility: {{ probability }}</p>
    {% endif %}
</body>
</html>
'''

def get_gender(name):
    """
    根据姓名预测性别
    """
    url = "https://api.genderize.io/?name=" + name
    response = requests.get(url)
    data = response.json()
    return data.get("gender"), data.get("probability")

@app.route('/', methods=['GET', 'POST'])
def predict_gender():
    gender = None
    probability = None
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            gender, probability = get_gender(name)
    return render_template_string(HTML_TEMPLATE, gender=gender, probability=probability)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

