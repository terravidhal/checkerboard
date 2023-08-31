from flask import Flask ,render_template , redirect # added redirect!
app = Flask(__name__)    

@app.route('/')
def checkerboard_home():
    return redirect("/8*8")

@app.route('/8*8')
def checkerboard_8_8():
    return render_template('index.html', num_cases = 8, num_lines = 8, color0 = "red", color1 ="black")

@app.route('/<int:x>')
def checkerboard_x_8(x):
    return render_template('index.html', num_cases = x, num_lines = 3, color0 = "red", color1 ="black")

# BONUS NINJA
@app.route('/<int:x>/<int:y>')
def checkerboard_x_y(x, y):
    return render_template('index.html', num_cases = x, num_lines = y, color0 = "red", color1 ="black")

# BONUS SENSEI
@app.route('/<int:x>/<int:y>/<string:bg0>/<string:bg1>')
def checkerboard_x_y_bg0_bg1(x, y, bg0, bg1):
    return render_template('index.html', num_cases = x, num_lines = y, color0 = bg0, color1 = bg1)

@app.errorhandler(404) # we specify in parameter here the type of error, here it is 404
def page_not_found(error): # (error) is important because it recovers the instance of the error that was thrown
    return f"<h2 style='text-align:center;padding-top:40px'>Sorry! No response. Try again</h2>"


if __name__=="__main__":   
    app.run(debug=True)    