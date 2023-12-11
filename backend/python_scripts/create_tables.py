from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://habib:ilovecheese@localhost/bistra_db'
db = SQLAlchemy(app)
fake = Faker()


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    country = db.relationship('Country', backref='states')

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'), nullable=False)
    state = db.relationship('State', backref='cities')

class Commune(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    city = db.relationship('City', backref='communes')

class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

class Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    commune_id = db.Column(db.Integer, db.ForeignKey('commune.id'), nullable=False)
    commune = db.relationship('Commune', backref='providers')

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=False)
    provider = db.relationship('Provider', backref='products')

with app.app_context():
    db.create_all()
    db.session.commit()

def generate_fake_data():
    with app.app_context():
        for _ in range(2):
            country = Country(name=fake.country())
            db.session.add(country)
            db.session.commit()

            for _ in range(2):
                state = State(name=fake.state(), country=country)
                db.session.add(state)
                db.session.commit()

                for _ in range(5):
                    city = City(name=fake.city(), state=state)
                    db.session.add(city)
                    db.session.commit()

                    for _ in range(6):
                        commune = Commune(name=fake.word(), city=city)
                        db.session.add(commune)
                        db.session.commit()

                        for _ in range(5):
                            provider = Provider(
                                name=fake.company(),
                                email=fake.unique.email(),  
                                phone=fake.phone_number()[:15],
                                commune=commune
                            )
                            db.session.add(provider)
                            db.session.commit()

                            for _ in range(20):
                                product = Product(
                                    name=fake.word(),
                                    price=fake.random_int(10, 100),
                                    provider=provider
                                )
                                db.session.add(product)
                                db.session.commit()

                for _ in range(6):
                    warehouse = Warehouse(
                        location=fake.word(),
                        capacity=fake.random_int(100, 500)
                    )
                    db.session.add(warehouse)
                    db.session.commit()

if __name__ == '__main__':
    generate_fake_data()
    print("Fake data generated successfully.")
