from flask import *
from flask_pymongo import PyMongo
from flask_moment import Moment

# creating the web application controller using Flask
app = Flask('ToDoList')
app.config[
    'MONGO_URI'] = 'mongodb+srv://dbuser:$wqKG8Q.Axiqk8M@mycluster.rvhdw.mongodb.net/ToDoListDatabase?retryWrites=true&w=majority'
app.config['SECRET_KEY'] = 'dinosaur'
# creates the controller for MongoDB using PyMongo
mongo = PyMongo(app)

moment = Moment(app)


@app.route('/')
def home():
    return redirect('/To-Do-List')


@app.route('/To-Do-List', methods=['GET', 'POST'])
def todo():
    if request.method == 'GET':
        notes = mongo.db.notes.find({})
        return render_template('To-Do-List.html', notes=notes)
    elif request.method == 'POST':
        note = request.form.to_dict()
        mongo.db.notes.insert_one(note)
        return redirect('/To-Do-List')



if __name__ == '__main__':
    app.run(debug=True)
