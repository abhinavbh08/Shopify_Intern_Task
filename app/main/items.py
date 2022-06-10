from ..forms import (
    ItemForm,
    ItemUpdateForm,
    ItemToWareHouseForm,
)
from flask import request, Blueprint, abort
from flask import flash, redirect, render_template, url_for
from ..services import item_service

bp = Blueprint("items", __name__, template_folder="templates")


@bp.route("/")
@bp.route("/index")
def index():
    return render_template("index.html")


@bp.route("/add", methods=["GET", "POST"])
def add():
    """Add an item."""
    form = ItemForm()
    if form.validate_on_submit():
        item_service.add(
            item_id=form.item_id.data,
            item_name=form.item_name.data,
            item_type=form.item_type.data,
            item_price=form.item_price.data,
            item_description=form.item_description.data,
        )
        flash("Your item has been added.")
        return redirect(url_for("items.index"))
    return render_template("add_item.html", title="Add Item", form=form)


@bp.route("/view", methods=["GET"])
def view():
    """View all the items present in the database."""
    items = item_service.get_all()
    return render_template("view.html", items=items)


@bp.route("/delete_item/<item_id>", methods=["GET", "POST"])
def delete_item(item_id):
    """Delete an item."""
    item_service.delete(item_id)
    flash("Your item has been deleted")
    return redirect(url_for("items.view"))


@bp.route("/update_item/<item_id>", methods=["GET", "POST"])
def update_item(item_id):
    """Update an item"""
    form = ItemUpdateForm()
    item = item_service.get_by_id(item_id)
    if request.method == "GET":
        form.item_id.data = item.item_id
        form.item_name.data = item.item_name
        form.item_type.data = item.item_type
        form.item_price.data = item.item_price
        form.item_description.data = item.item_description
    if form.validate_on_submit():
        item_service.update(
            item,
            item_name=form.item_name.data,
            item_type=form.item_type.data,
            item_price=form.item_price.data,
            item_description=form.item_description.data,
        )
        flash("Your item has been updated.")
        return redirect(url_for("items.view"))
    return render_template("update_item.html", form=form)


@bp.route("/add_item_to_warehouse/<item_id>", methods=["GET", "POST"])
def add_item_to_warehouse(item_id):
    """Add an item to a warehouse along with its quantity."""
    form = ItemToWareHouseForm()
    item = item_service.get_by_id(item_id)
    if request.method == "GET":
        form.item_id.data = item.item_id
        form.item_name.data = item.item_name
        form.item_type.data = item.item_type
        form.item_price.data = item.item_price
        form.item_description.data = item.item_description
    if form.validate_on_submit():
        try:
            item_service.add_warehouse(
                item=item,
                item_id=item.item_id,
                warehouse_id=form.category.data,
                count_data=form.count_of_item.data,
            )
        except Exception as e:
            abort(409, e)
        return redirect(url_for("items.view"))
    return render_template("add_item_to_warehouse.html", form=form)


@bp.route("/view_warehouses_for_item/<item_id>", methods=["GET"])
def view_warehouses_for_item(item_id):
    """View warehouses where an item is present"""
    item, wh_cnt_data = item_service.view_warehouses_for_item(item_id)
    return render_template(
        "view_warehouses_for_item.html", item=item, warehouse_list=wh_cnt_data
    )
