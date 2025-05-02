# mailgrab
**mailgrab** est un outil Python permettant d'extraire des adresses email à partir de pages web ou de fichiers texte. Il utilise les expressions régulières pour identifier et extraire les emails, et Playwright pour le scraping web. Ce projet est idéal pour récupérer des adresses email à partir de différentes sources.

## Fonctionnalités

- Extrait des adresses email à partir d'une URL de site web ou d'un fichier texte.
- Utilisation de Playwright pour l'extraction de contenu de pages web avec gestion des erreurs.
- Recherche d'emails via des expressions régulières.
- Interface en ligne de commande simple à utiliser.
- Support pour l'extraction unique ou multiple (selon le nombre d'emails trouvés).

## Installation

Avant d'utiliser **mailgrab**, assure-toi que Python 3.x est installé sur ta machine.

### Étapes d'installation :

1. **Cloner le dépôt** :

    ```bash
    git clone https://github.com/nanaelie/mailgrab.git
    ```

2. **Installer les dépendances** et installer globalement :

   Accède au répertoire du projet et installe les dépendances nécessaires :

   ```bash
   cd mailgrab
   pip install .
   ```

   > **Remarque** : Assurez-vous que Playwright est correctement installé. Vous pourriez également avoir besoin de télécharger les navigateurs utilisés par Playwright avec cette commande :

   ```bash
   python -m playwright install
   ```

## Utilisation

**mailgrab** fonctionne en ligne de commande et accepte deux types d'entrées : une URL de site web ou un chemin vers un fichier texte.

### Extraire des emails depuis une URL

Si tu souhaites extraire des emails d'une page web, utilise la commande `mailgrab` et fournis l'URL du site :

```bash
mailgrab --url "https://example.com"
```

Cela extraira les adresses email présentes sur la page web à l'URL spécifiée.

### Extraire des emails depuis un fichier texte

Pour extraire des emails à partir d'un fichier texte, utilise l'option `--file` et fournis le chemin du fichier :

```bash
mailgrab --file "chemin/vers/le/fichier.txt"
```

Cela extraira les adresses email présentes dans le fichier texte.

### Options disponibles

* `--url <url>` : URL du site web à partir duquel les emails seront extraits.
* `--file <chemin_du_fichier>` : Chemin vers un fichier texte pour extraire les emails.

### Exemple d'exécution :

**Depuis une URL** :

```bash
mailgrab --url "https://example.com"
```

**Depuis un fichier** :

```bash
mailgrab --file "texte_emails.txt"
```

## Validation des chemins de fichiers

Le script vérifie que le chemin du fichier passé en argument existe, est un fichier valide et est accessible en lecture. Si le fichier ne peut pas être ouvert ou si le chemin est incorrect, une erreur détaillée sera affichée.

## Contribuer

Si tu souhaites contribuer à **mailgrab**, voici les étapes à suivre :

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
