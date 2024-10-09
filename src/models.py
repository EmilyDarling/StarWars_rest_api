from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

    

class User(db.Model):
    __tablename__ = 'user'   
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(250), nullable=False)
    password= db.Column(db.String(250), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            # do not serialize the password, its a security breach
        }



class Character(db.Model):
      
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(250), nullable=False)
    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender" : self.username,
            "eye_color" : self.gender,
            "hair_color" : self.hair_color,
            "height" : self.height,
            "skin_color" : self.skin_color,
            "mass" : self.mass,
            # do not serialize the password, its a security breach
        }
    

class Planet(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    rotation_period = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(250), nullable=False)
     
    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "user_id" : self.user_id,
            "name": self.name,
            "climate" : self.climate,
            "population" : self.population,
            "gravity" : self.gravity,
            "rotation_period" : self.rotation_period,
            "terrain" : self.terrain,
            "mass" : self.mass,
            # do not serialize the password, its a security breach
        }
    


class Favorite(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(250), nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    person = db.relationship(User)
    character_id = db.Column(db.Integer, db.ForeignKey(Character.id))
    character = db.relationship(Character)
    planet_id = db.Column(db.Integer, db.ForeignKey(Planet.id))
    planet = db.relationship(Planet)
    
    def __repr__(self):
        return '<Favorite %r>' % self.favorite

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "user": self.user,
            "character": self.character,
            "planet": self.planet
            # do not serialize the password, its a security breach
        }