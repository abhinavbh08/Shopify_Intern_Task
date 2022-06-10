from app import db
from ..models import Item, ItemWareHouseAssociation, WareHouse
from ..core import Service


class ItemService(Service):
    """Service class for handling items."""

    __model__ = Item

    def get_by_id(self, id):
        return Item.query.filter_by(item_id=id).first()

    def delete(self, id):
        """Delete an item"""
        item = Item.query.filter_by(item_id=id).first()
        for assoc in item.warehouses.all():
            db.session.delete(assoc)
        db.session.delete(item)
        db.session.commit()

    def add_warehouse(self, item, item_id, warehouse_id, count_data):
        """Add item to an warehouse"""
        assoc = ItemWareHouseAssociation.query.filter_by(
            item_id=item_id, warehouse_id=warehouse_id
        ).first()
        if assoc:
            raise Exception("This item and warehouse combination already exists.")
        wh = WareHouse.query.filter_by(id=warehouse_id).first()
        i_wh_assc = ItemWareHouseAssociation(
            item=item, warehouse=wh, quantity=count_data
        )
        db.session.add(i_wh_assc)
        db.session.commit()

    def view_warehouses_for_item(self, item_id):
        """View warehouses where an item is present."""
        item = self.get_by_id(item_id)
        warehouse_list = []
        count_list = []
        warehouses = item.warehouses.all()
        for wh in warehouses:
            warehouse_list.append(wh.warehouse)
            count_list.append(wh.quantity)
        return item, zip(warehouse_list, count_list)
