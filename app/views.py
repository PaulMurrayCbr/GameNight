from app import app
from flask import render_template, flash, redirect
from forms import NewCharacterForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/character/<name>')
def character(name):
    return "you are looking at the page for %r" % name

@app.route('/admin/')
def admin():
    return render_template('admin.html', title='Admin', 
               newpc_form = NewCharacterForm(),
               newbg_form = NewCharacterForm())

@app.route('/admin/newpc.do', methods=['POST'])
def do_newpc():
    flash(("New PC", 'success'))
    return redirect('/admin/')

@app.route('/admin/newbg.do', methods=['POST'])
def do_newbg():
    flash(("New BG",'success'))
    return redirect('/admin/')

