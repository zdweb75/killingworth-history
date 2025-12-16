# Flask Web Application

## Overview
A simple beginner-friendly Flask web application demonstrating basic web development concepts.

## Project Structure
```
├── app.py              # Main Flask application
├── templates/          # HTML templates folder
│   └── index.html      # Home page template
├── static/             # Static assets folder
│   ├── style.css       # CSS styles
│   └── script.js       # JavaScript file
└── requirements.txt    # Python dependencies
```

## Running the Application
The app runs on port 5000. Start it with:
```bash
python app.py
```

## Key Concepts
- **Routes**: Defined using `@app.route()` decorator
- **Templates**: HTML files in `templates/` folder, rendered with `render_template()`
- **Static Files**: CSS/JS files in `static/` folder, referenced using `url_for('static', filename='...')`

## Dependencies
- Flask: Lightweight Python web framework
