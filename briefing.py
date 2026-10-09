from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter

def build_briefing(text_content, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'NewspaperTitle',
        parent=styles['Heading1'],
        fontSize=24,
        leading=28,
        spaceAfter=12
    )
    
    story = [
        Paragraph("AMELIA'S MORNING TECH DIGEST", title_style),
        Spacer(1, 12)
    ]
    
    for paragraph in text_content.split("\n\n"):
        story.append(Paragraph(paragraph.replace("\n", "<br/>"), styles['Normal']))
        story.append(Spacer(1, 10))
        
    doc.build(story)
    return filename
