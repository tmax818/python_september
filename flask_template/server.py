
from flask import Flask, render_template, redirect, request
# import the class from friend.py
from thing import Thing

app = Flask(__name__)

# ! CREATE

@app.route("/")
def index():
    
    # call the get all classmethod to get all friends
    return render_template("index.html", things = Thing.get_all())

@app.route('/handle_new_thing', methods=['POST'])
def handle_new_thing():
    print(request.form)
    Thing.save(request.form)
    return redirect('/')

@app.route('/thing/<int:id>')
def show(id):
    data = {'id': id}
    return render_template('show.html', thing=Thing.get_one(data))


# ! READ/RETRIEVE


            
if __name__ == "__main__":
    app.run(debug=True)