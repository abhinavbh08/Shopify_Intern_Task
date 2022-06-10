from app.items.models import Item
from .items.service import ItemService
from .warehouses.service import WareHouseService

warehouse_service = WareHouseService()
item_service = ItemService()
