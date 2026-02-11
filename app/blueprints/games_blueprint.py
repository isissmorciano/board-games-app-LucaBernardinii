from flask import Blueprint, render_template, request, redirect, url_for
from app.repository.games_repository import GamesRepository
from app.models import Game

games_bp = Blueprint('games', __name__)
repo = GamesRepository()

@games_bp.route('/')
def index():
    games = repo.get_all()
    return render_template('index.html', games=games)

@games_bp.route('/add', methods=['POST'])
def add_game():
    title = request.form.get('title')
    genre = request.form.get('genre')
    year = request.form.get('year')
    players = request.form.get('players')
    
    game = Game(title, genre, year, players)
    repo.add(game)
    
    return redirect(url_for('games.index'))