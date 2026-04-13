# Deeptargha Maity — Portfolio (Flask)

Forest & Mountain themed personal portfolio built with **Flask + HTML + CSS + JavaScript**.

## Project Structure

```
portfolio/
├── app.py                  ← Flask backend (routes + data)
├── requirements.txt
├── templates/
│   └── index.html          ← Jinja2 HTML template
└── static/
    ├── css/
    │   └── main.css        ← All styles (green forest theme)
    └── js/
        └── main.js         ← Particles, cursor, scroll reveal, contact form
```

## Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the Flask server
python app.py

# 3. Open in browser
http://localhost:5000
```

## Customisation

All portfolio content lives in **`app.py`** inside the `PORTFOLIO_DATA` dictionary.  
Edit that file to update your name, links, projects, skills, etc. — no HTML changes needed.

To add your real social links, replace the `"#"` placeholders in `PORTFOLIO_DATA["socials"]`.

## Contact Form

The `/contact` POST route receives form submissions.  
In production, replace the `print(...)` line in `app.py` with your email-sending or database logic.
