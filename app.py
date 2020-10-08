import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://rooot:ovJpdy6ZxuMmEtWB@myfirstcluster.jwwdc.mongodb.net/task_manager?retryWrites=true&w=majority'
app.secret_key = '@v3rts3cr3tk3y'


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    tasks = mongo.db.tasks.find()
    return render_template("tasks.html", tasks=tasks)


@app.route('/add_task')
def add_task():
    return render_template('addtask.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)


# if __name__ == '__main__':
#     app.run(host=os.environ.get('IP'),
#             port=int(os.environ.get('PORT')),
#             debug=True)
