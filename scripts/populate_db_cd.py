import uuid

from bull import app
app.config['STRIPE_SECRET_KEY'] = None
from bull.models import Product, Purchase, db

cd1 = Product(
    id=3,
    name='Weights & Pulleys CD',
    file_name='weights and pulleys cd.mp3',
    version='1.5',
    is_active=True,
    price=10.00)


with app.app_context():
    session = db.session()
    db.metadata.create_all(db.engine)
    session.add(cd1)
    session.commit()