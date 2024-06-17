from models.__init__ import CURSOR, CONN
from models.brands import Brand  # Assuming Brand model is correctly defined in models/brands.py

class Products:
    # Constructor
    def __init__(self, brand_id, model, price, description, id=None):
        self.id = id
        self.brand_id = brand_id
        self.model = model
        self.price = price
        self.description = description

    def __repr__(self):
        return f"<Product {self.id}: Brand='{self.brand.brand_name}', Model='{self.model}', Price={self.price}, Description='{self.description}'>"

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, brand_id):
        if isinstance(brand_id, int) and brand_id > 0:
            self._brand_id = brand_id
        else:
            raise ValueError("Brand ID must be a positive integer")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if isinstance(model, str) and len(model) > 0:
            self._model = model
        else:
            raise ValueError("Model must be a non-empty string")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price >= 0:
            self._price = price
        else:
            raise ValueError("Price must be a non-negative number")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description) > 0:
            self._description = description
        else:
            raise ValueError("Description must be a non-empty string")

    @property
    def brand(self):
        return Brand.find_by_id(self.brand_id)

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, Brand):
            self._brand_id = brand.brand_id
        else:
            raise ValueError("Brand must be a valid Brand object")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                brand_id INTEGER,
                model TEXT,
                price REAL,
                description TEXT,
                FOREIGN KEY (brand_id) REFERENCES brands(brand_id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS products;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id is None:
            sql = """
                INSERT INTO products (brand_id, model, price, description)
                VALUES (?, ?, ?, ?)
            """
            CURSOR.execute(sql, (self.brand_id, self.model, self.price, self.description))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            self.update()

    def update(self):
        sql = """
            UPDATE products
            SET brand_id = ?, model = ?, price = ?, description = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.brand_id, self.model, self.price, self.description, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM products
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None

    @classmethod
    def create(cls, brand_id, model, price, description):
        product = cls(brand_id, model, price, description)
        product.save()
        return product

    @classmethod
    def instance_from_db(cls, row):
        product = cls(row[1], row[2], row[3], row[4])
        product.id = row[0]
        return product

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM products
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM products
            WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_brand(cls, brand_id):
        sql = """
            SELECT *
            FROM products
            WHERE brand_id = ?
        """
        CURSOR.execute(sql, (brand_id,))
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_price(cls, price):
        sql = """
            SELECT *
            FROM products
            WHERE price = ?
        """
        CURSOR.execute(sql, (price,))
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]

    def orders(self):
        from models.orders import Order
        sql = """
            SELECT * FROM orders
            WHERE product_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        return [Order.instance_from_db(row) for row in rows]
