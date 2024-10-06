from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Hero, Power, HeroPower
import os

# Determine the base directory and set up the database URI
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE  # Set the database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications
app.json.compact = False  # Pretty-print JSON responses

# Set up database migration and API
migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

# Home route
@app.route('/')
def index():
    return '<h1>Code challenge</h1>'

# Resource to handle operations related to heroes
class Heroes(Resource):
    def get(self):
        # Retrieve all heroes from the database
        heroes = Hero.query.all()
        # Return a JSON response with hero details
        return jsonify([{
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        } for hero in heroes])

# Resource to handle fetching a hero by their ID
class HeroById(Resource):
    def get(self, id):
        # Retrieve a specific hero by ID
        hero = Hero.query.get(id)
        if hero:
            # Return hero details and associated powers
            return jsonify({
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name,
                "hero_powers": [{
                    "hero_id": hp.hero_id,
                    "id": hp.id,
                    "strength": hp.strength,
                    "power": {
                        "description": hp.power.description,
                        "id": hp.power.id,
                        "name": hp.power.name
                    }
                } for hp in hero.hero_powers]
            })
        return {"error": "Hero not found"}, 404  # Return error if hero not found

# Resource to handle operations related to powers
class Powers(Resource):
    def get(self):
        # Retrieve all powers from the database
        powers = Power.query.all()
        # Return a JSON response with power details
        return jsonify([power.to_dict() for power in powers])

# Resource to handle fetching a power by its ID
class PowerById(Resource):
    def get(self, id):
        # Retrieve a specific power by ID
        power = Power.query.get(id)
        if power:
            # Return power details
            return jsonify(power.to_dict())
        return {"error": "Power not found"}, 404  # Return error if power not found

    def patch(self, id):
        # Update a specific power's details
        power = Power.query.get(id)
        if not power:
            return {"error": "Power not found"}, 404  # Return error if power not found

        data = request.get_json()
        # Validation to ensure new description meets the length requirement
        if 'description' in data and (len(data['description']) < 20):
            return {"errors": ["Description must be at least 20 characters long"]}, 400
        
        try:
            # Update power attributes based on the provided data
            for attr in data:
                setattr(power, attr, data[attr])
            db.session.commit()  # Commit the changes to the database
            return jsonify(power.to_dict())  # Return updated power details
        except ValueError as e:
            return {"errors": [str(e)]}, 400  # Return error if there was an issue

# Resource to handle creating relationships between heroes and powers
class HeroPowers(Resource):
    def post(self):
        # Add a new hero-power relationship
        data = request.get_json()

        # Check if the specified hero and power exist
        hero = Hero.query.get(data['hero_id'])
        power = Power.query.get(data['power_id'])
        if not hero or not power:
            return {"errors": ["Hero or Power not found"]}, 404  # Return error if not found

        try:
            # Create a new HeroPower relationship
            hero_power = HeroPower(
                strength=data['strength'],
                hero_id=data['hero_id'],
                power_id=data['power_id']
            )
            db.session.add(hero_power)  # Add the relationship to the session
            db.session.commit()  # Commit the changes to the database
            # Return details of the newly created hero-power relationship
            return jsonify({
                "id": hero_power.id,
                "hero_id": hero_power.hero_id,
                "power_id": hero_power.power_id,
                "strength": hero_power.strength,
                "hero": {
                    "id": hero.id,
                    "name": hero.name,
                    "super_name": hero.super_name
                },
                "power": {
                    "description": power.description,
                    "id": power.id,
                    "name": power.name
                }
            }), 201
        except ValueError as e:
            return {"errors": [str(e)]}, 400  # Return error if there was an issue

# Set up API resource routing
api.add_resource(Heroes, '/heroes')
api.add_resource(HeroById, '/heroes/<int:id>')
api.add_resource(Powers, '/powers')
api.add_resource(PowerById, '/powers/<int:id>')
api.add_resource(HeroPowers, '/hero_powers')

# Run the application
if __name__ == '__main__':
    app.run(port=5555, debug=True)
