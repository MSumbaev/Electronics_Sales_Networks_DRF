from rest_framework.exceptions import ValidationError


class DebtChangeValidator:
    """Валидатор на запрет изменения задолженности 'debt'"""
    def __init__(self, debt):
        self.debt = debt

    def __call__(self, value):
        debt = dict(value).get(self.debt)

        if debt is None:
            return
        elif debt:
            raise ValidationError('Для изменения поля debt(задолженность) обратитесь к администратору!')
