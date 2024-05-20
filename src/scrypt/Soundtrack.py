import os, sys, pygame

class Soundtrack:
    
    soundtrack = None
    sound = None

    def __init__(self, soundtrack):
        if os.path.isfile(soundtrack):
            self.soundtrack = soundtrack
            pygame.mixer.init()
        else:
            print(soundtrack + "not found... ignoring", file=sys.strderr)

    def play(self):
        pygame.mixer.music.load(self.soundtrack)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=-1)
    
    def set(self, soundtrack):
        if os.path.isfile(soundtrack):
            self.soundtrack = soundtrack
        else:
            print(soundtrack + "not found... ignoring")#, file=sys.strderr)

    def play_sound(self, sound):
        # som
        if os.path.isfile(sound):
            self.sound = sound
            pygame.mixer.music.load(self.sound)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
        else:
            print(sound + " file not found.. ignoring")#, file=sys.stderr)