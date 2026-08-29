import flask from Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def season():
    result = None 
    season = request.form['season']

    if request.method == "POST":
        season = request.form["season"]
        if season == "spring":
        result = 'spring'
        
        elif season == "summer":
        result = 'summer'
        
        elif season == "fall":
        result = 'fall'
        
        elif season == "winter":
        result = 'winter'
       
        
        else:
        result = invalid 
    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)