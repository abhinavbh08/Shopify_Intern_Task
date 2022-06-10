from ..models import WareHouse
from ..core import Service


class WareHouseService(Service):
    """Service class for warehouse functionality."""

    __model__ = WareHouse

    def add(self, **kwargs):
        """Adds an item to the database"""
        item = self.__model__.query.filter_by(name=kwargs["name"], location=kwargs["location"]).first()
        if item:
            raise Exception("Warehouse already exists at this location.")
        super().add(**kwargs)

    def view_items_in_warehouse(self, wh_id):
        """View all the items present in a warehouse."""
        wh = self.get_by_id(wh_id)
        item_list = []
        count_list = []
        items = wh.items.all()
        for it in items:
            item_list.append(it.item)
            count_list.append(it.quantity)
        return wh, zip(item_list, count_list)