import pyfiglet
import osutools

from pyfiglet import Figlet
textbig = Figlet(font='doh')
print(textbig.renderText('OSU!STATS'))
print("Witaj W OSU!STATS 1.0")

token = input("Podaj Token Api Osu Możesz Go Wygenerować Na https://osu.ppy.sh/p/api")
osu = osutools.OsuClient(token)
print(osu)