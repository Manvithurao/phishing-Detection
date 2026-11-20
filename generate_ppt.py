from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Theme colors
NAVY = RGBColor(12, 29, 55)
BLUE = RGBColor(30, 98, 180)
LIGHT = RGBColor(239, 244, 249)
ACCENT = RGBColor(35, 174, 118)
TEXT = RGBColor(33, 37, 41)
WHITE = RGBColor(255, 255, 255)
GRAY = RGBColor(88, 96, 105)


def set_background(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_title(slide, title, subtitle=None):
    title_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.35), Inches(12.0), Inches(0.8))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.alignment = PP_ALIGN.LEFT
    run = p.runs[0]
    run.font.size = Pt(26)
    run.font.bold = True
    run.font.color.rgb = NAVY
    if subtitle:
        sub = slide.shapes.add_textbox(Inches(0.65), Inches(0.95), Inches(12.0), Inches(0.4))
        stf = sub.text_frame
        sp = stf.paragraphs[0]
        sp.text = subtitle
        sp.alignment = PP_ALIGN.LEFT
        sr = sp.runs[0]
        sr.font.size = Pt(11)
        sr.font.color.rgb = GRAY


def add_bullets(slide, bullets, left=0.9, top=1.5, width=11.6, height=4.6):
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    for i, bullet in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = bullet
        p.level = 0
        p.bullet = True
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(8)
        run = p.runs[0]
        run.font.size = Pt(22 if len(bullet) < 60 else 18)
        run.font.color.rgb = TEXT


def add_footer(slide, text):
    footer = slide.shapes.add_textbox(Inches(0.6), Inches(7.0), Inches(12.0), Inches(0.3))
    tf = footer.text_frame
    p = tf.paragraphs[0]
    p.text = text
    p.alignment = PP_ALIGN.RIGHT
    run = p.runs[0]
    run.font.size = Pt(9)
    run.font.color.rgb = GRAY

# Slide 1: Title
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_background(slide, WHITE)
# top accent band
band = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.333), Inches(0.3))
band.fill.solid(); band.fill.fore_color.rgb = BLUE
band.line.fill.background()

logo = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(3.2), Inches(0.7))
tf = logo.text_frame
p = tf.paragraphs[0]
p.text = 'Phishing Website Detection System'
p.alignment = PP_ALIGN.LEFT
run = p.runs[0]
run.font.size = Pt(18)
run.font.bold = True
run.font.color.rgb = NAVY

big = slide.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(8.5), Inches(1.8))
tf2 = big.text_frame
p2 = tf2.paragraphs[0]
p2.text = 'Project Presentation'
p2.alignment = PP_ALIGN.LEFT
run2 = p2.runs[0]
run2.font.size = Pt(30)
run2.font.bold = True
run2.font.color.rgb = NAVY

sub = slide.shapes.add_textbox(Inches(0.8), Inches(3.2), Inches(8.0), Inches(1.1))
tf3 = sub.text_frame
p3 = tf3.paragraphs[0]
p3.text = 'Machine Learning + Flask Web Application for Real-Time Phishing Detection'
p3.alignment = PP_ALIGN.LEFT
run3 = p3.runs[0]
run3.font.size = Pt(18)
run3.font.color.rgb = TEXT

box = slide.shapes.add_shape(1, Inches(9.0), Inches(1.5), Inches(3.6), Inches(3.8))
box.fill.solid(); box.fill.fore_color.rgb = LIGHT
box.line.color.rgb = BLUE
box.line.width = Pt(1.5)

shape_tf = box.text_frame
shape_tf.word_wrap = True
shape_tf.margin_left = Inches(0.2)
shape_tf.margin_right = Inches(0.2)
shape_tf.margin_top = Inches(0.2)
shape_tf.margin_bottom = Inches(0.2)
par = shape_tf.paragraphs[0]
par.text = 'Prepared by:\nProject Team\nCybersecurity / AI Development'
par.alignment = PP_ALIGN.CENTER
par.runs[0].font.size = Pt(18)
par.runs[0].font.color.rgb = NAVY
add_footer(slide, '10-Slide Project Presentation | 2026')

# Slide 2: Problem & Objective
slide = prs.slides.add_slide(prs.slide_layouts[6]); set_background(slide, WHITE)
add_title(slide, '1. Problem Statement & Objective', 'Why this project matters')
add_bullets(slide, [
    'Phishing attacks trick users into revealing sensitive data such as passwords, OTPs, and banking information.',
    'Traditional blacklist-based detection is slow and fails against new and rapidly changing phishing websites.',
    'The project aims to detect phishing URLs in real time using machine learning and an easy-to-use web interface.',
    'Goal: improve cybersecurity awareness and provide a fast, accessible defense tool for users and administrators.'
], left=0.9, top=1.5, width=11.6, height=4.5)
add_footer(slide, 'Objective: Real-time phishing URL classification')

# Slide 3: Overview
slide = prs.slides.add_slide(prs.slide_layouts[6]); set_background(slide, WHITE)
add_title(slide, '2. Project Overview', 'System at a glance')
add_bullets(slide, [
    'The system accepts a suspicious URL from a user through a Flask web app.',
    'It extracts key lexical and domain-based features from the link.',
    'A trained Random Forest classifier predicts whether the website is legitimate or phishing.',
    'The result is displayed with a risk score, confidence level, and scan history stored in a database.',
    'The project combines cybersecurity, data science, and web development into one practical solution.'
])
add_footer(slide, 'Core idea: detect malicious links before users click')

# Slide 4: Architecture
slide = prs.slides.add_slide(prs.slide_layouts[6]); set_background(slide, LIGHT)
add_title(slide, '3. System Architecture', 'End-to-end workflow')
text = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.8), Inches(4.8))
tf = text.text_frame
p = tf.paragraphs[0]
p.text = 'User enters URL → Flask backend receives input → Feature extraction module analyzes URL structure → Random Forest model classifies risk → Result stored in SQLite → UI shows report and scan history'
p.alignment = PP_ALIGN.LEFT
run = p.runs[0]
run.font.size = Pt(22)
run.font.color.rgb = NAVY
# Add simple flow arrows using shapes for emphasis
for x in [1.3, 3.6, 5.9, 8.2, 10.5]:
    shape = slide.shapes.add_shape(1, Inches(x), Inches(3.0), Inches(1.1), Inches(0.45))
    shape.fill.solid(); shape.fill.fore_color.rgb = BLUE
    shape.line.fill.background()
    tf2 = shape.text_frame; tf2.text = '→'; tf2.paragraphs[0].alignment = PP_ALIGN.CENTER; tf2.paragraphs[0].runs[0].font.size = Pt(24); tf2.paragraphs[0].runs[0].font.bold = True; tf2.paragraphs[0].runs[0].font.color.rgb = WHITE
add_footer(slide, 'Architecture designed for speed and user accessibility')

# Slide 5: Feature Extraction
slide = prs.slides.add_slide(prs.slide_layouts[6]); set_background(slide, WHITE)
add_title(slide, '4. Feature Extraction Module', 'Signals used to identify phishing patterns')
add_bullets(slide, [
    'URL length: unusually long URLs are often used to hide the true destination.',
    'Presence of IP address: malicious links may directly embed an IP instead of a domain name.',
    'Use of @ symbol: browsers may ignore characters before the @ sign.',
    'Hyphen count: brand impersonation often uses fake domain names with hyphens.',
    'Domain age and suspicious keywords: phishing domains are often newly registered and use urgent terms like login, verify, update, or secure.'
])
add_footer(slide, 'Feature set is the backbone of model accuracy')

# Slide 6: ML Model
slide = prs.slides.add_slide(prs.slide_layouts[6]); set_background(slide, LIGHT)
add_title(slide, '5. Machine Learning Model', 'Random Forest Classifier')
add_bullets(slide, [
    'The model is trained on URL and domain-based risk features to classify websites as legitimate or phishing.',
    'Random Forest was selected because it handles non-linear patterns very effectively.',
    'It is robust against overfitting and provides good accuracy for real-time classification.',
    'The model outputs a probability score and confidence level to guide the final decision.',
    'This approach is faster and more adaptive than static blacklists alone.'
])
add_footer(slide, 'ML makes the system proactive against zero-day phishing links')

# Slide 7: Technologies Used
slide = prs.slides.add_slide(prs.slide_layouts[6]); set_background(slide, WHITE)
add_title(slide, '6. Technologies Used', 'Project stack')
add_bullets(slide, [
    'Python: core language for backend logic, model loading, and feature extraction.',
    'Flask: web framework for routing, form handling, and user interaction.',
    'scikit-learn: ML training and Random Forest implementation.',
    'pandas / numpy: dataset processing and numerical feature handling.',
    'HTML5 / CSS3 / JavaScript: responsive interface with a modern glassmorphism design.',
    'SQLite: local storage for user data, scan history, and reported URLs.'
])
add_footer(slide, 'A clean blend of AI, web development, and cybersecurity')

# Slide 8: UI & Application
slide = prs.slides.add_slide(prs.slide_layouts[6]); set_background(slide, WHITE)
add_title(slide, '7. User Interface & Functional Modules', 'Practical deployment')
add_bullets(slide, [
    'Home page: users paste a suspicious URL and get a phishing/legitimate result instantly.',
    'Dashboard: users can review previous scans and threat history.',
    'Admin dashboard: administrators monitor system activity and reported URLs.',
    'Login and registration pages: secure access for different user roles.',
    'Reporting feature allows suspicious websites to be flagged by the public or internal users.'
])
add_footer(slide, 'The interface is designed for both usability and security monitoring')

# Slide 9: Results & Evaluation
slide = prs.slides.add_slide(prs.slide_layouts[6]); set_background(slide, LIGHT)
add_title(slide, '8. Results & Evaluation', 'Performance overview')
add_bullets(slide, [
    'The system is designed to classify URLs quickly with a lightweight backend and efficient feature extraction pipeline.',
    'High recall is prioritized so that suspicious links are not missed.',
    'The app gives immediate feedback using a risk score and confidence indicator.',
    'Results are stored in a database for monitoring, reporting, and future model improvement.',
    'This makes the solution usable in real-world scenarios where speed and interpretability matter.'
])
add_footer(slide, 'Evaluation focus: accuracy, speed, usability, and threat detection')

# Slide 10: Conclusion & Final Takeaway
slide = prs.slides.add_slide(prs.slide_layouts[6]); set_background(slide, NAVY)
add_title(slide, '10. Conclusion & Final Takeaway', 'Project impact')
text = slide.shapes.add_textbox(Inches(0.8), Inches(2.0), Inches(11.6), Inches(3.5))
tf = text.text_frame
p = tf.paragraphs[0]
p.text = 'This project demonstrates how machine learning can be used to detect phishing websites before users are harmed. By combining URL analysis, Random Forest classification, and a Flask web app, the system provides an effective and user-friendly cybersecurity solution. Future enhancements include real-time blacklist APIs, advanced deep learning models, and browser extension support.'
p.alignment = PP_ALIGN.LEFT
run = p.runs[0]
run.font.size = Pt(22)
run.font.color.rgb = WHITE
add_footer(slide, 'Protecting users from phishing attacks through smart automation')

output_file = r"d:\phishing project\Phishing_Detection_Project_Presentation.pptx"
prs.save(output_file)
print(f"Created PowerPoint: {output_file}")
print(f"Slide count: {len(prs.slides)}")
