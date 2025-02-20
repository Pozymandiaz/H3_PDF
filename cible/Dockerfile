FROM ubuntu:20.04

WORKDIR /app

# Désactiver les invites interactives
ENV DEBIAN_FRONTEND=noninteractive TZ=Europe/Paris

# Installer Wine sans interaction
RUN apt update && apt install -y wine


# Copier le PDF malveillant et le script de démarrage
COPY malicious.pdf /app/malicious.pdf
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]