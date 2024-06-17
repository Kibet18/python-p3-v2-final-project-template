from models.__init__ import CURSOR, CONN

class Brand:
    # Dictionary to keep track of all Brand instances created.
    all = {}

    def __init__(self, brand_name, brand_id=None):
        self.brand_id = brand_id
        self.brand_name = brand_name

    def __repr__(self):
        return f"<Brand {self.brand_id}: Name='{self.brand_name}'>"

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        # Ensure brand_name is a non-empty string
        if isinstance(brand_name, str) and len(brand_name):
            self._brand_name = brand_name
        else:
            raise ValueError("Brand name must be a non-empty string")

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Brand instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS brands (
                brand_id INTEGER PRIMARY KEY,
                brand_name TEXT UNIQUE
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Brand instances"""
        sql = """
            DROP TABLE IF EXISTS brands;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the brand details into the brands table"""
        sql = """
            INSERT INTO brands (brand_name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.brand_name,))
        CONN.commit()

        self.brand_id = CURSOR.lastrowid
        type(self).all[self.brand_id] = self

    def update(self):
        """Update the table row corresponding to the current Brand instance"""
        sql = """
            UPDATE brands
            SET brand_name = ?
            WHERE brand_id = ?
        """
        CURSOR.execute(sql, (self.brand_name, self.brand_id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Brand instance,
        delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM brands
            WHERE brand_id = ?
        """
        CURSOR.execute(sql, (self.brand_id,))
        CONN.commit()

        # Delete the dictionary entry using brand_id as the key
        del type(self).all[self.brand_id]

        # Set the brand_id to None
        self.brand_id = None

    @classmethod
    def create(cls, brand_name):
        """Initialize a new Brand instance and save the object to the database"""
        brand = cls(brand_name)
        brand.save()
        return brand

    @classmethod
    def instance_from_db(cls, row):
        """Return a Brand object having the attribute values from the table row."""
        # Check the dictionary for an existing instance using the row's primary key
        brand = cls.all.get(row[0])
        if brand:
            # Ensure attributes match row values in case local instance was modified
            brand.brand_name = row[1]
        else:
            # Not in dictionary, create new instance and add to dictionary
            brand = cls(row[1])
            brand.brand_id = row[0]
            cls.all[brand.brand_id] = brand
        return brand

    @classmethod
    def get_all(cls):
        """Return a list containing all Brand objects from the database"""
        sql = """
            SELECT *
            FROM brands
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, brand_name):
        """Return a Brand object corresponding to the brand_name"""
        sql = """
            SELECT *
            FROM brands
            WHERE brand_name = ?
        """
        row = CURSOR.execute(sql, (brand_name,)).fetchone()
        return cls.instance_from_db(row) if row else None
