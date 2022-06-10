from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Optional
from ..models import Item, WareHouse


class ItemForm(FlaskForm):
    """Form for taking an item as input"""

    item_id = StringField("Item ID", validators=[DataRequired()])
    item_name = StringField("Item Name", validators=[DataRequired()])
    item_type = StringField("Item Type")
    item_price = DecimalField("Item Price", validators=[Optional()])
    item_description = StringField("Item Description")
    submit = SubmitField("Submit")

    def validate_item_id(self, item_id):
        """Check if the item id does not already exists"""
        item = Item.query.filter_by(item_id=item_id.data).first()
        if item is not None:
            raise ValidationError(
                "Please use a different item id. This one already exists."
            )


class ItemUpdateForm(FlaskForm):
    """Form for updating an item."""

    item_id = StringField("Item ID", render_kw={"disabled": ""})
    item_name = StringField("Item Name", validators=[DataRequired()])
    item_type = StringField("Item Type")
    item_price = DecimalField("Item Price", validators=[Optional()])
    item_description = StringField("Item Description")
    submit = SubmitField("Submit")


class ItemToWareHouseForm(FlaskForm):
    """Form for adding an item to a warehouse"""

    item_id = StringField("Item ID", render_kw={"disabled": ""})
    item_name = StringField("Item Name", render_kw={"disabled": ""})
    item_type = StringField("Item Type", render_kw={"disabled": ""})
    item_price = DecimalField("Item Price", render_kw={"disabled": ""})
    item_description = StringField("Item Description", render_kw={"disabled": ""})
    category = SelectField("Warehouse", validators=[DataRequired()])
    count_of_item = IntegerField("Count of Item", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(ItemToWareHouseForm, self).__init__(*args, **kwargs)
        self.category.choices = [
            (w.id, w.name + ", " + w.location) for w in WareHouse.query.all()
        ]
