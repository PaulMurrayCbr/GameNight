from app import app, db
from flask import render_template, flash, redirect
import forms 
import models
import compute
from flask.globals import request

from sqlalchemy.orm.exc import  NoResultFound, MultipleResultsFound

def menugear() :
	return {
	    'pcs': models.Character.query.filter_by(pc=True),
	    'bgs': models.Character.query.filter_by(pc=False)
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
		if pc.pc:
			updatepc_form=forms.PC(obj=pc)
			
			add_unsourced_effect_form = forms.AddUnsourcedEffect()
		
			add_unsourced_effect_form.bonustype.choices= [ ('','untyped') ] + [
				(bt.name, bt.name) for bt in models.BonusType.query.all()
			]
		
			return render_template('pc.html', 
						updatepc_form=updatepc_form,
						add_unsourced_effect_form = add_unsourced_effect_form,
						pc=pc,
						stats = compute.compute_character(pc),
						menu=menugear())
		else:
			flash(('%s is not a PC' % name, 'danger'))
			
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
		
			pc.name = updatepc_form.name.data
			pc.pname = updatepc_form.pname.data
			db.session.commit()
		
		else:
			flash(('%s is not a PC' % name, 'danger'))
			
	except MultipleResultsFound, e:
		flash(('Found multiple characters named %s' % name, 'danger'))
	except NoResultFound, e:
		flash(('PC %s not found' % name, 'warning'))

	return redirect('/pc/%s/' % pc.name)

@app.route('/pc/<name>/add-unsourced-effect.do', methods=['POST'])
def pc_add_unsourced_effect(name):
	try:
		pc = models.Character.query.filter_by(name=name).one()
		if pc.pc:
			form = forms.AddUnsourcedEffect(request.form)

			effect = models.ActiveEffect()
			effect.characterid = pc.id
			effect.bonustype = form.bonustype.data
			effect.bonusto = form.bonusto.data
			effect.bonusamt = 2
			db.session.add(effect)			
			db.session.commit()
		
		else:
			flash(('%s is not a PC' % name, 'danger'))
			
	except MultipleResultsFound, e:
		flash(('Found multiple characters named %s' % name, 'danger'))
	except NoResultFound, e:
		flash(('PC %s not found' % name, 'warning'))
	return redirect('/pc/%s/' % pc.name)


@app.route('/admin/pc/')
def adminpc():
    pcs = models.Character.query.filter_by(pc=True)

    return render_template('/admin/pcs.html',
               pcs=pcs,
               newpc_form=forms.PC(),
               menu=menugear())

@app.route('/admin/pc/newpc.do', methods=['POST'])
def do_newpc():
    form = forms.PC(request.form)
    pc = models.Character(name=form.name.data, pname=form.pname.data, pc=True)
    db.session.add(pc)
    db.session.commit()
    
    flash(("New PC %s" % pc.name, 'success'))
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

@app.route('/admin/bg/')
def adminbg():
	bgs = models.Character.query.filter_by(pc=False)
	return render_template('/admin/bgs.html', 
               bgs=bgs,
               newbg_form=forms.BG(), 
               menu=menugear())

@app.route('/admin/bg/newbg.do', methods=['POST'])
def do_newbg():
    form = forms.BG(request.form)
    
    bg = models.Character(name=form.name.data, pc=False)
    db.session.add(bg)
    db.session.commit()

    flash(("New BG %s" % bg.name, 'success'))
    return redirect('/admin/bg/')

@app.route('/admin/bg/<id>/delete.do', methods=['GET'])
def do_deletebg(id):
    bg = models.Character.query.get(id)
    if not bg:
        flash(("BG %s not found" % id , 'danger'))
    elif bg.pc :
        flash(("'%s' is not a BG" % bg.name , 'danger'))
    else :
        db.session.delete(bg)
        db.session.commit()
        flash(("BG '%s' deleted" % bg.name , 'success'))
        
    return redirect('/admin/bg')

@app.route('/admin/bonuses/')
def bonuses():
	bts = [ {'id': bt.id, 'form': forms.BonusType(obj=bt) } for bt in models.BonusType.query.all() ]

	return render_template('/admin/bonuses.html',
			   bts=bts,
			   newbtype_form=forms.BonusType(),
			   menu=menugear())

@app.route('/admin/bonuses/new.do', methods=['POST'])
def do_new_bonus():
	form = forms.BonusType(request.form)
	
	bt = models.BonusType(name=form.name.data, stacking=form.stacking.data)
	db.session.add(bt)
	db.session.commit()

	flash(("New Bonus Type %s" % bt.name, 'success'))
	return redirect('/admin/bonuses/')

@app.route('/admin/bonuses/<name>/update.do', methods=['POST'])
def do_update_bonus(name):
	form = forms.BonusType(request.form)
	
	try:
		bt = models.BonusType.query.filter_by(name=name).one()
		bt.name = form.name.data
		bt.stacking = form.stacking.data
		db.session.commit()
		
		flash(("Bonus Type %s updated" % bt.name, 'success'))
	except MultipleResultsFound, e:
		flash(('Found multiple bonuses named %s' % name, 'danger'))
		pc = None
	except NoResultFound, e:
		flash(('Bonus type %s not found' % name, 'warning'))
		pc = None

	
	return redirect('/admin/bonuses/')

@app.route('/admin/bonuses/<id>/delete.do', methods=['GET'])
def do_delete_bonus(id):
	bt = models.BonusType.query.get(id)
	if not bt:
		flash(("Bonus Type %s not found" % id , 'danger'))
	else :
		db.session.delete(bt)
		db.session.commit()
		
		flash(("Bonus Type %s updated" % bt.name, 'success'))
	return redirect('/admin/bonuses/')
