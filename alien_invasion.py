import sys

import pygame

from settings import Settings

from ship import Ships


class AlienInvasion:
	"""管理游戏资源和行为的类"""
	
	def __init__(self):
		"""初始化游戏并创建游戏资源"""
		pygame.init()  # 初始化背景设置
		self.settings = Settings()
		
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height)
		)
		pygame.display.set_caption("Alien Invasion")  # 屏幕上显示的主要内容
		
		self.ship = Ships(self)
	
	def run_game(self):
		"""开始游戏的主循环"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()
	
	def _check_events(self):
		# 监视键盘和鼠标时间
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
				
	def _check_keydown_events(self, event):
		if event.key == pygame.K_d:
			self.ship.moving_right = True
		if event.key == pygame.K_w:
			self.ship.moving_up = True
		if event.key == pygame.K_a:
			self.ship.moving_left = True  	# 使用四个if同时判断两个条件，保证同时按下左右方向键飞船原地不动
		if event.key == pygame.K_s:
			self.ship.moving_down = True
		elif event.key == pygame.K_ESCAPE:
			sys.exit()
		
	def _check_keyup_events(self, event):
		if event.key == pygame.K_d:
			self.ship.moving_right = False
		elif event.key == pygame.K_w:
			self.ship.moving_up = False
		elif event.key == pygame.K_a:
			self.ship.moving_left = False
		elif event.key == pygame.K_s:
			self.ship.moving_down = False  	# 此处使用elif只需判断一个条件，长按方向键并松开只需一次判断即可
			
	def _update_screen(self):
		# 每次循环时都重绘屏幕。
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		# 让最近绘制的屏幕可见
		pygame.display.flip()


if __name__ == '__main__':  # 当作为主程序运行时执行游戏，通过其他方式导入便不会执行
	# 创建游戏实例并运行游戏
	ai = AlienInvasion()	 # 创建一个实例
	ai.run_game()
