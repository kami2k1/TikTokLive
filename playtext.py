import os
import uuid
import asyncio
from gtts import gTTS
from pydub import AudioSegment

import pygame
pygame.mixer.init()
runing = True
idz = 0
async def play(text, speed: float = 1.1):
  global runing , idz
  try:
    
    idz +=1
   
    if runing == False:

        temp = 'data'
        
        os.makedirs(temp, exist_ok=True)


        id = f"tiktok{idz}.mp3"
        temp_file = os.path.join(temp, id)


        tts = gTTS(text, lang="vi")
        tts.save(temp_file)





        if speed != 1.0: 
            Au = AudioSegment.from_file(temp_file, format="mp3")
            Au = Au.speedup(playback_speed=speed)
            Au.export(temp_file, format="mp3")


    
        pygame.mixer.music.load(temp_file)
        await asyncio.to_thread(pygame.mixer.music.play)
    
        while pygame.mixer.music.get_busy():  # Chờ phát xong
            await asyncio.sleep(0.1)
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        os.remove(temp_file)
        runing = True
  except Exception as e:
     runing = True
   
    

