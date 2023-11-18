from dao.base import BaseDAO

from quesions.models import Questions


class QuestionsDAO(BaseDAO):
    model = Questions