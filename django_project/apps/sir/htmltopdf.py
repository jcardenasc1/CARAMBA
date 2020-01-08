import cStringIO as StringIO
import ho.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape
from django.conf import settings
import os


def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    return path


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), dest=result, link_callback=fetch_resources)
    #pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), dest=result, link_callback=fetch_resources )
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had errors<pre>%s</pre>' % escape(html))


