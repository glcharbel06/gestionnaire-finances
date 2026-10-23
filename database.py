import sqlite3

def init_db():
    conn = sqlite3.connect("finance.db")
    with open("shema.sql", "r") as f:
        sql_script = f.read()

    conn.executescript(sql_script)
    conn.commit()
    conn.close()

def add_transaction(description, amount, date, category_id, type_transac):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO transactions (description, amount, date, category_id, type) VALUES (?, ?, ?, ?, ?)",
        (description, amount, date, category_id, type_transac)
    )

    conn.commit()
    conn.close()

def show_transaction():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()

    conn.close()
    return transactions

if __name__ == "__main__":
    init_db()
    add_transaction('loyer appartement', 600, "10/10/2026", 1, 'depense')
    add_transaction('salaire', 2800, '01/10/2026', 1, 'revenu')
    resultat = show_transaction()
    print("mes transactions :", resultat)

# intégration de la fonction qui se charge de faire la somme des dépenses par catégorie

def get_summary():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE category_id = 1")
    revenus = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE category_id = 2")
    D_fixe = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE category_id = 3")
    D_variable = cursor.fetchone()[0] or 0

    conn.close()
    return revenus, D_fixe, D_variable

revenus, D_fixe, D_variable = get_summary()
print("Revenus :", revenus)
print("Dépenses fixes :", D_fixe)
print("Dépenses variables :", D_variable)

def diagnose():
    revenus, d_fixe, d_variable = get_summary
    reste = revenus - d_fixe - d_variable
    ratio_fixe = (d_fixe / revenus) * 100
    if reste < 0:
        print("Alerte : situation de déficit !")
    elif ratio_fixe > 50:
        print("Alerte : charges fixes trop élevées (> 50 %) !")
    elif taux_epargne < 10:
        print("Recalibrage : capacité d'épargne faible (< 10 %) !")
    else:
        print("Optimisation : budget sain et bonne capacité d'épargne !")

diagnose()

