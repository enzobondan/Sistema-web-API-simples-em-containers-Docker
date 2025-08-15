from datetime import datetime
from . import db

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.Numeric(12, 2), nullable=False)
    team_size = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'budget': float(self.budget),
            'team_size': self.team_size,
            'deadline': self.deadline.isoformat(),
            'created_at': self.created_at.isoformat()
        }