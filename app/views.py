from app import app
from flask.templating import render_template
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
    return 'new pc'

@app.route('/admin/newbg.do', methods=['POST'])
def do_newbg():
    return 'new bg'

