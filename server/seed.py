from random import choice as rc

from app import app
from models import db, Hero, Power, HeroPower

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        Power.query.delete()
        Hero.query.delete()
        HeroPower.query.delete()

        print("Seeding powers...")
        powers = [
    Power(name="super strength", description="gives the wielder super-human strengths"),
    Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
    Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
    Power(name="elasticity", description="can stretch the human body to extreme lengths"),
    Power(name="invisibility", description="allows the wielder to become unseen"),
    Power(name="telekinesis", description="enables the manipulation of objects with the mind"),
    Power(name="time manipulation", description="grants the ability to slow down or speed up time"),
    Power(name="teleportation", description="allows instant movement from one place to another"),
    Power(name="super speed", description="enables the wielder to move at incredible speeds"),
    Power(name="regeneration", description="allows for rapid healing from injuries"),
    Power(name="force field creation", description="can create protective barriers"),
    Power(name="weather control", description="grants the ability to influence weather patterns"),
    Power(name="fire manipulation", description="allows the wielder to control and generate fire"),
    Power(name="earth manipulation", description="enables the control over earth and stone"),
    Power(name="water manipulation", description="allows the control of water in all its forms"),
    Power(name="mind reading", description="grants the ability to read thoughts"),
    Power(name="shape-shifting", description="allows the wielder to change their appearance at will"),
    Power(name="light manipulation", description="can bend light to create illusions"),
    Power(name="sound manipulation", description="grants the ability to control sound waves"),
    Power(name="animal communication", description="allows communication with animals"),
    Power(name="plant manipulation", description="can control and grow plants rapidly"),
    Power(name="x-ray vision", description="grants the ability to see through solid objects"),
    Power(name="night vision", description="enables the ability to see in darkness"),
    Power(name="super intelligence", description="gives enhanced cognitive abilities"),
    Power(name="gravity control", description="can manipulate gravitational forces"),
    Power(name="energy absorption", description="allows the absorption of energy from surroundings"),
    Power(name="shadow manipulation", description="enables control over shadows"),
    Power(name="memory manipulation", description="grants the ability to alter memories"),
    Power(name="duplicate creation", description="can create duplicates of oneself"),
    Power(name="enhanced agility", description="grants extraordinary agility and reflexes"),
    Power(name="elemental control", description="can control elements like fire, water, earth, and air"),
]

        db.session.add_all(powers)

        print("Seeding heroes...")
        heroes = [
    Hero(name="Kamala Khan", super_name="Ms. Marvel"),
    Hero(name="Doreen Green", super_name="Squirrel Girl"),
    Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
    Hero(name="Janet Van Dyne", super_name="The Wasp"),
    Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
    Hero(name="Carol Danvers", super_name="Captain Marvel"),
    Hero(name="Jean Grey", super_name="Dark Phoenix"),
    Hero(name="Ororo Munroe", super_name="Storm"),
    Hero(name="Kitty Pryde", super_name="Shadowcat"),
    Hero(name="Elektra Natchios", super_name="Elektra"),
    Hero(name="Bruce Banner", super_name="Hulk"),
    Hero(name="Peter Parker", super_name="Spider-Man"),
    Hero(name="Natasha Romanoff", super_name="Black Widow"),
    Hero(name="Stephen Strange", super_name="Doctor Strange"),
    Hero(name="Tony Stark", super_name="Iron Man"),
    Hero(name="Thor Odinson", super_name="Thor"),
    Hero(name="Steve Rogers", super_name="Captain America"),
    Hero(name="Clint Barton", super_name="Hawkeye"),
    Hero(name="Matt Murdock", super_name="Daredevil"),
    Hero(name="Jessica Jones", super_name="Jessica Jones"),
    Hero(name="Luke Cage", super_name="Power Man"),
    Hero(name="Frank Castle", super_name="The Punisher"),
    Hero(name="Groot", super_name="Groot"),
    Hero(name="Rocket Raccoon", super_name="Rocket"),
    Hero(name="Gamora", super_name="Gamora"),
    Hero(name="Star-Lord", super_name="Star-Lord"),
    Hero(name="Vision", super_name="Vision"),
    Hero(name="Scarlet Spider", super_name="Scarlet Spider"),
    Hero(name="Black Panther", super_name="Black Panther"),
    Hero(name="Shuri", super_name="Shuri"),
    Hero(name="Miles Morales", super_name="Spider-Man"),
    Hero(name="Betsy Braddock", super_name="Psylocke"),
]
        db.session.add_all(heroes)

        print("Adding powers to heroes...")
        strengths = ["Strong", "Weak", "Average"]
        hero_powers = []
        for hero in heroes:
            power = rc(powers)
            hero_powers.append(
                HeroPower(hero=hero, power=power, strength=rc(strengths))
            )
        db.session.add_all(hero_powers)
        db.session.commit()

        print("Done seeding!")
