from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates_todo')

todos = [{"Task": "This is first task", "done": False}, {"Task": "This is Second task", "done": True}]

@app.route('/')
def index():
    return render_template('todo.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    todos.append({'Task': todo, 'done': False})
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['Task'] = request.form['todo']
        return redirect(url_for('index'))
    else:
        print(index)
        return render_template('edit_todo.html', todo=todo, index=index)

@app.route('/check/<int:index>')
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)