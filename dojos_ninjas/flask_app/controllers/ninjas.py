from flask_app import app, render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
 

# ! CREATE

@app.route("/ninjas")
def ninjas():
    # call the get all classmethod to get all friends
    return render_template("new_ninja.html", dojos = Dojo.get_all())

@app.route('/handle_new_ninja', methods=['POST'])
def handle_new_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect(f"/dojo/{request.form['dojo_id']}")

# ! READ ONE

@app.route('/ninja/<int:id>')
def show_ninja(id):
    data = {'id': id}
    return render_template('show.html', ninja=Ninja.get_one(data))


# ! READ/RETRIEVE ALL

@app.route('/bob')
def bob():
    return render_template('ninjas.html', ninjas = Ninja.get_all())

# ! UPDATE

@app.route('/edit/<int:id>')
def edit_ninja(id):
    data = {'id': id}
    return render_template('edit_ninja.html', ninja = Ninja.get_one(data))

@app.route('/update/ninja', methods = ['POST'])
def update_ninja():
    print(request.form)
    Ninja.update(request.form)
    return redirect('/ninjas')

# ! DELETE

@app.route('/delete/<int:id>')
def delete_ninja(id):
    data = {'id': id}
    Ninja.destroy(data)
    return redirect('/ninjas')