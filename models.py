from app import db
from app import ma

class Test(db.Model):
    """Data model for testing SQLAlchemy."""

    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __repr__(self):
        return '<Test {}>'.format(self.name)

class TestSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")

test_schema = TestSchema()
tests_schema = TestSchema(many=True)

class Stock(db.Model):
    """Data model for stocks."""

    __tablename__ = 'stock'
    id = db.Column(db.Integer, primary_key=True)
    equity = db.Column(db.String())
    info = db.Column(db.JSON)
    history = db.Column(db.JSON)
    history_alpha = db.Column(db.JSON)

    def __repr__(self):
        return f'<Stock equity: {self.id} equity: {self.equity}>'

class StockSchema(ma.Schema):
    class Meta:
        fields = ("id", "info", "history", "history_alpha")

stock_schema = StockSchema()
stocks_schema = StockSchema(many=True)