# import psycopg2

# class DB:
#     def __init__(self,dbname):
#         self.conn = psycopg2.connect(
#             dbname = dbname,
#             host = 'localhost',
#             port = 5432,
#             user = 'postgres',
#             password = '1977iyun'
#         )
#         self.curr = self.conn.cursor()
    
#     def products(self,table_name):
#         self.curr.execute(f"select *from {table_name}")
#         print(self.curr.fetchall())

#     def insert_func(self,table_name):
#         self.curr.execute(f'select *from {table_name}')
#         co{i[0]: i[1] for i in self.curr.description}
#         d = {}
#         for i, j in columns.items():
#             if i != 'id':
#                 if j == 23:
#                     a = int(input(f'{i} ni kiriting: '))
#                 else:
#                     a = input(f'{i} ni kiriting: ')
#                 d[i]=a
        # lumns = 
#         k = ','.join([f"{i}" for i, j in d.items()]) 
#         k_ = [j for i, j in d.items()]
    
#         self.curr.execute(f"insert into {table_name}({k}) values{tuple(k_)};")
#         print('Malumot qoshildi')
#         self.conn.commit()

# n67 = DB('postgres')
# n67.insert_func('person')
            



# import psycopg2
# from prettytable import PrettyTable 

# conn = psycopg2.connect(
#             dbname = 'postgres',
#             host = 'localhost',
#             port = 5432,
#             user = 'postgres',
#             password = '1977iyun'
#         )
# curr = conn.cursor()


# class Mijoz:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# m = Mijoz('Anvar',23)
        
# class Dori:
#     def __init__(self, nomi, narxi, firma):
#         self.nomi = nomi
#         self.narxi = narxi
#         self.firma = firma

#     def get_info(self):
#         return f"nomi:{self.nomi} narxi:{self.narxi} firma:{self.firma}"
    
# d = Dori('Noshpa',15600,23)

# class Dorixona:

#     def dorilar(self):
#         table = PrettyTable()
#         curr.execute(f"select *from dori")
#         fields = [i[0] for i in curr.description]
#         table.field_names = fields
#         table.add_rows([list(i) for i in curr.fetchall()])
#         print(table)

#     def detail(self,dori_nomi):
#         table = PrettyTable()
#         curr.execute(f"select *from dori where name = '{dori_nomi}'")
#         fields = [i[0] for i in curr.description]
#         table.field_names = fields
#         table.add_rows([list(i) for i in curr.fetchall()])
#         print(table)

#     def dori_qoshish(self):
#         name = input("Dori nomini kiriting :")
#         price = int(input("Dori narxini kiriting:"))
#         count = int(input("Dori sonini kiriting :"))
#         curr.execute(f"select *from dori where name = '{name}'")
#         dori = curr.fetchone()
#         if dori:
#             curr.execute(f"update dori set price = {price}, count = {dori[3]+ count} where name = '{name}'")
#         else :
#             curr.execute(f"insert into dori(name,price,count) values ('{name}',{price},{count})")

#         conn.commit()
#         print("dori qoshildi")


#     def sotish(self):
#         name = input("Ismingzini kiriting:")
#         curr.execute(f"select *from mijoz where name = '{name}'")
#         mijoz = curr.fetchone()
#         if mijoz:
#             dori_nomi = input("Dori nomini kiriting:")
#             curr.execute(f"select *from dori where name = '{dori_nomi}'")
#             dori = curr.fetchone()
#             if dori:
#                 print(f"{dori_nomi} dan {dori[3] } ta bor")
#                 dori_soni = int(input("Dori sonini kiriting:"))
#                 curr.execute(f"update dori set count = {dori[3] - dori_soni} where name = '{dori_nomi}'")
#                 conn.commit()
#                 curr.execute(f"insert into dorixona (user_id,dori_id,count,total_summ) values ({mijoz[0]},{dori[0]},{dori_soni},{dori_soni*dori[2]})")
#                 conn.commit()
#             else:
#                 print("Bunaqa dori mavjud emas")
        
#         else:
#             print("siz royxatdan otishingiz kerak")



#     def mijoz_qoshish(self):
#         name = input("Ism kiriting:")
#         age = int(input("Yoshingzini kiriting:"))
#         user_id = input("User kiriting  raqamlardan iborat 6 ta xonali")
#         mijoz = curr.fetchone()
#         if mijoz:
#             curr.execute(f"select *from mijoz where user_id = {user_id}")
#             print("siz royxatdan otgansz")
#             conn.commit()
#         else :
#             curr.execute(f"insert into mijoz(name,age,user_id) values ('{name}',{age},{user_id})")
#             print("Siz royxatdan otdingzi")
#             conn.commit()

#     def xarajatlar(self):

#         user_input = input("User id ingizni kiriting (6 xonali kod): ")
#         curr.execute(f"select id FROM mijoz where user_id = {user_input}")
#         mijoz = curr.fetchone()
#         if mijoz:
#             mijoz_id = mijoz[0]
#             curr.execute(f"select sum(total_summ) from dorixona where user_id = {mijoz_id}")
#             jami = curr.fetchone()

#             if jami:
#                 print(f"Umumiy xarajatingiz: {jami} so‘m")
#             else:
#                 print("Hech qanday xarajat topilmadi.")
#         else:
#             print("Bunday  mijoz topilmadi.")

        
# p = Dorixona()

# a = True
# while a:
#     d = int(input( " 0 chiqish \n 1 dorilar\n 2 dorini qidirish\n 3 dori qoshish \n 4 dori sotib olish\n 5 royxatdan otish \n 6 Xarajatlar \n Tepadan birini tanlang /n :"))
#     if d == 1:
#         p.dorilar()
#     elif d == 2:
#         dori_nomi = input("Dorini nomini kiriting:" )
#         p.detail(dori_nomi)
#     elif d == 3:
#         p.dori_qoshish()
#     elif d == 4 :
#         p.sotish()
#     elif d == 0:
#         a = False
#     elif d == 5:
#         p.mijoz_qoshish()
#     elif d == 6:
#         p.xarajatlar()
    
print('Git')