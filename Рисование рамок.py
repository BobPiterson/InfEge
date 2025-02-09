# Рамка, размер которой подстраивается под размеры терминала
import shutil

x = shutil.get_terminal_size().columns  # ширина терминала
y = shutil.get_terminal_size().lines    # высота терминала

print('\u250F' + '\u2501' * (x - 2) + '\u2513')
for i in range(y - 3):
    print('\u2503' + ' ' * (x - 2) +  '\u2503')
print('\u2517' + '\u2501' * (x - 2) + '\u251B')