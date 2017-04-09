from app import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    pname = db.Column(db.String(64))
    pc = db.Column(db.Boolean)

    def __repr__(self):
        return '<%r (%r)>' % (self.name), (self.pname)
    
class Buff(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    name = db.Column(db.String(64))
    duration_unit = db.Column(db.String(64))
    duration = db.Column(db.Integer)

    def __repr__(self):
        return '<Buff %r>' % (self.name)
    
class Effect(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    buff_id = db.Column(db.Integer, db.ForeignKey('buff.id'))
    type = db.Column(db.String(64))     # morale, sacred, etc
    target = db.Column(db.String(64))   # ac, to-hit, saves
    bounus = db.Column(db.Integer)      # + whatever
    ablative = db.Column(db.Boolean)

    def __repr__(self):
        return '<Buff %r>' % (self.name)
    
class Casting(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    buff_id = db.Column(db.Integer, db.ForeignKey('buff.id'))
    duration_remaining = db.Column(db.Integer)
    bounus = db.Column(db.Integer)      # used when its rolled when you cast it
    
class CastOn(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    casting_id = db.Column(db.Integer, db.ForeignKey('casting.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    enabled = db.Column(db.Boolean)

class CastEffect(db.Model): # only neded when an effect is ablative
    id = db.Column(db.Integer, primary_key = True)
    caston_id = db.Column(db.Integer, db.ForeignKey('cast_on.id'))
    effect_id = db.Column(db.Integer, db.ForeignKey('effect.id'))
    ablative_remaining = db.Column(db.Integer)
    
