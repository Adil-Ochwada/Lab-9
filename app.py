from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# App and database setup
app = Flask('Computer Expenses')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///components.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database model
class Component(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hardware_part = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.hardware_part} - {self.price}'

# Main page
@app.route('/')
def index():
    components = Component.query.all()
    total_sum = sum(c.price for c in components)
    return render_template('index.html', components=components, total=total_sum)

# Add a new component
@app.route('/add', methods=['POST'])
def add_component():
    data = request.json
    new_component = Component(**data)
    db.session.add(new_component)
    db.session.commit()
    return 'ADDED'

# Clear all components
@app.route('/clear', methods=['POST'])
def clear_components():
    db.session.query(Component).delete()
    db.session.commit()
    return 'CLEARED'

# Run app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)



