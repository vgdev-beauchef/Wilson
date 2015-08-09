import pygame

def playMusic(musicFile):
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(musicFile)
    except pygame.error:
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30)
def musicWrapper(musicFile):
    freq = 44100 # audio CD quality
    bitsize = -16 # unsigned 16 bit
    channels = 2 # 1 is mono, 2 is stereo
    buffer = 1024 # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)
    # optional volume 0 to 1.0
    pygame.mixer.music.set_volume(1.0)
    try:
        playMusic(musicFile)
    except KeyboardInterrupt:
        # if user hits Ctrl/C then exit
        # (works only in console mode)
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        raise SystemExit

if __name__ == '__main__':
    file = 'resources/tracks/track_01.mid'
    freq = 44100 # audio CD quality
    bitsize = -16 # unsigned 16 bit
    channels = 2 # 1 is mono, 2 is stereo
    buffer = 1024 # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)
    # optional volume 0 to 1.0
    pygame.mixer.music.set_volume(1.0)
    try:
        playMusic(file)
    except KeyboardInterrupt:
        # if user hits Ctrl/C then exit
        # (works only in console mode)
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        raise SystemExit
