"""
Flask + HTMX Demo Application
A modern web application showcasing HTMX capabilities with Flask and Jinja2

Available Endpoints:
- / - Home page with feature overview
- /basic - Basic HTMX requests and triggers
- /tasks - Task management with CRUD operations
- /search - Live search and infinite scroll
- /forms - Form validation with server-side checks
- /polling - Auto-refresh and live notifications
- /modal - Modal dialogs and OOB swaps
- /transitions - CSS transitions and loading states
- /sse - Server-sent events for real-time updates

API Endpoints:
- /api/* - Various API endpoints for HTMX interactions
"""
from flask import Flask, render_template, request, jsonify, Response
from datetime import datetime
import time
import json

app = Flask(__name__)
# SECURITY: Change this secret key in production - use environment variables
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

# In-memory data store for demo purposes
tasks = [
    {"id": 1, "title": "Learn HTMX", "completed": False, "priority": "high"},
    {"id": 2, "title": "Build Flask App", "completed": False, "priority": "medium"},
    {"id": 3, "title": "Deploy to Production", "completed": False, "priority": "low"},
]

users = [
    {"id": i, "name": f"User {i}", "email": f"user{i}@example.com"} 
    for i in range(1, 51)
]

next_task_id = 4


@app.route('/')
def index():
    """Main page with navigation to all HTMX demos"""
    return render_template('index.html')


# =============================================================================
# BASIC HTMX EXAMPLES
# =============================================================================

@app.route('/basic')
def basic():
    """Basic HTMX requests demo"""
    return render_template('basic.html')


@app.route('/api/greet', methods=['GET'])
def greet():
    """Simple GET request"""
    name = request.args.get('name', 'World')
    return f'<div class="alert alert-success">Hello, {name}!</div>'


@app.route('/api/time', methods=['GET'])
def get_time():
    """Get current server time"""
    current_time = datetime.now().strftime('%H:%M:%S')
    return f'<span class="badge badge-info">{current_time}</span>'


# =============================================================================
# TASK MANAGEMENT (CRUD OPERATIONS)
# =============================================================================

@app.route('/tasks')
def tasks_page():
    """Task management demo"""
    return render_template('tasks.html', tasks=tasks)


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    filter_status = request.args.get('status', 'all')
    filtered_tasks = tasks
    
    if filter_status == 'completed':
        filtered_tasks = [t for t in tasks if t['completed']]
    elif filter_status == 'active':
        filtered_tasks = [t for t in tasks if not t['completed']]
    
    return render_template('partials/task_list.html', tasks=filtered_tasks)


@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    global next_task_id
    title = request.form.get('title')
    priority = request.form.get('priority', 'medium')
    
    if not title:
        return '<div class="alert alert-error">Task title is required</div>', 400
    
    new_task = {
        "id": next_task_id,
        "title": title,
        "completed": False,
        "priority": priority
    }
    tasks.append(new_task)
    next_task_id += 1
    
    return render_template('partials/task_item.html', task=new_task)


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a single task"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return '<div class="alert alert-error">Task not found</div>', 404
    return render_template('partials/task_item.html', task=task)


@app.route('/api/tasks/<int:task_id>/toggle', methods=['PUT', 'POST'])
def toggle_task(task_id):
    """Toggle task completion status"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return '<div class="alert alert-error">Task not found</div>', 404
    
    task['completed'] = not task['completed']
    return render_template('partials/task_item.html', task=task)


@app.route('/api/tasks/<int:task_id>/edit', methods=['GET'])
def edit_task_form(task_id):
    """Get edit form for a task"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return '<div class="alert alert-error">Task not found</div>', 404
    return render_template('partials/task_edit.html', task=task)


@app.route('/api/tasks/<int:task_id>', methods=['PUT', 'POST'])
def update_task(task_id):
    """Update a task"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return '<div class="alert alert-error">Task not found</div>', 404
    
    title = request.form.get('title')
    priority = request.form.get('priority')
    
    if not title:
        return '<div class="alert alert-error">Task title is required</div>', 400
    
    task['title'] = title
    task['priority'] = priority
    
    return render_template('partials/task_item.html', task=task)


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return '', 200


@app.route('/api/tasks/<int:task_id>/delete-confirm', methods=['GET'])
def delete_task_confirm(task_id):
    """Show delete confirmation"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return '<div class="alert alert-error">Task not found</div>', 404
    return render_template('partials/task_delete_confirm.html', task=task)


# =============================================================================
# SEARCH AND INFINITE SCROLL
# =============================================================================

@app.route('/search')
def search_page():
    """Search and infinite scroll demo"""
    return render_template('search.html')


@app.route('/api/search', methods=['GET'])
def search_users():
    """Search users with debouncing"""
    query = request.args.get('q', '').lower()
    
    # Simulate processing time
    time.sleep(0.3)
    
    filtered_users = [u for u in users if query in u['name'].lower() or query in u['email'].lower()]
    
    return render_template('partials/user_list.html', users=filtered_users, query=query)


@app.route('/api/users/infinite', methods=['GET'])
def infinite_scroll_users():
    """Infinite scroll pagination"""
    page = int(request.args.get('page', 1))
    per_page = 10
    
    # Simulate loading time
    time.sleep(0.5)
    
    start = (page - 1) * per_page
    end = start + per_page
    page_users = users[start:end]
    
    has_more = end < len(users)
    
    return render_template('partials/user_infinite.html', 
                         users=page_users, 
                         page=page + 1, 
                         has_more=has_more)


# =============================================================================
# FORMS AND VALIDATION
# =============================================================================

@app.route('/forms')
def forms_page():
    """Forms and validation demo"""
    return render_template('forms.html')


@app.route('/api/validate-email', methods=['POST'])
def validate_email():
    """Validate email on blur"""
    email = request.form.get('email', '')
    
    if not email:
        return '<div class="error-message">Email is required</div>', 400
    
    if '@' not in email or '.' not in email.split('@')[-1]:
        return '<div class="error-message">Please enter a valid email address</div>', 400
    
    return '<div class="success-message">✓ Email looks good!</div>', 200


@app.route('/api/validate-username', methods=['POST'])
def validate_username():
    """Validate username availability"""
    username = request.form.get('username', '')
    
    if not username:
        return '<div class="error-message">Username is required</div>', 400
    
    if len(username) < 3:
        return '<div class="error-message">Username must be at least 3 characters</div>', 400
    
    # Simulate checking database
    taken_usernames = ['admin', 'user', 'test']
    if username.lower() in taken_usernames:
        return '<div class="error-message">Username is already taken</div>', 400
    
    return '<div class="success-message">✓ Username is available!</div>', 200


@app.route('/api/submit-form', methods=['POST'])
def submit_form():
    """Submit the complete form"""
    username = request.form.get('username', '')
    email = request.form.get('email', '')
    
    # Simulate processing
    time.sleep(1)
    
    return f'''
    <div class="alert alert-success">
        <h3>Registration Successful!</h3>
        <p>Welcome, {username}!</p>
        <p>We've sent a confirmation email to {email}</p>
    </div>
    '''


# =============================================================================
# POLLING AND AUTO-REFRESH
# =============================================================================

@app.route('/polling')
def polling_page():
    """Polling and auto-refresh demo"""
    return render_template('polling.html')


@app.route('/api/server-status', methods=['GET'])
def server_status():
    """Get server status (simulated)"""
    import random
    
    cpu = random.randint(10, 90)
    memory = random.randint(30, 85)
    disk = random.randint(40, 70)
    
    return render_template('partials/server_status.html', 
                         cpu=cpu, 
                         memory=memory, 
                         disk=disk,
                         timestamp=datetime.now().strftime('%H:%M:%S'))


@app.route('/api/notifications', methods=['GET'])
def notifications():
    """Get new notifications"""
    import random
    
    notification_types = [
        ("info", "New user registered"),
        ("success", "Backup completed successfully"),
        ("warning", "High memory usage detected"),
        ("error", "Failed login attempt")
    ]
    
    # Randomly decide if there's a new notification
    if random.random() > 0.5:
        notif_type, message = random.choice(notification_types)
        return f'''
        <div class="notification notification-{notif_type}" 
             style="animation: slideIn 0.3s ease-out;">
            <strong>{notif_type.upper()}:</strong> {message}
            <span class="notification-time">{datetime.now().strftime('%H:%M:%S')}</span>
        </div>
        '''
    
    return '', 204


# =============================================================================
# MODALS AND OUT-OF-BAND SWAPS
# =============================================================================

@app.route('/modal')
def modal_page():
    """Modal dialogs demo"""
    return render_template('modal.html')


@app.route('/api/modal-content/<content_type>', methods=['GET'])
def modal_content(content_type):
    """Load modal content dynamically"""
    if content_type == 'info':
        title = "Information"
        body = "This is a dynamically loaded modal using HTMX!"
    elif content_type == 'form':
        title = "Quick Form"
        body = '''
        <form hx-post="/api/modal-submit" hx-target="#modal-body">
            <div class="form-group">
                <label>Your Name:</label>
                <input type="text" name="name" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        '''
    else:
        title = "Details"
        body = f"Content for {content_type}"
    
    return render_template('partials/modal_content.html', title=title, body=body)


@app.route('/api/modal-submit', methods=['POST'])
def modal_submit():
    """Submit modal form"""
    name = request.form.get('name', 'Guest')
    return f'<div class="alert alert-success">Thank you, {name}!</div>'


@app.route('/api/oob-demo', methods=['POST'])
def oob_demo():
    """Out-of-band swap demo"""
    # This returns multiple updates in one response
    return '''
    <div id="main-content" class="alert alert-success">
        Main content updated!
    </div>
    <div id="sidebar-content" hx-swap-oob="true" class="alert alert-info">
        Sidebar updated via OOB swap!
    </div>
    <div id="header-status" hx-swap-oob="true">
        <span class="badge badge-success">Connected</span>
    </div>
    '''


# =============================================================================
# LOADING STATES AND CSS TRANSITIONS
# =============================================================================

@app.route('/transitions')
def transitions_page():
    """CSS transitions and loading states demo"""
    return render_template('transitions.html')


@app.route('/api/slow-load', methods=['GET'])
def slow_load():
    """Simulate slow loading for demonstration"""
    duration = int(request.args.get('duration', 2))
    time.sleep(duration)
    
    return '''
    <div class="card">
        <h3>Content Loaded!</h3>
        <p>This content took a while to load, but HTMX showed a nice loading indicator.</p>
    </div>
    '''


# =============================================================================
# SERVER-SENT EVENTS (SSE)
# =============================================================================

@app.route('/sse')
def sse_page():
    """Server-Sent Events demo"""
    return render_template('sse.html')


@app.route('/api/sse-stream')
def sse_stream():
    """Server-sent events stream"""
    def generate():
        import random
        for i in range(10):
            time.sleep(1)
            data = {
                'count': i + 1,
                'message': f'Update {i + 1}',
                'value': random.randint(1, 100)
            }
            yield f"data: {json.dumps(data)}\n\n"
    
    return Response(generate(), mimetype='text/event-stream')


@app.route('/api/sse-content', methods=['POST'])
def sse_content():
    """Handle SSE data and return HTML"""
    data = request.get_json()
    count = data.get('count', 0)
    message = data.get('message', '')
    value = data.get('value', 0)
    
    return f'''
    <div class="sse-item" style="animation: slideIn 0.3s ease-out;">
        <span class="badge badge-primary">#{count}</span>
        <strong>{message}</strong>
        <div class="progress">
            <div class="progress-bar" style="width: {value}%">{value}%</div>
        </div>
    </div>
    '''


if __name__ == '__main__':
    # SECURITY WARNING: Debug mode should only be used in development
    # In production, use a WSGI server (gunicorn, uwsgi) without debug=True
    app.run(debug=True, host='0.0.0.0', port=5000)
