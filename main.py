from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
  'Job Title': "Data Engineer",
  'Location': "Templeton",
  'Salary': 90000
}, {
  'Job Title': "Data Scientist",
  'Location': "Paso Robles",
  'Salary': 120000
}, {
  'Job Title': "Data Analyst",
  'Location': "Atascadero",
  'Salary': 80000
}]


@app.route('/')
def hello_world():
  return render_template('home.html', job=jobs)


@app.route('/resources')
def hello_world_resources():
  return render_template('resources.html', job=jobs)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)


#app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
