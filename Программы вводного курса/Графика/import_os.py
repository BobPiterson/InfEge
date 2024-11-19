import os
game_folder = os.path.dirname(__file__)
print(game_folder)

img_folder = os.path.join(game_folder, 'img')
print(img_folder)

print(os.path.join(img_folder, 'p1_jump.png'))
print('D:\Documents\GitHub\InfEge\Программы вводного курса\Графика\img\p1_jump.png')