from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from ..models import WareHouse


class WareHouseForm(FlaskForm):
    """Form to add an warehouse."""

    name = StringField("Name of the Warehourse", validators=[DataRequired()])
    location = StringField("Location of the warehouse", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        wh = WareHouse.query.filter_by(
            name=self.name.data, location=self.location.data
        ).first()
        if wh is not None:
            self.name.errors.append("This warehouse already exists at that location")
            return False

        return True
