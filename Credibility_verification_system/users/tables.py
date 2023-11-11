import django_tables2 as tables
from .models import Statement, Verdict

class StatementTable(tables.Table):
    created_at = tables.DateTimeColumn(format="F d, Y H:i A", verbose_name="Created At")

    class Meta:
        model = Statement
        template_name = "django_tables2/bootstrap4.html"

class VerdictTable(tables.Table):
    predicted_probability = tables.Column(verbose_name="Predicted Probability (%)")

    class Meta:
        model = Verdict
        template_name = "django_tables2/bootstrap4.html"
