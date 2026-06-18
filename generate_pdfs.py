import os
from xhtml2pdf import pisa

# Resume files to convert
resumes = [
    "resume-einzelhandel.html",
    "resume-buero.html",
    "resume-lager.html",
    "resume-service.html",
    "resume-kundenservice.html",
    "resume-bildung.html",
    "resume-fahrtdienste.html",
    "resume-reinigung.html",
    "resume-gesundheit.html",
]

# Directories
resumes_dir = os.path.join(os.path.dirname(__file__), "resumes")
pdf_dir = os.path.join(os.path.dirname(__file__), "pdf")

# Create pdf directory if it doesn't exist
os.makedirs(pdf_dir, exist_ok=True)

print("Generating PDFs from HTML resumes...")

for resume in resumes:
    html_path = os.path.join(resumes_dir, resume)
    pdf_name = resume.replace(".html", ".pdf")
    pdf_path = os.path.join(pdf_dir, pdf_name)
    
    if os.path.exists(html_path):
        try:
            # Read HTML file
            with open(html_path, "r", encoding="utf-8") as f:
                html_content = f.read()
            
            # Convert HTML to PDF
            with open(pdf_path, "wb") as pdf_file:
                pisa_status = pisa.CreatePDF(
                    html_content,
                    dest=pdf_file,
                    encoding="utf-8"
                )
            
            if pisa_status.err:
                print(f"[ERROR] {resume}: {pisa_status.err} errors")
            else:
                print(f"[OK] {pdf_name}")
        except Exception as e:
            print(f"[ERROR] {resume}: {e}")
    else:
        print(f"[NOT FOUND] {resume}")

print(f"\nDone! PDFs saved to: {pdf_dir}")
