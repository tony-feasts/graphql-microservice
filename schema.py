import graphene
from resolvers import resolve_player_count, resolve_username_with_highest_game_id

# Define the Query class where you define fields
class Query(graphene.ObjectType):
    player_count = graphene.Int()
    username_with_highest_game_id = graphene.String()

    # Link resolvers to fields in the schema
    def resolve_player_count(self, info):
        return resolve_player_count(self, info)

    def resolve_username_with_highest_game_id(self, info):
        return resolve_username_with_highest_game_id(self, info)

# Create the GraphQL schema
schema = graphene.Schema(query=Query)
