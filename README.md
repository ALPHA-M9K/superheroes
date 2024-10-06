#  Project Name
SUPERHEROES API

## Overview
The Superheroes API is a Flask-based web application that allows users to manage and retrieve information about superheroes, their superpowers, and the relationships between them. This project provides a RESTful API for tracking heroes and their superpowers.

## Project Structure
- `server/app.py`: The main Flask application file containing route definitions and API logic.
- `server/models.py`: Defines the data models for `Hero`, `Power`, and `HeroPower`, including their relationships and validations.
- `server/seed.py`: Script to populate the database with initial data for testing.

## Features
- Retrieve a list of all heroes
- Get detailed information about a specific hero, including their superpowers
- Retrieve a list of all superpowers
- Get detailed information about a specific superpower
- Update superpower descriptions
- Create new associations between heroes and powers (HeroPower)
- Data validations for power descriptions and hero power strengths

## Installation

### Setup
1. Ensure you have Python and pipenv installed on your system.
2. Clone the repository and navigate to the project directory.
3. Set up the virtual environment and install dependencies:
   
   pipenv install
   pipenv shell
   
4. Set up the database:
   
   export FLASK_APP=server/app.py
   flask db init
   flask db upgrade head
   python server/seed.py
   

## Running the Application
Start the Flask backend:

python server/app.py



## API Endpoints
- `GET /heroes`: Retrieve a list of all heroes
- `GET /heroes/:id`: Get detailed information about a specific hero
- `GET /powers`: Retrieve a list of all superpowers
- `GET /powers/:id`: Get detailed information about a specific superpower
- `PATCH /powers/:id`: Update a superpower's description
- `POST /hero_powers`: Create a new HeroPower association

## Data Models
- `Hero`: Represents a superhero with attributes like name and super name.
- `Power`: Represents a superpower with a name and description.
- `HeroPower`: Represents the association between a hero and a power, including the strength of the power for that hero.


## Future Enhancements
- Implement user authentication and authorization
- Add more complex querying capabilities (e.g., finding heroes by power type)
- Incorporate a rating system for heroes and powers
- Develop a frontend interface for easier interaction with the API

## Contributing
Contributions to the Superheroes API project are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License.