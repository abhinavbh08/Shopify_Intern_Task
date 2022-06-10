from app import db


class WareHouse(db.Model):
    """Table for a warehouse."""

    __tablename__ = "warehouses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)

    items = db.relationship(
        "ItemWareHouseAssociation", back_populates="warehouse", lazy="dynamic"
    )

    def __repr__(self) -> str:
        return self.name + "," + self.location
