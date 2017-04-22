from app import db

# no indexes yet

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    abbrev = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(20), unique=True)
    pname = db.Column(db.String(20))

    def __repr__(self):
        return '<%r (%r)>' % self.name, self.pname
    
class Buff(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    character_id = db.Column(db.Integer, db.ForeignKey('Character.id'))
    description = db.Column(db.String(1023))
    duration_unit = db.Column(db.String(10))
    duration = db.Column(db.Integer)
    current_duration = db.Column(db.Integer)
    supressed = db.Column(db.Boolean())

    def __repr__(self):
        return '<Buff#%d %r>' % self.id, self.name
    
class BuffOn(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    character_id = db.Column(db.Integer, db.ForeignKey('Character.id'))
    buff_id = db.Column(db.Integer, db.ForeignKey('Buff.id'))
    supressed = db.Column(db.Boolean())
    notes = db.Column(db.String(1023))
    