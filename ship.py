import pygame

from settings import Settings


class Ships:
	""""管理飞船的类"""
	
	def __init__(self, ai_game):
		"""初始化飞船并设置其初始位置"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()	 # 获取屏幕矩形的坐标值
		
		# 移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images\ship.bmp')
		self.rec = self.image.get_rect()
		
		# 对于每艘新飞船，都将其放在屏幕底部的中央
		self.rec.midbottom = self.screen_rect.midbottom
		
		# 在飞船的属性x中存储小数值
		self.x = float(self.rec.x)
		self.y = float(self.rec.y)
		
	def update(self):
		"""根据移动标志调整飞船的位置"""
		# 更新飞船而不是rect对象的x值
		if self.moving_right and self.rec.right < self.screen_rect.right:	 # 限制飞船移动范围
			self.x += self.settings.ship_speed
		if self.moving_left and self.rec.left > 0:
			self.x -= self.settings.ship_speed
		if self.moving_up and self.rec.top > 0:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rec.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed
			
		# 根据self.x更新rect对象
		self.rec.x = self.x
		self.rec.y = self.y 	# 必须返回坐标值，不然飞船不会变化
	
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rec)
	