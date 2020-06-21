from random import sample
from django.shortcuts import render
from string import ascii_uppercase
from .board import Board

def board(request):
	word_length_min = request.GET.get('minlength')
	word_length_max = request.GET.get('maxlength')
	word_max = request.GET.get('wordmax')

	try:
		word_length_min = int(word_length_min)
	except:
		word_length_min = 3
	try:
		word_length_max = int(word_length_max)
	except:
		word_length_max = 15
	try:
		word_max = int(word_max)
	except:
		word_max = 99999

	#build board
	
	tiles, filtered_words = get_board(word_length_min, word_length_max)
	while len(filtered_words) > word_max:
		tiles, filtered_words = get_board(word_length_min, word_length_max)

	return render(request, 'bog/bog.html', {'tiles':tiles, 'words':filtered_words})


#helper function should be in another file?
def get_board(word_length_min, word_length_max):
	tiles = []
	board = Board(4)
	board.find_words()
	words = board.words
	filtered_words = []
	for word in words:
		if len(word) >= word_length_min and len(word) <= word_length_max:
			filtered_words.append(word)
	for row in board.grid:
		tiles.extend([tile.letter for tile in row])
	return tiles, filtered_words