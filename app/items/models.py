from app import db


class Item(db.Model):
    """Table for an item"""

    __tablename__ = "items"
    
    item_id = db.Column(db.String, unique=True, primary_key=True)
    item_name = db.Column(db.String(64), index=True, nullable=False)
    item_type = db.Column(db.String(64), index=True)
    item_price = db.Column(db.Float)
    item_description = db.Column(db.String(128))

    warehouses = db.relationship(
        "ItemWareHouseAssociation", back_populates="item", lazy="dynamic"
    )

    def __repr__(self):
        return str(self.item_name)


class ItemWareHouseAssociation(db.Model):
    """Table for item and warehouse association"""

    __tablename__ = "items_warehouses"
    
    item_id = db.Column(db.Integer, db.ForeignKey("items.item_id"), primary_key=True)
    warehouse_id = db.Column(
        db.Integer, db.ForeignKey("warehouses.id"), primary_key=True
    )
    quantity = db.Column(db.Integer, nullable=False)

    warehouse = db.relationship("WareHouse", back_populates="items")
    item = db.relationship("Item", back_populates="warehouses")
