from  sqlite4  import  SQLite4

# Init database object, singleton pattern restricts multiple objects per db
database = SQLite4("database.db")
# Connect to db and creates execution thread
database.connect()

database.create_table("test", ["foo", "bar"])
database.insert("test", {"foo": "foo", "bar": "bar"})
# update
database.update("test", {"foo": "fooo", "bar": "baar"}, "1 = 1")

req = database.select("test", columns=['foo'], condition='foo = "fooo"')

print(req)