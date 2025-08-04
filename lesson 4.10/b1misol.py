import psycopg2
from prettytable import PrettyTable

conn = psycopg2.connect(
    dbname='imtixon',
    host='localhost',
    port=5432,
    user='postgres',
    password='1977iyun'
)
curr = conn.cursor()


class Kutubxona:

    def barcha_kitoblar(self):
        table = PrettyTable()
        curr.execute(f"select books.id, title, full_name as author, published_year from books join authors on books.author_id = authors.id")
        fields = [i[0] for i in curr.description]
        table.field_names = fields
        table.add_rows(curr.fetchall())
        print(table)

    def kitob_qidirish(self):
        title = input("Kitob nomini kiriting: ")
        table = PrettyTable()
        curr.execute(f"select * from books where title = {title}")
        fields = [i[0] for i in curr.description]
        table.field_names = fields
        table.add_rows(curr.fetchall())
        print(table)

    def kitob_qoshish(self):
        title = input("Kitob nomi: ")
        author_id = int(input("Muallif ID: "))
        description = input("Kitob haqida: ")
        year = int(input("Nashr yili: "))
        genre_id = int(input("Janr ID: "))
        curr.execute(f"insert into books (title, author_id, description, published_year, genre_id) values {title}, {author_id}, {description}, {year}, {genre_id}")
        conn.commit()
        print("Kitob qoвЂshildi.")

    def muallif_qoshish(self):
        full_name = input("Muallif ismi: ")
        country = input("Muallif davlati: ")
        curr.execute(f"insert into authors (full_name, country) values  {full_name}, {country}")
        conn.commit()
        print("Muallif qoвЂshildi.")

    def janr_qoshish(self):
        name = input("Janr nomi: ")
        curr.execute(f"insert into genres (name) value {name}")
        conn.commit()
        print("Janr qoвЂshildi.")

    def izoh_qoldirish(self):
        user_id = int(input("Foydalanuvchi ID: "))
        book_id = int(input("Kitob ID: "))
        content = input("Izoh matni: ")
        curr.execute(f"INSERT INTO comments (user_id, book_id, content) VALUES {user_id}, {book_id}, {content}")
        conn.commit()
        print("Izoh qoldirildi.")

    def izohlar_korish(self):
        book_id = int(input("Kitob ID sini kiriting: "))
        table = PrettyTable()
        curr.execute(f"select comments.id, users.full_name, comments.content, comments.created_at from comments join users on comments.user_id = users.id where book_id = {book_id}")
        fields = [i[0] for i in curr.description]
        table.field_names = fields
        table.add_rows(curr.fetchall())
        print(table)


p = Kutubxona()
while True:
    print("""
    ========== NajotKutubxona ==========
    1. Barcha kitoblar
    2. Kitob qidirish
    3. Kitob qoвЂshish
    4. Muallif qoвЂshish
    5. Janr qoвЂshish
    6. Izoh qoldirish
    7. Kitobdagi izohlarni koвЂrish
    0. Chiqish
    """)
    d = input("Raqamlardan birini kiriting ")
    if d == "1":
        p.barcha_kitoblar()
    elif d == "2":
        p.kitob_qidirish()
    elif d == "3":
        p.kitob_qoshish()
    elif d == "4":
        p.muallif_qoshish()
    elif d == "5":
        p.janr_qoshish()
    elif d == "6":
        p.izoh_qoldirish()
    elif d == "7":
        p.izohlar_korish()
    elif d == "0":
        print("Dastur yakunlandi.")
        break


