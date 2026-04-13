from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Portfolio data — edit this to update your site
PORTFOLIO_DATA = {
    "name": "Deeptargha Maity",
    "title": "Aspiring Data Scientist",
    "subtitle": "2nd Year CSE Student",
    "tagline": "Turning curiosity into code, and data into insight.",
    "bio": "I am a dedicated and curious 19-year-old Computer Science & Engineering student from India with a strong passion for Data Science. I enjoy working with Python, data-driven tools, and building meaningful projects.",
    "about_long": "I believe in the power of data to transform the way we understand the world. Every day I am building towards my goal of becoming a skilled Data Scientist — someone who can bridge the gap between technology and real-world impact through intelligent analysis and visualization.",
    "stats": [
        {"number": "2", "label": "Years of Study"},
        {"number": "6", "label": "Projects Built"},
        {"number": "8+", "label": "Tools Learned"},
        {"number": "5", "label": "Languages Known"},
    ],
    "education": [
        {"year": "2026 – Present", "degree": "B.Tech in Computer Science & Engineering", "school": "2nd Year CSE · Data Science Focus", "current": True},
        {"year": "2024", "degree": "Higher Secondary (Class XII)", "school": "Garden Reach Mudiali High School", "current": False},
        {"year": "2022", "degree": "Secondary (Class X)", "school": "Garden Reach Mudiali High School", "current": False},
    ],
    "skills": {
        "programming": [
            {"name": "Python", "percent": 88},
            {"name": "C++", "percent": 75},
            {"name": "C", "percent": 72},
            {"name": "HTML / CSS", "percent": 80},
            {"name": "JavaScript", "percent": 65},
        ],
        "data_science": [
            {"name": "Data Analysis", "percent": 80},
            {"name": "Data Visualization", "percent": 78},
            {"name": "Statistics", "percent": 70},
            {"name": "Machine Learning", "percent": 55},
            {"name": "Problem Solving", "percent": 85},
        ],
        "tools": ["NumPy", "Pandas", "Matplotlib", "Seaborn", "Jupyter", "Google Colab", "Scikit-learn", "Excel", "Git", "VS Code"],
    },
    "projects": [
        {"number": "01", "title": "Student Portfolio Website", "desc": "A personal portfolio with forest-mountain theme, smooth animations, and responsive design showcasing my journey.", "tags": ["HTML", "CSS", "Flask"], "github": "https://github.com/Deeptargha-Maity/Portfolio", "demo": "#"},
        {"number": "02", "title": "Python Data Analysis", "desc": "Exploratory data analysis on a real-world dataset using Pandas and Matplotlib to uncover patterns and trends.", "tags": ["Python", "Pandas", "Matplotlib"], "github": "#", "demo": "#"},
        {"number": "03", "title": "Data Visualization Dashboard", "desc": "Interactive dashboard built with Seaborn and Matplotlib, visualizing student performance metrics.", "tags": ["Python", "Seaborn", "Jupyter"], "github": "#", "demo": "#"},
        {"number": "04", "title": "C++ Problem Solving", "desc": "Collection of algorithmic problems and solutions covering sorting, searching, and data structures.", "tags": ["C++", "DSA", "Algorithms"], "github": "#", "demo": None},
        {"number": "05", "title": "Mini ML Project", "desc": "A beginner machine learning model using Scikit-learn to predict outcomes from structured CSV data.", "tags": ["Python", "Scikit-learn", "ML"], "github": "#", "demo": None},
        {"number": "06", "title": "CSV Data Cleaning Tool", "desc": "A Python utility to detect, flag, and fix common data quality issues in CSV files before analysis.", "tags": ["Python", "Pandas", "NumPy"], "github": "#", "demo": None},
    ],
    "pillars": [
        {"icon": "", "title": "Data Analysis", "desc": "Finding patterns and meaning in raw datasets."},
        {"icon": "", "title": "Machine Learning", "desc": "Building models that learn and predict."},
        {"icon": "", "title": "Visualization", "desc": "Turning numbers into stories people can see."},
        {"icon": "", "title": "Problem Solving", "desc": "Using data to solve real-world challenges."},
    ],
    "journey": [
        {"step": "STEP 01", "title": "Mastering Python", "desc": "Started with Python fundamentals, built up to data manipulation and scripting."},
        {"step": "STEP 02", "title": "Foundations in C & C++", "desc": "Strengthened problem-solving, logic, and understanding of algorithms."},
        {"step": "STEP 03", "title": "Web Basics", "desc": "Learned HTML, CSS, and Flask to build interactive web applications."},
        {"step": "STEP 04", "title": "Data Science Tools", "desc": "Explored NumPy, Pandas, Matplotlib, Seaborn, and Jupyter."},
        {"step": "STEP 05", "title": "Mini Projects", "desc": "Applied knowledge through real projects — from CSV cleaners to dashboards."},
        {"step": "NEXT →", "title": "Deep ML & AI", "desc": "Currently diving into machine learning algorithms and advanced data workflows."},
    ],
    "socials": {
        "github": "https://github.com/Deeptargha-Maity",
        "linkedin": "https://www.linkedin.com/in/deeptarghamaity",
        "email": "deeptargha@email.com",
        "instagram": "https://www.instagram.com/dptg.exec",
    }
}

@app.route("/")
def index():
    return render_template("index.html", data=PORTFOLIO_DATA)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()
    if not name or not email or not message:
        return jsonify({"success": False, "error": "All fields are required."})
    # In production: send email or save to DB here
    print(f"New message from {name} <{email}>: {message}")
    return jsonify({"success": True, "message": f"Thanks {name}! I'll get back to you soon."})

if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, threaded=True)
