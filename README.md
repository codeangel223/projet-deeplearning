Voici un doc complet et simple pour démarrer, avec les étapes de clonage, création et activation d’un environnement virtuel, puis installation des dépendances :

````markdown
# Get started

## Télécharger les datasets dans `/data`

```bash
|- data
|---- cats_dogs/
|--------- *.jpg
|---- cell_images/
|---------- Parasitized/
|---------------- *.jpg
|---------- Uninfected/
|---------------- *.jpg
```
````

---

## Étapes pour démarrer

1. **Cloner le dépôt**

```bash
git clone https://votre-repo-git-url.git
cd votre-repo-git-url
```

2. **Créer un environnement virtuel**

```bash
python3 -m venv venv
```

3. **Activer l’environnement virtuel**

- Sous Linux/macOS :

```bash
source venv/bin/activate
```

- Sous Windows (PowerShell) :

```powershell
.\venv\Scripts\Activate.ps1
```

- Sous Windows (cmd) :

```cmd
venv\Scripts\activate.bat
```

4. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

## Launch Exo1 with streamlit

```bash
streamlit run src/exo1/__main__.py
```

---

[https://model-parasited-uninfected.onrender.com/](Exo1 - Parasited | Uninfected)

[https://cats-dog-classification.onrender.com/](Exo2 - Cat | Dog)

Jean Fabrice 🤝 Moussa
