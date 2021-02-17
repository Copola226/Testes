"""
cursor.execute("
create table livro(titulo text, ano year);
")
"""
import sqlite3
conn = sqlite3.connect('Dados.db')
cursor = conn.cursor()

cursor.execute("""
delete from livro where ano = 1222;
""")
conn.commit()

for linha in cursor.execute("""
select * from livro order by ano;
"""):
    print(linha)
conn.close()
