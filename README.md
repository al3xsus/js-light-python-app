# 🚀 Flask + HTMX Demo Application

A comprehensive demonstration of HTMX capabilities with Flask and Jinja2. This modern web application showcases how to build dynamic, interactive user interfaces without writing JavaScript.

## 📋 Features

This application demonstrates the following HTMX features:

### 🎯 Basic Operations
- **GET/POST Requests** - Simple AJAX requests without page reloads
- **Dynamic Content Loading** - Fetch and display content on demand
- **Debouncing** - Optimize requests with input delays

### ✅ Task Management (CRUD)
- **Create** - Add new tasks with inline forms
- **Read** - Display and filter tasks dynamically
- **Update** - Inline editing with server validation
- **Delete** - Confirmation dialogs before deletion
- **Real-time Filtering** - Filter by status (all/active/completed)

### 🔍 Search & Navigation
- **Live Search** - Search-as-you-type with debouncing
- **Infinite Scroll** - Automatic pagination without buttons
- **Loading Indicators** - Visual feedback during requests

### 📝 Forms & Validation
- **Real-time Validation** - Server-side validation on field blur
- **Inline Feedback** - Show errors/success next to fields
- **Form Submission** - AJAX form posts with response handling

### 🔄 Real-time Updates
- **Polling** - Auto-refresh content at intervals
- **Live Notifications** - Check for updates periodically
- **Server Status Monitor** - Real-time dashboard metrics

### 🪟 Advanced Features
- **Modal Dialogs** - Dynamic content loading in modals
- **Out-of-Band Swaps (OOB)** - Update multiple page areas from one request
- **CSS Transitions** - Smooth animations with HTMX classes
- **Loading States** - Various loading indicators and disabled states
- **Server-Sent Events (SSE)** - Real-time server push updates

## 🛠️ Technology Stack

- **Python 3.x** - Backend language
- **Flask 3.0** - Web framework
- **Jinja2 3.1** - Template engine
- **HTMX 1.9** - Frontend interactivity
- **Modern CSS** - Custom styling with CSS variables

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/al3xsus/js-light-python-app.git
cd js-light-python-app
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Open your browser**
Navigate to `http://localhost:5000`

## 📖 Usage

The application consists of multiple demo pages, each showcasing different HTMX features:

- **Home** (`/`) - Overview of all features with navigation
- **Basic** (`/basic`) - Fundamental HTMX requests and triggers
- **Tasks** (`/tasks`) - Complete CRUD task management system
- **Search** (`/search`) - Live search and infinite scroll
- **Forms** (`/forms`) - Form validation with server-side checks
- **Polling** (`/polling`) - Auto-refresh and live notifications
- **Modal** (`/modal`) - Dynamic modals and OOB swaps
- **Transitions** (`/transitions`) - CSS animations and loading states
- **SSE** (`/sse`) - Server-sent events for real-time updates

## 🎨 HTMX Attributes Demonstrated

| Attribute | Purpose | Example Page |
|-----------|---------|--------------|
| `hx-get` | Issue GET request | Basic, Search |
| `hx-post` | Issue POST request | Tasks, Forms |
| `hx-put` | Issue PUT request | Tasks (update) |
| `hx-delete` | Issue DELETE request | Tasks (delete) |
| `hx-target` | Specify where to load response | All pages |
| `hx-swap` | Control how content is swapped | All pages |
| `hx-trigger` | Specify what triggers request | Basic, Search, Polling |
| `hx-indicator` | Show loading indicator | Search, Transitions |
| `hx-swap-oob` | Out-of-band swaps | Modal |
| `hx-disabled-elt` | Disable elements during request | Transitions |
| `hx-include` | Include additional elements | Basic |

## 🏗️ Project Structure

```
js-light-python-app/
├── app.py                 # Flask application with all routes
├── requirements.txt       # Python dependencies
├── static/
│   └── css/
│       └── style.css     # Custom CSS styling
├── templates/
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   ├── basic.html        # Basic HTMX examples
│   ├── tasks.html        # Task management
│   ├── search.html       # Search and infinite scroll
│   ├── forms.html        # Form validation
│   ├── polling.html      # Polling and auto-refresh
│   ├── modal.html        # Modal and OOB swaps
│   ├── transitions.html  # CSS transitions
│   ├── sse.html          # Server-sent events
│   └── partials/         # Reusable template fragments
│       ├── task_item.html
│       ├── task_edit.html
│       ├── task_delete_confirm.html
│       ├── task_list.html
│       ├── user_list.html
│       ├── user_infinite.html
│       ├── server_status.html
│       └── modal_content.html
└── README.md             # This file
```

## 💡 Key Concepts

### Why HTMX?

HTMX allows you to:
- Build modern UIs without writing JavaScript
- Keep logic on the server where it belongs
- Use hypermedia as the engine of application state
- Progressively enhance existing applications
- Reduce complexity and bundle sizes

### Why Flask?

Flask is:
- Lightweight and flexible
- Perfect for serving HTML fragments
- Easy to learn and use
- Has excellent template support with Jinja2

### Pattern: Partial Templates

This app uses the "partial template" pattern where:
1. Server returns small HTML fragments
2. HTMX swaps them into the DOM
3. Each fragment is a reusable Jinja2 template
4. Logic stays server-side (Python)

## 🔧 Development

### Adding New Features

1. Add a route in `app.py`
2. Create a template in `templates/`
3. Create partials in `templates/partials/` if needed
4. Add navigation link in `base.html`
5. Test the feature

### Customizing Styles

Edit `static/css/style.css` to customize:
- Color scheme (CSS variables in `:root`)
- Component styles
- Animations and transitions
- Responsive breakpoints

## 📚 Learning Resources

- [HTMX Documentation](https://htmx.org/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available for educational purposes.

## 🎯 Next Steps

Try these challenges to extend your learning:
1. Add user authentication
2. Connect to a real database
3. Add file upload functionality
4. Implement drag-and-drop sorting
5. Add WebSocket support
6. Create a chat application

---

**Built with ❤️ using Python, Flask, and HTMX**
