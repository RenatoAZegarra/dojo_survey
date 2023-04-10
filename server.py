from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/process', methods=['POST'])
# def process():
#     name = request.form["name"]
#     location = request.form["location"]
#     language = request.form["language"]
#     comments = request.form["comments"]
#     return redirect('/result')


@app.route('/result', methods=['GET', 'POST'])
def result():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comments = request.form["comments"]
    computers = request.form.getlist('computers[]')
    return render_template('result.html', name = name, location = location, language = language, comments = comments, computers = computers)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.