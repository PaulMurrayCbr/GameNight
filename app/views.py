from app import app, db
from flask import render_template, flash, redirect
import forms 
import models
from flask.globals import request

from sqlalchemy.orm.exc import  NoResultFound, MultipleResultsFound

def menugear() :
	return {
	    'pcs': models.Character.query.all()
	}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', menu=menugear())

@app.route('/whiteboard')
def whiteboard():
    return render_template('whiteboard.html', menu=menugear())
   
@app.route('/pc/<name>/')
def character(name):
	try:
		pc = models.Character.query.filter_by(name=name).one()
		updatepc_form=forms.PC(obj=pc)
	
		return render_template('pc.html', 
					updatepc_form=updatepc_form,
					pc=pc,
					menu=menugear())
			
	except MultipleResultsFound, e:
		flash(('Found multiple characters named %s' % name, 'danger'))
		pc = None
	except NoResultFound, e:
		flash(('PC %s not found' % name, 'warning'))
		pc = None

	return redirect('/')


@app.route('/pc/<name>/update.do', methods=['POST'])
def do_updatepc(name):
	try:
		pc = models.Character.query.filter_by(name=name).one()
		if pc.pc:
			updatepc_form=forms.PC(obj=pc)
		
			pc.abbrev = updatepc_form.abbrev.data
			pc.name = updatepc_form.name.data
			pc.pname = updatepc_form.pname.data
			db.session.commit()
		
			return redirect('/pc/%s' % pc.name)
		else:
			flash(('%s is not a PC' % name, 'danger'))
			
	except MultipleResultsFound, e:
		flash(('Found multiple characters named %s' % name, 'danger'))
		pc = None
	except NoResultFound, e:
		flash(('PC %s not found' % name, 'warning'))
		pc = None

@app.route('/admin/pc/')
def adminpc():
    pcs = models.Character.query.all()

    return render_template('/admin/pcs.html',
               pcs=pcs,
               newpc_form=forms.PC(),
               menu=menugear())

@app.route('/admin/pc/newpc.do', methods=['POST'])
def do_newpc():
    form = forms.PC(request.form)
    pc = models.Character(name=form.name.data, pname=form.pname.data, abbrev=form.abbrev.data)
    db.session.add(pc)
    db.session.commit()
    
    flash(("New PC", 'success'))
    return redirect('/admin/pc/')

@app.route('/admin/pc/<id>/delete.do', methods=['GET'])
def do_deletepc(id):
    pc = models.Character.query.get(id)
    if not pc:
        flash(("PC %s not found" % id , 'danger'))
    elif not pc.pc :
        flash(("'%s' is not a PC" % pc.name , 'danger'))
    else :
        db.session.delete(pc)
        db.session.commit()
        flash(("PC '%s' deleted" % pc.name , 'success'))
        
    return redirect('/admin/pc/')

