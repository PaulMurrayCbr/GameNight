from app import db

# no indexes yet

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    pname = db.Column(db.String(64))
    pc = db.Column(db.Boolean)

    def __repr__(self):
        return '<%r (%r)>' % (self.name), (self.pname)

class ActiveEffect(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    characterid = db.Column(db.Integer)
    sourceid = db.Column(db.Integer)
    bonustype = db.Column(db.String(64))
    bonusto = db.Column(db.String(64))   # ac, to-hit, saves
    bonusamt = db.Column(db.Integer)

    def __repr__(self):
        return '<ActiveEffect %r>' % (self.id)
    
# yeah, I'm going to need this.
class BonusType(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique=True)
    stacking = db.Column(db.Boolean)
    
