from django.http import HttpResponse
from django.shortcuts import render


def information(request):
    html_content = """
    <html>
    <body>
    <h2>My information</h2>
    <table>
        <tr>
             <td>Name:</td>
            <td>Nazar</td>
        </tr>
        <tr>
            <td>Age:</td>
            <td>18</td>
        </tr>
        <tr>
            <td>Location:</td>
            <td>Ukrainge</td>
        </tr>
    </table>
    </body>
    </html>
    """
    return HttpResponse(html_content, content_type='text/html;charset=utf-8')
