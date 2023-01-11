import pygame.font

class Button:

	def __init__(self, ai_game, msg):
		"""Initialise button attiributes."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions of the button.
		self.width, self.height = 200, 50
		self.button_colour = (0, 255, 0)
		self.text_colour = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Build the button's rect object and centre it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# The button needs to be prepped only once.
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turns message into a rendered image and centre on the button."""
		self.msg_image = self.font.render(msg, True, self.text_colour,
			self.button_colour)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		""" Draw blank button, then draw the message."""
		self.screen.fill(self.button_colour, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		