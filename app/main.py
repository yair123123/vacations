from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema

from app.db.database import init_db, fill_db
from app.gql.mutation import Mutations
from app.gql.query import Query

app =Flask(__name__)
schema = Schema(query=Query,mutation=Mutations)

app.add_url_rule(
   '/graphql',
   view_func=GraphQLView.as_view(
       'graphql',
       schema=schema,
       graphiql=True
   )
)
if __name__ == '__main__':
    init_db()
    fill_db()
    app.run()