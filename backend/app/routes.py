from flask import request, jsonify
from . import db
from .models import Project
from .utils.validation import validate_project_data

def init_app(app):
    @app.route('/api/projects', methods=['GET', 'POST'])
    def handle_projects():
        if request.method == 'POST':
            data = request.get_json()
            
            errors = validate_project_data(data)
            if errors:
                return jsonify({"errors": errors}), 400
                
            try:
                project = Project(
                    title=data['title'],
                    description=data['description'],
                    category=data['category'],
                    budget=data['budget'],
                    team_size=data['team_size'],
                    deadline=data['deadline']
                )
                db.session.add(project)
                db.session.commit()
                return jsonify(project.to_dict()), 201
            except Exception as e:
                return jsonify({"error": str(e)}), 500
                
        elif request.method == 'GET':
            projects = Project.query.order_by(Project.created_at.desc()).all()
            return jsonify([p.to_dict() for p in projects])
    
    @app.route('/api/projects/<int:id>', methods=['GET'])
    def get_project(id):
        project = Project.query.get_or_404(id)
        return jsonify(project.to_dict())