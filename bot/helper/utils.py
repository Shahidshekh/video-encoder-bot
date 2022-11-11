import os
from bot import data, download_dir
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import MessageNotModified
from .ffmpeg_utils import encode, get_thumbnail, get_duration, get_width_height

def on_task_complete():
    del data[0]
    if len(data) > 0:
      add_task(data[0])

def add_task(app, message: Message):
    try:
      msg = message.reply_text("Downloading video...", quote=True)
      file = [message.document, message.video]
      file_name = [fi for fi in file if fi is not None][0].file_name
      

      filepath = app.download_media(message,download_dir)
      size = os.stat(filepath).st_size
      print(f"downloaded {size}")
      msg.edit("Encoding video...")
      new_file = encode(filepath)
      if new_file:
        msg.edit("Video Encoded, getting metadata...")
        duration = get_duration(new_file)
        thumb = get_thumbnail(new_file, download_dir, duration / 4)
        width, height = get_width_height(new_file)
        msg.edit("Uploading video...")
        message.reply_video(new_file, quote=True, supports_streaming=True, thumb=thumb, duration=duration, width=width, height=height)
        os.remove(new_file)
        os.remove(thumb)
        msg.edit("Video Encoded to x265")
      else:
        msg.edit("Something went wrong while encoding your file. Make sure it is not already in HEVC format.")
        os.remove(filepath)
    except MessageNotModified:
      pass
    except Exception as e:
      msg.edit(f"{e}")
    on_task_complete()
