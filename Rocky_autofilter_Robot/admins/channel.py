# MIT License

# Copyright (c) 2022 sachin9742s

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Telegram Link : https://telegram.dog/Kiccharequest
# Repo Link : https://github.com/sachin9742s/Rocky_autofilter_Robot
# License Link : https://github.com/sachin9742s/Rocky_autofilter_Robot/blob/Rocky_autofilter_Robot/LICENSE

from pyrogram import Client, filters
from database.autofilter_mdb import save_file
from Rocky_autofilter_Robot import CHANNELS

media_filter = filters.document | filters.video | filters.audio

@Client.on_message(filters.chat(CHANNELS) & media_filter)
async def media(bot, update):
    for file_type in ("document", "video", "audio"):
        media = getattr(update, file_type, None)
        if media is not None:
            break
    else:
        return

    media.file_type = file_type
    media.caption = update.caption
    await save_file(media)
