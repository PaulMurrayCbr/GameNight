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
    # if a buff has a null character id, then it's something that is a general buff
    # this supports conditions
    
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    description = db.Column(db.String(1023))
    duration_unit = db.Column(db.String(10))
    duration = db.Column(db.Integer)

    def __repr__(self):
        return '<Buff#%d %r>' % self.id, self.name
    
