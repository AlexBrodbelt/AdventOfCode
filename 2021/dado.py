import secrets
import ctypes
import winsound

sneaky_number = secrets.choice([i+j for i in range(1,7) for j in range(1,7)])

winsound.PlaySound("Grabación.wav", winsound.SND_ALIAS)

ctypes.windll.user32.MessageBoxW(0, "That will be a {} for you\n friiiiibeeeeee \N{winking face}" .format(sneaky_number), 16)


