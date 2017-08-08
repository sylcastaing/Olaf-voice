#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import logging

from threading import Thread, Event

from respeaker import Microphone, Player, pixel_ring

from olaf import Bot, Speech
from olaf.config import Logger

logger = logging.getLogger('olaf-voice.main')

def task(quit_event):
    mic = Microphone(quit_event=quit_event)
    player = Player(mic.pyaudio_instance)

    pixel_ring.set_color(rgb=0x505000)
    time.sleep(3)

    speech = Speech()
    myBot = Bot()

    while not quit_event.is_set():
        if mic.wakeup(keyword='olaf'):
            pixel_ring.listen()
            data = mic.listen()
            pixel_ring.wait()
            text = speech.recognize(data)
            if text:
                logger.debug('Recognized : %s', text)
                result = myBot.request(text)
                pixel_ring.speak(4, 0)
                audio = speech.synthetize(result)

                if (audio != None):
                    player.play_raw(audio)
                
            pixel_ring.off()

    mic.close()
    pixel_ring.off()

def main():
    Logger()

    logger.info("Starting application")

    quit_event = Event()
    thread = Thread(target=task, args=(quit_event,))
    thread.start()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            logger.info("KeyboardInterrupt = Quit")
            quit_event.set()
            break
    thread.join()

if __name__ == '__main__':
    main()