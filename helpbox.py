import pygame.font


class Helpbox():
    """显示帮助信息的类"""

    def __init__(self, ai_settings, screen):
        """初始化显示帮助涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        # 显示帮助信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('SimHei', 24)
        # 准备包含帮助的图像
        self.prep_help()

    def prep_help(self):
        """将帮助转换为一幅渲染的图像"""
        help_str = '左右键移动飞船，空格键发射子弹'
        # print(help_str)
        self.help_image = self.font.render(help_str, True, self.text_color,
                                           self.ai_settings.bg_color)
        # 将帮助放在屏幕右上角
        self.help_rect = self.help_image.get_rect()
        self.help_rect.left = 420
        self.help_rect.top = 520

    def show_help(self):
        """在屏幕上显示当前帮助和最高帮助"""
        self.screen.blit(self.help_image, self.help_rect)

