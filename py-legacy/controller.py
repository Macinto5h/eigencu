"""
controller.py

Version 0.1

By: M.J. Camara

Class that contains constants that are frequently used throughout the program. Used by controllers as an abstract class.
"""

class Controller:
	"""
	Constants frequently used throughout the program
	"""
	IMAGE_WIDTH = 178
	IMAGE_HEIGHT = 178
	FACE_CLASS_THRESHOLD = 6 * (10 ** 3)
	FACE_SPACE_THRESHOLD = 8 * (10 ** 3)
	FACE_NUMBER = 35
