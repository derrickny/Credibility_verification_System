from django.db import models

class PercentField(models.DecimalField):
    def get_prep_value(self, value):
        if value is None:
            return None
        else:
            return value / 100.0

    def set_prep_value(self, value):
        if value is None:
            return None
        else:
            return value * 100.0