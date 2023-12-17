from django.http import HttpResponse
from django.shortcuts import render


def list_singers():
    singers = [
        {'id': 1, "name": "Океан Ельзи"},
        {'id': 2, "name": "Бумбокс"}
    ]
    return singers


def popular_singers(request):
    html_content = """
    <h1>Popular singers of Ukraine</h1>
    <ul>
    """
    for singer in list_singers():
        html_content += f"<li><strong>{singer['name']}</strong></li>"
    html_content += """</ul>"""

    return HttpResponse(html_content, content_type='text/html;charset=utf-8')


def singer_card(request):
    singer_id = request.GET.get('id')
    singer_id = int(singer_id)
    singers = list_singers()
    singer = next((s for s in singers if s['id'] == singer_id), None)

    html_content = f"""
    <html>
    <body>
    <h1>{singer['name']}</h1>
    </body>
    </html>
    """
    return HttpResponse(html_content, content_type='text/html;charset=utf-8')
