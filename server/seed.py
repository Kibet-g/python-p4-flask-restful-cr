#!/usr/bin/env python3

from faker import Faker

from app import app
from models import db, Newsletter

fake = Faker()

with app.app_context():
    # Clear existing data
    Newsletter.query.delete()

    # Create seed data
    newsletters = []
    for _ in range(50):
        newsletter = Newsletter(
            title=fake.text(max_nb_chars=20),
            body=fake.paragraph(nb_sentences=5),
        )
        newsletters.append(newsletter)

    # Add and commit data
    db.session.add_all(newsletters)
    db.session.commit()

    print("Database seeded with fake newsletters!")
