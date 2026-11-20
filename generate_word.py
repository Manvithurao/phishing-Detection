from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

slides = [
    {
        'title': 'Phishing Website Detection System',
        'subtitle': 'Project Presentation',
        'content': [
            'Machine Learning + Flask Web Application for Real-Time Phishing Detection',
            'Prepared by: Project Team',
            'Cybersecurity / AI Development'
        ]
    },
    {
        'title': '1. Problem Statement & Objective',
        'subtitle': 'Why this project matters',
        'content': [
            'Phishing attacks trick users into revealing sensitive data such as passwords, OTPs, and banking information.',
            'Traditional blacklist-based detection is slow and fails against new and rapidly changing phishing websites.',
            'The project aims to detect phishing URLs in real time using machine learning and an easy-to-use web interface.',
            'Goal: improve cybersecurity awareness and provide a fast, accessible defense tool for users and administrators.'
        ]
    },
    {
        'title': '2. Project Overview',
        'subtitle': 'System at a glance',
        'content': [
            'The system accepts a suspicious URL from a user through a Flask web app.',
            'It extracts key lexical and domain-based features from the link.',
            'A trained Random Forest classifier predicts whether the website is legitimate or phishing.',
            'The result is displayed with a risk score, confidence level, and scan history stored in a database.',
            'The project combines cybersecurity, data science, and web development into one practical solution.'
        ]
    },
    {
        'title': '3. System Architecture',
        'subtitle': 'End-to-end workflow',
        'content': [
            'User enters URL → Flask backend receives input → Feature extraction module analyzes URL structure → Random Forest model classifies risk → Result stored in SQLite → UI shows report and scan history.'
        ]
    },
    {
        'title': '4. Feature Extraction Module',
        'subtitle': 'Signals used to identify phishing patterns',
        'content': [
            'URL length: unusually long URLs are often used to hide the true destination.',
            'Presence of IP address: malicious links may directly embed an IP instead of a domain name.',
            'Use of @ symbol: browsers may ignore characters before the @ sign.',
            'Hyphen count: brand impersonation often uses fake domain names with hyphens.',
            'Domain age and suspicious keywords: phishing domains are often newly registered and use urgent terms such as login, verify, update, and secure.'
        ]
    },
    {
        'title': '5. Machine Learning Model',
        'subtitle': 'Random Forest Classifier',
        'content': [
            'The model is trained on URL and domain-based risk features to classify websites as legitimate or phishing.',
            'Random Forest was selected because it handles non-linear patterns very effectively.',
            'It is robust against overfitting and provides good accuracy for real-time classification.',
            'The model outputs a probability score and confidence level to guide the final decision.',
            'This approach is faster and more adaptive than static blacklists alone.'
        ]
    },
    {
        'title': '6. Technologies Used',
        'subtitle': 'Project stack',
        'content': [
            'Python: core language for backend logic, model loading, and feature extraction.',
            'Flask: web framework for routing, form handling, and user interaction.',
            'scikit-learn: ML training and Random Forest implementation.',
            'pandas / numpy: dataset processing and numerical feature handling.',
            'HTML5 / CSS3 / JavaScript: responsive interface with a modern glassmorphism design.',
            'SQLite: local storage for user data, scan history, and reported URLs.'
        ]
    },
    {
        'title': '7. User Interface & Functional Modules',
        'subtitle': 'Practical deployment',
        'content': [
            'Home page: users paste a suspicious URL and get a phishing/legitimate result instantly.',
            'Dashboard: users can review previous scans and threat history.',
            'Admin dashboard: administrators monitor system activity and reported URLs.',
            'Login and registration pages: secure access for different user roles.',
            'Reporting feature allows suspicious websites to be flagged by the public or internal users.'
        ]
    },
    {
        'title': '8. Results & Evaluation',
        'subtitle': 'Performance overview',
        'content': [
            'The system is designed to classify URLs quickly with a lightweight backend and efficient feature extraction pipeline.',
            'High recall is prioritized so that suspicious links are not missed.',
            'The app gives immediate feedback using a risk score and confidence indicator.',
            'Results are stored in a database for monitoring, reporting, and future model improvement.',
            'This makes the solution usable in real-world scenarios where speed and interpretability matter.'
        ]
    },
    {
        'title': '9. Conclusion & Final Takeaway',
        'subtitle': 'Project impact',
        'content': [
            'This project demonstrates how machine learning can be used to detect phishing websites before users are harmed.',
            'By combining URL analysis, Random Forest classification, and a Flask web app, the system provides an effective and user-friendly cybersecurity solution.',
            'Future enhancements include real-time blacklist APIs, advanced deep learning models, and browser extension support.',
            'The solution can be extended into a broader security platform for malicious URL detection and online safety.'
        ]
    }
]


doc = Document()
section = doc.sections[0]
section.top_margin = Inches(0.5)
section.bottom_margin = Inches(0.5)
section.left_margin = Inches(0.75)
section.right_margin = Inches(0.75)

for index, slide in enumerate(slides, start=1):
    title = doc.add_paragraph()
    run = title.add_run(f"Slide {index}: {slide['title']}")
    run.bold = True
    run.font.size = Pt(22)
    run.font.name = 'Calibri'

    subtitle = doc.add_paragraph()
    run_sub = subtitle.add_run(slide['subtitle'])
    run_sub.italic = True
    run_sub.font.size = Pt(12)
    run_sub.font.name = 'Calibri'
    run_sub.font.color.rgb = RGBColor(79, 79, 79)

    for item in slide['content']:
      p = doc.add_paragraph(style='List Bullet')
      p.alignment = WD_ALIGN_PARAGRAPH.LEFT
      run_item = p.add_run(item)
      run_item.font.size = Pt(12)
      run_item.font.name = 'Calibri'

    doc.add_paragraph('')

output_path = r'd:\phishing project\Phishing_Detection_Project_Presentation.docx'
doc.save(output_path)
print(f'Created Word document: {output_path}')
print(f'Slide sections: {len(slides)}')
