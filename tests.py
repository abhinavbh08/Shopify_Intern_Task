import unittest
from config import Config
from app import create_app, db
from app.services import item_service, warehouse_service

class ItemWareHouse(unittest.TestCase):

    def setUp(self):
        self.app = create_app(Config)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_item_add(self):
        item_dkt = {"item_id":"1234", "item_name":"Oranges"}
        item_service.add(**item_dkt)
        ret_item = item_service.get_by_id(item_dkt["item_id"])
        self.assertEqual(item_dkt["item_id"], ret_item.item_id)

    def test_delete_item(self):
        item_dkt = {"item_id":"1234", "item_name":"Oranges"}
        item_service.add(**item_dkt)
        item_service.delete(item_dkt["item_id"])
        ret_item = item_service.get_by_id(item_dkt["item_id"])
        self.assertEqual(ret_item, None)

    def test_update_item(self):
        item_dkt = {"item_id":"1234", "item_name":"Oranges"}
        item_service.add(**item_dkt)
        item_service.update(item_service.get_by_id(item_dkt["item_id"]), **{"item_name":"Apples"})
        ret_item = item_service.get_by_id(item_dkt["item_id"])
        self.assertEqual(ret_item.item_name, "Apples")

    def test_warehouse_add(self):
        wh_dkt = {"name": "Warehouse1", "location": "Berlin"}
        warehouse_service.add(**wh_dkt)
        ret_wh = warehouse_service.get_by_id(1)
        self.assertEqual(wh_dkt["name"], ret_wh.name)
        self.assertEqual(wh_dkt["location"], ret_wh.location)

    def test_item_warehouse(self):
        item_dkt = {"item_id":"1234", "item_name":"Oranges"}
        wh_dkt = {"name": "Warehouse1", "location": "Berlin"}
        item_service.add(**item_dkt)
        warehouse_service.add(**wh_dkt)
        item_service.add_warehouse(item_service.get_by_id(item_dkt["item_id"]), item_dkt["item_id"], 1, 12)
        item, lst = item_service.view_warehouses_for_item(item_dkt["item_id"])
        wh, cnt = list(lst)[0]
        self.assertEqual(cnt, 12)
        self.assertEqual(wh.name, wh_dkt["name"])
        self.assertEqual(wh.location, wh_dkt["location"])

if __name__ == "__main__":
    unittest.main()