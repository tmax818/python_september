from flask_app import app, render_template, request, redirect
from flask_app.models.dojo import Dojo

# ! CREATE

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    return render_template("index.html", dojos = Dojo.get_all())

@app.route('/handle_new_dojo', methods=['POST'])
def handle_new_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/')

# ! READ ONE

@app.route('/dojo/<int:id>')
def show(id):
    data = {'id': id}
    return render_template('show.html', dojo=Dojo.get_one(data))


# ! READ/RETRIEVE ALL

@app.route('/dojos')
def dojos():
    return render_template('dojos.html', dojos = Dojo.get_all())

# ! UPDATE

@app.route('/edit/<int:id>')
def edit_dojo(id):
    data = {'id': id}
    return render_template('edit_dojo.html', dojo = Dojo.get_one(data))

@app.route('/update/dojo', methods = ['POST'])
def update_dojo():
    print(request.form)
    Dojo.update(request.form)
    return redirect('/dojos')

# ! DELETE

@app.route('/delete/<int:id>')
def delete_dojo(id):
    data = {'id': id}
    Dojo.destroy(data)
    return redirect('/dojos')