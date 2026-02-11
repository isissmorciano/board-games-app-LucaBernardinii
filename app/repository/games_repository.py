import sqlite3
from app.models import Game

class GamesRepository:
    def __init__(self, db_path='instance/board_games.sqlite'):
        self.db_path = db_path
    
    def get_all(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM giochi')
        rows = cursor.fetchall()
        conn.close()
        
        games = [Game(row[1], row[2], row[3], row[4], row[0]) for row in rows]
        return games
    
    def add(self, game):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO giochi (nome, categoria, durata_media, numero_giocatori_massimo) VALUES (?, ?, ?, ?)',
                      (game.title, game.genre, game.year, game.players))
        conn.commit()
        conn.close()