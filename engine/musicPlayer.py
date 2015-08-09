import pygame

def playMusic(musicFile):
    clock = pygame.Clock()
    try:
        pygame.mixer.music.load(musicFile)
    except pygame.error:
        return
    pygame.mixer.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30)

if __name__ == '__main__':
    file = 'resources/music/track_01.mid'
    freq = 44100 # audio CD quality
    bitsize = -16 # unsigned 16 bit
    channels = 2 # 1 is mono, 2 is stereo
    buffer = 1024 # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)
    # optional volume 0 to 1.0
    pygame.mixer.music.set_volume(0.8)
    try:
        play_music(music_file)
    except KeyboardInterrupt:
        # if user hits Ctrl/C then exit
        # (works only in console mode)
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        raise SystemExit
