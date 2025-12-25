from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_incident_report(case):
    """
    Generate a SOC incident report in PDF format.
    """

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/incident_{case['case_id']}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    width, height = A4
    y = height - 50

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Security Incident Report")
    y -= 40

    # Metadata
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Incident ID: {case['case_id']}")
    y -= 20
    c.drawString(50, y, f"Created At: {case['created_at']}")
    y -= 20
    c.drawString(50, y, f"Severity: {case['severity']}")
    y -= 30

    # Incident Details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Incident Details")
    y -= 20

    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Title: {case['title']}")
    y -= 20
    c.drawString(50, y, f"Source IP: {case['source_ip']}")
    y -= 20
    c.drawString(50, y, f"Affected Host: {case['host']}")
    y -= 30

    # Response Section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Recommended Response Actions")
    y -= 20

    c.setFont("Helvetica", 11)
    actions = [
        "Block source IP at firewall",
        "Check for compromised credentials",
        "Monitor host for further suspicious activity",
        "Perform password reset if required"
    ]

    for action in actions:
        c.drawString(60, y, f"- {action}")
        y -= 15

    # Footer
    y -= 30
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(
        50, y,
        f"Report generated automatically by SOC Automation Platform on {datetime.utcnow().isoformat()}Z"
    )

    c.save()
    return filename


if __name__ == "__main__":
    sample_case = {
        "case_id": "demo1234",
        "title": "SSH brute force attempt",
        "severity": "HIGH",
        "source_ip": "185.220.101.1",
        "host": "linux-server",
        "created_at": datetime.utcnow().isoformat() + "Z"
    }

    report = generate_incident_report(sample_case)
    print(f"Incident report generated: {report}")
