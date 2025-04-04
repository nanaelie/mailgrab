# email_extractor
Email Extractor est un outil Python permettant d'extraire des adresses email à partir de pages web ou de fichiers texte. Il utilise les expressions régulières pour identifier et extraire les emails, et Playwright pour le scraping web. Ce projet est idéal pour récupérer des adresses email à partir de différentes sources.

## Fonctionnalités

- Extrait des adresses email à partir d'une URL de site web ou d'un fichier texte.
- Utilisation de Playwright pour l'extraction de contenu de pages web avec gestion des erreurs.
- Recherche d'emails via des expressions régulières.
- Interface en ligne de commande simple à utiliser.
- Support pour l'extraction unique ou multiple (selon le nombre d'emails trouvés).

## Installation

Avant d'utiliser **Email Extractor**, assure-toi que Python 3.x est installé sur ta machine.

### Étapes d'installation :

1. **Cloner le dépôt** :

   ```bash
   git clone https://github.com/nanaelie/email_extractor.git
   ```

2. **Installer les dépendances** :

   Accède au répertoire du projet et installe les dépendances nécessaires :

   ```bash
   cd email_extractor
   pip install -r requirements.txt
   ```

   > **Remarque** : Assure-toi que Playwright est correctement installé. Tu peux également avoir besoin de télécharger les navigateurs utilisés par Playwright avec cette commande :
   ```bash
   python -m playwright install
   ```

## Utilisation

**Email Extractor** fonctionne en ligne de commande et accepte deux types d'entrées : une URL de site web ou un chemin vers un fichier texte.

### Extraire des emails depuis une URL

Si tu souhaites extraire des emails d'une page web, utilise l'option `--url` et fournis l'URL du site :

```bash
python email_extractor.py --url "https://example.com"
```

Cela extraira les adresses email présentes sur la page web à l'URL spécifiée.

### Extraire des emails depuis un fichier texte

Pour extraire des emails à partir d'un fichier texte, utilise l'option `--file` et fournis le chemin du fichier :

```bash
python email_extractor.py --file "chemin/vers/le/fichier.txt"
```

Cela extraira les adresses email présentes dans le fichier texte.

### Options disponibles

- `--url <url>` : URL du site web à partir duquel les emails seront extraits.
- `--file <chemin_du_fichier>` : Chemin vers un fichier texte pour extraire les emails.

### Exemple d'exécution :

**Depuis une URL** :
```bash
python email_extractor.py --url "https://example.com"
```

**Depuis un fichier** :
```bash
python email_extractor.py --file "texte_emails.txt"
```

## Validation des chemins de fichiers

Le script vérifie que le chemin du fichier passé en argument existe, est un fichier valide et est accessible en lecture. Si le fichier ne peut pas être ouvert ou si le chemin est incorrect, une erreur détaillée sera affichée.

## Contribuer

Si tu souhaites contribuer à **Email Extractor**, voici les étapes à suivre :

1. Fork ce dépôt.
2. Crée une nouvelle branche (`git checkout -b ma-nouvelle-fonctionnalité`).
3. Apporte tes modifications.
4. Commit tes changements (`git commit -am 'Ajout de la fonctionnalité X'`).
5. Pousse tes modifications (`git push origin ma-nouvelle-fonctionnalité`).
6. Ouvre une pull request pour fusionner tes changements avec le dépôt principal.

## Licence

Ce projet est sous licence MIT - consulte le fichier [LICENSE](LICENSE) pour plus de détails.

## Contact

Si tu as des questions, des suggestions ou des problèmes, n'hésite pas à ouvrir une issue sur le dépôt GitHub ou à me contacter directement.
