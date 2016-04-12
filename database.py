import sqlite3

class Database:

    db = None


    def __init__(self, db):
        self.db = sqlite3.connect(db)
        self.cur = self.db.cursor()
        def dict_factory(cursor, row):
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d
        self.db.row_factory = dict_factory


    def add_product(self, p_name, p_buy, p_sell, p_active):
        self.cur.execute(
                'insert into products (name,buy,sell,active) values(?,?,?,?)',
                p_name, p_buy, p_sell, p_active)
        p_id = self.cur.lastrowid
        self.db.commit()
        return p_id


    def delete_product(self, p_id):
        pass


    def update_product(self, p_id, p_name=None, p_buy=None, p_sell=None,
            p_active=None):
        query = 'update products set '
        args = []
        if p_name is not None:
            query += 'name=? '
            args.append(p_name)
        if p_buy is not None:
            query += 'buy=? '
            args.append(p_buy)
        if p_sell is not None:
            query += 'sell=? '
            args.append(p_sell)
        if p_active is not None:
            query += 'active=? '
            args.append(p_active)

        query += 'where id=?'
        args.append(p_id)
        self.cur.execute(query, *args)
        self.db.commit()


    def get_products(self, p_filter):
        query = 'select * from products where '
        args = []
        for key, value in p_filter.items():
            query += key + '=? and '
            args.append(value)
        if len(p_filter.keys()) > 0:
            query = query[:-4]
        else:
            query = query[:-7]
        self.cur.execute(query, *args)
        return self.cur.fetchall()
        self.cur.execute(query, *args)
        return self.cur.fetchall()


    def add_account(self, a_name):
        self.cur.execute('insert into accounts (name) values(?)', a_name)
        a_id = self.cur.lastrowid
        self.db.commit()
        return a_id

    def delete_account(self, a_id):
        # Should probably not be implemented
        pass

    def get_accounts(self, a_filter):
        query = 'select * from accounts where '
        args = []
        for key, value in a_filter.items():
            query += key + '=? and '
            args.append(value)
        if len(a_filter.keys()) > 0:
            query = query[:-4]
        else:
            query = query[:-7]
        self.cur.execute(query, *args)
        return self.cur.fetchall()
        self.cur.execute(query, *args)
        return self.cur.fetchall()

    def add_location(self, l_name):
        self.cur.execute('insert into locations (name) values(?)', p_name)
        l_id = self.cur.lastrowid
        self.db.commit()
        return l_id


    def delete_location(self, l_id):
        # Should probably not be iplemented
        pass

    def get_locations(self, l_filter):
        query = 'select * from locations where '
        args = []
        for key, value in l_filter.items():
            query += key + '=? and '
            args.append(value)
        if len(l_filter.keys()) > 0:
            query = query[:-4]
        else:
            query = query[:-7]
        self.cur.execute(query, *args)
        return self.cur.fetchall()
        self.cur.execute(query, *args)
        return self.cur.fetchall()


    def add_transaction(self, t_name, t_from, t_to, t_balance):
        self.cur.execute(
                'insert into transactions ' +\
                        '(name,datetime,from_id,to_id,balance) ' +\
                        'values(?,?,?,?,?)',
                        t_name,
                        datetime.now(),
                        t_from,
                        t_to,
                        t_balance)
        t_id = self.cur.lastrowid
        self.db.commit()
        return t_id


    def get_transactions(self, t_filter):
        query = 'select * from transactions where '
        args = []
        for key, value in t_filter.items():
            query += key + '=? and '
            args.append(value)
        if len(t_filter.keys()) > 0:
            query = query[:-4]
        else:
            query = query[:-7]
        self.cur.execute(query, *args)
        return self.cur.fetchall()

    def update_stock(self, p_id, l_id, amount):
        self.cur.execute('update stock set amount=? where product=? and location=?',
                amount, p_id, l_id)
        self.db.commit()


    def add_stock(self, p_id, l_id, amount):
        self.cur.execute('insert into stock (product,location,amount) values(?,?,?)',
                p_id, l_id, amount)
        self.db.commit()


    def get_stock(self, s_filter):
        self.cur.execute('select amount from stock where product=? and location=?',
                s_filter['p_id'], s_filter['l_id'])
        return self.cur.fetchall()


    def add_producttransaction(self, t_id, p_id, amount):
        self.cur.execute('insert into producttransactions (t_id,p_id,amount)' +\
                ' values(?,?,?)', t_id, p_id, amount)
        self.db.commit()


    def get_producttransactions(self, t_id):
        self.cur.execute(
                'select p_id,amount from producttransactions where t_id=?',
                t_id)
        return self.cur.fetchall()

