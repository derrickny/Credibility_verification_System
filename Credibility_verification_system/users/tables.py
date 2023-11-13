import django_tables2 as tables
from .models import Statement, Verdict

class StatementVerdictTable(tables.Table):
    statement = tables.Column(verbose_name="Statement")
    created_at = tables.DateTimeColumn(format="F d, Y H:i A", verbose_name="Created At")
    Statement_verdict = tables.Column(verbose_name="Statement Verdict")
    predicted_probability = tables.Column(verbose_name="Predicted Probability (%)")

    class Meta:
        model = Statement  # It doesn't matter which model you choose here since we are defining columns explicitly
        template_name = "django_tables2/bootstrap4.html"
