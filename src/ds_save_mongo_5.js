use myDB
show dbs
show tables
db.myCollections.insert({"Persons":[{"id":"201511095","이름":"김지영"},{"id":"201511113","이름":"서창희"}]})
db.myCollections.find({"Persons.이름":"김지영"})