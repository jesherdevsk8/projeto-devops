# restapi-flask

## Development commands

- **create user**
```bash
curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d '{
            "first_name": "Jesher Minelli",
            "last_name": "Alves",
            "cpf": "641.396.500-28",
            "email": "jesherdevsk8@gmail.com",
            "birth_date": "1994-06-08"
         }'
```

- **get users**
```bash
curl http://127.0.0.1:5000/users -I
```

- **get specific user**
```bash
curl -X GET "http://127.0.0.1:5000/users?cpf=641.396.500-28&email="
curl -X GET "http://127.0.0.1:5000/users?cpf=&email=jesherdevsk8@gmail.com"
curl -X GET "http://127.0.0.1:5000/users?cpf=641.396.500-28&email=jesherdevsk8@gmail.com"
```

## MongoDB commands
```bash
mongo -u admin -p admin
show dbs
use users
show collections
db.user_model.find()
db.user_model.find({email: 'jesherdevsk8@gmail.com'})
db.user_model.insertOne({cpf: '006.461.230-92', first_name: 'José', last_name: 'Valim', email: 'josevalim@test.com', birth_date: '1988-01-01'})
db.user_model.updateOne({email: 'josevalim@test.com'}, { $set: { email: 'jose@valim.me' } })
db.user_model.deleteOne({email: 'jose@valim.me'})
quit()
```