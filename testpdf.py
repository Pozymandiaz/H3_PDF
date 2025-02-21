import fitz  # PyMuPDF

def check_pdf_javascript(pdf_path):
    """Vérifie si du JavaScript est présent dans le PDF."""
    doc = fitz.open(pdf_path)
    js_found = False

    for i in range(len(doc)):
        page = doc[i]
        annots = page.annots()  # Vérifie les annotations (JS peut être caché ici)

        if annots:
            for annot in annots:
                if "JavaScript" in str(annot.info):
                    js_found = True
                    print(f"[✅] JavaScript détecté sur la page {i+1} !")

    if not js_found:
        print(f"[❌] Aucun JavaScript détecté dans {pdf_path}.")

check_pdf_javascript("malicious.pdf")
