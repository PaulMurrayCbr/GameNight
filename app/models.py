from app import db

# no indexes yet

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    abbrev = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(20), unique=True)
    pname = db.Column(db.String(20))

    def __repr__(self):
        return '<%r (%r)>' % self.name, self.pname

class Hp(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    source = db.Column(db.String(20)) # base, temp, stoneskin, con bonus, neg levels, prot acid, damage, nonlethal
    max = db.Column(db.Integer)
    current = db.Column(db.Integer)
    ablative_only = db.Column(db.Boolean)
    
class Buff(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    description = db.Column(db.String(1023))
    duration_unit = db.Column(db.String(10))
    duration = db.Column(db.Integer)
    current_duration = db.Column(db.Integer)
    supressed = db.Column(db.Boolean())

    def __repr__(self):
        return '<Buff#%d %r>' % self.id, self.name
    
class BuffOn(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    buff_id = db.Column(db.Integer, db.ForeignKey('buff.id'))
    supressed = db.Column(db.Boolean())
    notes = db.Column(db.String(1023))
    