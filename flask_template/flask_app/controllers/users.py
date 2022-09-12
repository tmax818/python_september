from flask_app import app, render_template, request, redirect
from flask_app.models.user import User

# ! CREATE

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    return render_template("index.html")

@app.route('/register/user', methods=['POST'])
def register():
    print(request.form)
    if not User.validate_user(request.form):
        return redirect('/')     
    User.save(request.form)
    return redirect('/things')