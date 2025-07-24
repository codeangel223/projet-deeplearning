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
git clone https://github.com/codeangel223/projet-deeplearning.git
cd projet-deeplearning
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

## Launch Exo1 with Gradio

```bash
python src/exo1/__main__.py # or python src/exo2/__main__.py pour demarrer Exo2
```

---

[https://model-parasited-uninfected.onrender.com/](Exo1 - Parasited | Uninfected)

[https://cats-dog-classification.onrender.com/](Exo2 - Cat | Dog)

Jean Fabrice 🤝 Moussa
