from main import app, db
from models import Product

app.app_context().push()

db.create_all()

product1 = Product(
    product_name="wheel",
    product_catalog="322535235235",
    product_description="Wheel that spins",
    product_price='55'
)
product2 = Product(
    product_name="breaks",
    product_catalog="415138454345",
    product_description="breaking breaks",
    product_price="1124"
)
db.session.add(product1)
db.session.add(product2)
db.session.commit()