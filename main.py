from flask import Flask, render_template,send_from_directory
app=Flask(__name__) # name of current directory

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route('/download')
def download():
    return send_from_directory('static',path='files/resume.pdf')
if __name__=="__main__":
    app.run(debug=True)