from ..forms import WareHouseForm
from flask import Blueprint, request
from flask import flash, redirect, render_template, url_for
from ..services import warehouse_service

bp = Blueprint(
    "warehouse", __name__, url_prefix="/warehouse", template_folder="templates"
)


@bp.route("/add_warehouse", methods=["GET", "POST"])
def add_warehouse():
    """Add a warehouse."""
    form = WareHouseForm()
    # if form.validate_on_submit():
    # Doing this due for replit compatibility.
    if request.method=="POST":   
        warehouse_service.add(name=form.name.data, location=form.location.data)
        flash("Your warehouse has been added.")
        return redirect(url_for("items.index"))
    return render_template("add_warehouse.html", title="Add Warehouse", form=form)


@bp.route("/view_warehouses", methods=["GET"])
def view_warehouses():
    """View list of warehouses."""
    warehouses = warehouse_service.get_all()
    return render_template("view_warehouses.html", warehouses=warehouses)


@bp.route("/view_items_in_warehouse/<wh_id>", methods=["GET"])
def view_items_in_warehouse(wh_id):
    """View items in a warehouse"""
    warehouse, item_cnt_data = warehouse_service.view_items_in_warehouse(wh_id)
    return render_template(
        "view_items_in_warehouse.html", warehouse=warehouse, item_list=item_cnt_data
    )
