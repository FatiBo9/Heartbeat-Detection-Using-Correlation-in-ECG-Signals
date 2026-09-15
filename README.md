---

## 7. Dépôt : `Détection des battements cardiaques par corrélation des signaux ECG`

```markdown
# 🫀 Détection Automatique de Battements Cardiaques (ECG)

## 📌 Présentation
Projet de traitement avancé du signal biomédical axé sur la détection automatique du complexe QRS et des battements cardiaques au sein d'un signal électrocardiogramme (ECG). L'approche repose sur l'algorithme de corrélation croisée avec un motif modèle, suivi d'une analyse de robustesse face à différents niveaux de bruit synthétique et réel.

## 🚀 Fonctionnalités
- Filtrage numérique et débruitage des signaux ECG temporels.
- Calcul de corrélation croisée et détection dynamique des pics R.
- Évaluation de la précision de détection sous dégradation du rapport signal/bruit (SNR).
- Visualisation interactive des signaux et des temps d'inter-battements (RR).

## 🛠️ Technologies & Outils
- **Langage :** Python
- **Traitement du Signal :** SciPy (signal module), NumPy
- **Visualisation :** Matplotlib, Seaborn

## ⚙️ Installation & Lancement

```bash
# 1. Cloner le dépôt
git clone [https://github.com/FatiBo9/D-tection-des-battements-cardiaques-par-corr-lation-des-signaux-ECG.git](https://github.com/FatiBo9/D-tection-des-battements-cardiaques-par-corr-lation-des-signaux-ECG.git)
cd D-tection-des-battements-cardiaques-par-corr-lation-des-signaux-ECG

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Exécuter le script principal
SP4.py