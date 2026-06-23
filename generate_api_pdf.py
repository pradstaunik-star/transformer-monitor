from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.enums import TA_LEFT

doc = SimpleDocTemplate(
    r"C:\_Coding\_G2R\API_Reference.pdf",
    pagesize=A4,
    leftMargin=2.5*cm, rightMargin=2.5*cm,
    topMargin=2.5*cm, bottomMargin=2.5*cm,
)

styles = getSampleStyleSheet()
title_style   = ParagraphStyle("title",  fontSize=18, fontName="Helvetica-Bold", spaceAfter=4)
sub_style     = ParagraphStyle("sub",    fontSize=11, fontName="Helvetica",      spaceAfter=16, textColor=colors.grey)
h1_style      = ParagraphStyle("h1",     fontSize=14, fontName="Helvetica-Bold", spaceBefore=18, spaceAfter=6,
                                textColor=colors.HexColor("#2E75B6"))
body_style    = ParagraphStyle("body",   fontSize=10, fontName="Helvetica",      spaceAfter=6, leading=14)
code_style    = ParagraphStyle("code",   fontSize=9,  fontName="Courier",        spaceAfter=10, leading=13,
                                backColor=colors.HexColor("#F4F4F4"),
                                leftIndent=12, rightIndent=12,
                                borderPadding=(6, 6, 6, 6))

story = []

story.append(Paragraph("Transformer Monitor — API Reference", title_style))
story.append(Paragraph("Base URL: http://&lt;host&gt;:5000", sub_style))

# GET /temperature
story.append(Paragraph("GET /temperature", h1_style))
story.append(Paragraph("Returns the current simulation state.", body_style))
story.append(Preformatted(
    '{\n'
    '  "current_temperature": 73.42,\n'
    '  "ambient_temperature": 25.0,\n'
    '  "load_percent": 80.0,\n'
    '  "fans_on": false,\n'
    '  "fan_mode": "auto",\n'
    '  "fan_on_threshold": 90.0,\n'
    '  "fan_off_threshold": 50.0\n'
    '}',
    code_style,
))

# GET /history
story.append(Paragraph("GET /history", h1_style))
story.append(Paragraph("Returns up to 20 temperature readings (one per ~3 s), oldest first.", body_style))
story.append(Preformatted(
    '[ {"t": 1750000000, "v": 61.5}, {"t": 1750000003, "v": 63.2}, ... ]',
    code_style,
))
story.append(Paragraph('"t" is a Unix timestamp, "v" is oil temperature in °C.', body_style))

# POST /settings
story.append(Paragraph("POST /settings", h1_style))
story.append(Paragraph("Updates simulation settings. All fields are optional.", body_style))
story.append(Preformatted(
    'Content-Type: application/json\n\n'
    '{\n'
    '  "ambient_temperature": 30.0,\n'
    '  "load_percent": 75.0,\n'
    '  "fan_mode": "auto",          // "auto" or "manual"\n'
    '  "fan_on_threshold": 90.0,    // auto mode only\n'
    '  "fan_off_threshold": 50.0,   // auto mode only\n'
    '  "fans_on": true              // manual mode only\n'
    '}',
    code_style,
))
story.append(Paragraph('Response: {"status": "ok"}', body_style))

doc.build(story)
print("Done")
