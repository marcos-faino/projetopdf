from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


class GeraPDFMixin:

    def render_to_pdf(self, template_end, context={}):
        template = get_template(template_end)
        html = template.render(context)
        result = BytesIO()
        try:
            pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
            return HttpResponse(result.getvalue(),
                                content_type='application/pdf')
        except IOError as e:
            print(e)
            return None
