from app import db


class Service:
    """Base class to encapsulate common database operations."""

    __model__ = None

    def add(self, **kwargs):
        """Adds an item to the database"""
        item = self.__model__(**kwargs)
        db.session.add(item)
        db.session.commit()

    def get_all(self):
        """Gets all the items from the database"""
        return self.__model__.query.all()

    def get_by_id(self, id):
        """Get item by id"""
        return self.__model__.query.filter_by(id=id).first()

    def update(self, obj, **kwargs):
        """Update an item in the database"""
        for k, v in kwargs.items():
            setattr(obj, k, v)
        db.session.add(obj)
        db.session.commit()
