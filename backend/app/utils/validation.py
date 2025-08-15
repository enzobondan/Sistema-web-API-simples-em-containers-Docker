from datetime import datetime

def validate_project_data(data):
    errors = {}
    
    if not data.get('title') or len(data['title']) > 100:
        errors['title'] = "Title is required (max 100 chars)"
    
    if not data.get('description'):
        errors['description'] = "Description is required"
    
    if data.get('budget') is None or float(data['budget']) <= 0:
        errors['budget'] = "Valid budget amount required"
    
    try:
        datetime.fromisoformat(data['deadline'])
    except (ValueError, KeyError):
        errors['deadline'] = "Valid ISO date required"
    
    return errors