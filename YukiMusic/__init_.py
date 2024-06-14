from YukiMusic.core.bot import Anony
from YukiMusic.core.dir import dirr
from YukiMusic.core.git import git
from YukiMusic.core.userbot import Userbot
from YukiMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()