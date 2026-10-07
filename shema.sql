PRAGMA foreign_keys = ON;


CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    type TEXT CHECK(type IN ('depense', 'revenu')) NOT NULL,
    is_essential INT NOT NULL
);

DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    amount REAL,
    date TEXT,
    category_id INTEGER,
    type TEXT
);


INSERT OR IGNORE INTO categories (name, type, is_essential) VALUES
    ('Loyer', 'depense', 1),
    ('Salaire', 'revenu', 1),
    ('Alimentation', 'depense', 1),
    ('Shopping vetements', 'depense', 0),
    ('Loisir', 'depense', 0);

