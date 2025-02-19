# Création d'un PDF Malveillant à des Fins de Recherche

## Avertissement
**Ce projet est destiné uniquement à des fins éducatives et de recherche.** L'utilisation non autorisée de ce script pour distribuer des PDF malveillants est illégale et contraire à l'éthique. Utilisez-le uniquement dans un environnement contrôlé pour l'analyse de sécurité et la recherche sur les vulnérabilités.

## Aperçu
Ce projet démontre comment du JavaScript peut être intégré dans un fichier PDF pour s'exécuter à l'ouverture du document. Historiquement, les attaquants ont utilisé cette technique pour exploiter des vulnérabilités dans les lecteurs de PDF. En étudiant cette méthode, les professionnels de la sécurité peuvent mieux comprendre les vecteurs d'attaque potentiels et améliorer les mesures de défense.

## Fonctionnalités clés
- **Génération de PDF :** Utilise la bibliothèque Python `fpdf` pour créer un document PDF simple.
- **Intégration de JavaScript :** Injecte un code JavaScript dans le PDF pour afficher une alerte contenant des informations système.
- **Recherche et tests :** Conçu pour être utilisé dans des environnements contrôlés afin d'étudier la manière dont différents lecteurs de PDF traitent les scripts intégrés.

## Prérequis
- Python 3.x
- Bibliothèque `fpdf` (installer avec `pip install fpdf`)

## Installation
1. Clonez ce dépôt ou téléchargez le script.
2. Installez les dépendances requises :
   ```bash
   pip install fpdf
   ```

## Utilisation
Pour générer le PDF malveillant, exécutez :
```bash
python pdf.py
```
Cela créera un fichier nommé `malicious.pdf` dans le répertoire courant.

## Payload JavaScript
Le code JavaScript intégré collecte des informations système (User-Agent et détails du système d'exploitation) et les affiche via une boîte d'alerte :
```javascript
var info = 'User-Agent: ' + app.viewerType + ' ' + app.viewerVersion + '\nOS: ' + platformName;
app.alert(info);
```

## Considérations de Sécurité
- **Environnement de test :** N'ouvrez le PDF généré que dans un environnement sécurisé et isolé.
- **Lecteurs de PDF modernes :** La plupart des lecteurs récents désactivent l'exécution du JavaScript par défaut, mais les logiciels plus anciens peuvent encore être vulnérables.
- **Utilisation éthique :** Ne distribuez pas et n'utilisez pas ce script à des fins malveillantes.

## Objectifs de Recherche
- **Analyser le comportement des lecteurs de PDF :** Tester comment différents lecteurs gèrent le JavaScript intégré.
- **Identifier les mesures de sécurité :** Documenter quelles fonctionnalités de sécurité empêchent l'exécution.
- **Améliorer les défenses :** Partager les résultats avec la communauté en cybersécurité pour renforcer la protection.

## Avis Légal
Utilisez ce script de manière responsable et uniquement dans des environnements où vous avez l'autorisation explicite de mener des recherches en sécurité. Une utilisation non autorisée peut enfreindre la loi et entraîner des conséquences graves.

## Licence
Ce projet est destiné à un usage éducatif uniquement et est fourni "tel quel" sans aucune garantie.



