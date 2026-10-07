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
