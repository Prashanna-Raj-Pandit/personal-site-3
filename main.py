from flask import Flask, render_template
app=Flask(__name__) # name of current directory

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

if __name__=="__main__":
    app.run(debug=True)