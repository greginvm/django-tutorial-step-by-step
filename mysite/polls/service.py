from django.db import connection


def dosomething(param):
    if False:
        return None

    cursor = connection.cursor()
    cursor.execute(
        "SELECT username FROM auth_user WHERE id=%s" % param)  # Noncompliant; Query is constructed based on user inputs
    row = cursor.fetchone()
