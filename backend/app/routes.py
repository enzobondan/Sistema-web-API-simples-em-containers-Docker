from flask import request, jsonify
from . import db
from .models import Project
from .utils.validation import validate_project_data

def init_app(app):
    @app.route('/api/projects', methods=['GET', 'POST'])
    def handle_projects():
        if request.method == 'POST':
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data provided"}), 400
                
            errors = validate_project_data(data)
            if errors:
                return jsonify({"errors": errors}), 400
                
            try:
                project = Project(
                    title=data.get('title'),
                    description=data.get('description'),
                    category=data.get('category'),
                    budget=data.get('budget'),
                    team_size=data.get('team_size'),
                    deadline=data.get('deadline')
                )
                db.session.add(project)
                db.session.commit()
                return jsonify(project.to_dict()), 201
            except Exception as e:
                db.session.rollback()
                app.logger.error(f"Error creating project: {str(e)}")
                return jsonify({"error": "Internal server error"}), 500
                
                
        elif request.method == 'GET':
            projects = Project.query.order_by(Project.created_at.desc()).all()
            return jsonify([p.to_dict() for p in projects])
    
    @app.route('/api/projects/<int:id>', methods=['GET'])
    def get_project(id):
        project = Project.query.get_or_404(id)
        return jsonify(project.to_dict())