from random import sample
from django.shortcuts import render
from string import ascii_uppercase
from .board import Board

def board(request):
	#build board
	tiles = []
	board = Board(4)
	board.find_words()
	words = board.words
	filtered_words = []
	for i, word in enumerate(words):
		if len(word) >= 3 and len(word) <= 15:
			filtered_words.append(word)
	for row in board.grid:
		tiles.extend([tile.letter for tile in row])


	return render(request, 'bog/bog.html', {'tiles':tiles, 'words':filtered_words})