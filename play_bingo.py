import random

class NumberGame():

	num_players = 80
	num_bingos = 0
	rounds = 1

	bucket = range(1, 26)

	players = []

	def play(self):

		# setup the players
		self.set_up_players()

		for round in range(1, self.rounds + 1):
			print('ROUND START: {round}'.format(round=str(round)))
			print('------------------------------------------')

			# pick a number from the bucket
			number_picked = random.sample(self.bucket, 1)[0]
			print('Number: {num}'.format(num=number_picked))

			# remove number picke from bucket
			self.bucket.remove(number_picked)

 			print('Bucket Remaining:')
 			print(self.bucket)

			# players now check to see if the number chosen in in their picks
			self.player_check(number_picked)

		print('---- end of round ----')
		for player in self.players:
			print(player)

		print("Total Bingos: {total}".format(total=self.num_bingos))

	def player_check(self, number_picked):
		print('Players are now checking their "boards"')

		players_to_remove = []

		for player in self.players:

			print(player)

			# check to see if the number picked is on the players board
			if number_picked in player:

				# if it is chosen remove it from their board (cross it out)
				player.remove(number_picked)
				
			# If the player has had all their numbers picked, i.e. all crossed out
			# BINGO
			if not player:
				self.num_bingos = self.num_bingos + 1
				print('We have a BINGO - Num Bingos: {bingos}'.format(bingos=self.num_bingos))
				print('Player is no longer playing')
				players_to_remove.append(player)

		for player_to_remove in players_to_remove:
			self.players.remove(player_to_remove)

	def set_up_players(self):

		while self.num_players >= 1:
			# set up new player
			player = random.sample(range(1,26), 5)
			print(player)

			self.players.append(player)

			self.num_players = self.num_players - 1
		
		print(self.num_players)

if __name__ == '__main__':
	bingo_game = NumberGame()
	bingo_game.play()

