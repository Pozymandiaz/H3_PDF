FROM ubuntu:20.04

WORKDIR /app

# Installer les dépendances
RUN dpkg --add-architecture i386 && \
    apt update && apt install -y wget curl libxml2 libcanberra-gtk-module \
                   libxext6:i386 libxrender1:i386 libxtst6:i386 xvfb \
                   netcat && \
    wget -O /tmp/acrobat.deb http://ardownload.adobe.com/pub/adobe/reader/unix/9.x/9.5.5/fr/AdbeRdr9.5.5-1_i386linux_fra.deb && \
    dpkg -i /tmp/acrobat.deb || apt --fix-broken install -y && \
    rm /tmp/acrobat.deb

# Copier le PDF malveillant et le script de démarrage
COPY malicious.pdf /app/malicious.pdf
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]