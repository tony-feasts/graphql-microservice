from db import get_connection

def resolve_player_count(self, info):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) AS player_count FROM userStats;")
    result = cursor.fetchone()
    connection.close()
    return result[0]  # Return the player count


# Resolver for username_with_highest_game_id query
def resolve_username_with_highest_game_id(self, info):
    connection = get_connection()
    cursor = connection.cursor()

    # SQL query to get the row with max game_id from rouletteStats and blackjackStats
    cursor.execute("""
    WITH blackjack_max AS (
    SELECT game_id, username
    FROM blackjackStats
    WHERE game_id = (SELECT MAX(game_id) FROM blackjackStats)
),
roulette_max AS (
    SELECT game_id, username
    FROM rouletteStats
    WHERE game_id = (SELECT MAX(game_id) FROM rouletteStats)
),
combined_max AS (
    SELECT *
    FROM blackjack_max
    UNION ALL
    SELECT *
    FROM roulette_max
)
SELECT username
FROM combined_max
WHERE game_id = (SELECT MAX(game_id) FROM combined_max);
    """)
    result = cursor.fetchone()
    connection.close()
    return result[0]  # Return the username with the highest game_id