from django.db.backends.sqlite3.base import SqliteDatabaseWrapper


class SqliteWithBusyTimeout(SqliteDatabaseWrapper):
    def _cursor(self):
        cursor = super()._cursor()
        cursor.execute("PRAGMA busy_timeout = 5000")
        return cursor
