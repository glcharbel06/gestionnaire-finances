Gestionnaire et moteur de décision financière

Outil d'analyse budgétaire et d'aide à la décision financière développé en Python et SQLite.
Plutôt que d'agir comme un simple enregistreur de dépenses passif, ce logiciel analyse la structure 
budgétaire d'un profil et propose des scénarios de rééquilibrage gradués :

Niveau 1 — Optimisation : situations saines, opportunités d'épargne.
Niveau 2 — Recalibrage : début de dérive sur les dépenses variables.
Niveau 3 — Alerte : déficit ou charges fixes trop élevées.

Stack technique
Langage : Python 3
Base de données : SQLite

Installation et exécution

Cloner le projet :
git clone https://github.com/glcharbel06/gestionnaire-finances.git
cd gestionnaire-finances

Initialiser la base et lancer le script :
python3 database.py

Feuille de route
- [x] Initialisation de la base SQLite et modélisation relationnelle
- [x] Gestion des transactions et catégorisation (Revenus, Charges obligatoires, Dépenses variables)
- [x] Calcul des agrégats mensuels (get_summary)
- [ ] Moteur de diagnostic et d'alertes (diagnose)