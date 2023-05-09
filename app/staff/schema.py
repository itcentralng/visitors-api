from app import db
from app import ma

class StaffSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Staff