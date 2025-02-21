def detect_javascript_in_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf_content = f.read()

    if b"/JavaScript" in pdf_content or b"/JS" in pdf_content:
        print("[✅] JavaScript détecté dans le PDF !")
    else:
        print("[❌] Aucun JavaScript détecté.")

if __name__ == "__main__":
    detect_javascript_in_pdf("malicious.pdf")
