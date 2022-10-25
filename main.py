from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/meet_team')
def meet_team():
    return render_template('meet-team.html')

@app.route('/get_involved')
def get_involved():
    return render_template('get-involved.html')

@app.route('/further_work')
def further_work():
    return render_template('further-work.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)