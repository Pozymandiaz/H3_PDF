FROM ubuntu:20.04
WORKDIR /app

# Installation du lecteur PDF (ex: Adobe Reader 9 qui supporte JavaScript)
RUN apt update && apt install -y wget curl && \
    wget -O /tmp/acrobat.deb http://ardownload.adobe.com/pub/adobe/reader/unix/9.x/9.5.5/fr/AdbeRdr9.5.5-1_i386linux_fra.deb && \
    dpkg -i /tmp/acrobat.deb || apt --fix-broken install -y

# Copier le fichier PDF malveillant
COPY malicious.pdf /app/malicious.pdf
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]
