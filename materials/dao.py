
from dao.base import BaseDAO
from materials.models import Materials


class MaterialsDAO(BaseDAO):
    model = Materials
