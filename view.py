
import pygame


class Events:
    exit = "EXIT"
    click = "CLICK"
    save = "SAVE"
    toggle = "TOGGLE"
    reset = "RESET"

    def __init__(self):
        pass

class UI:

    events = Events()
    _exit_keys = [ pygame.K_q, pygame.K_ESCAPE ]
    _save_keys = [ pygame.K_s ]
    _toggle_keys = [ pygame.K_t ]
    _reset_keys = [ pygame.K_r ]
    
    def __init__(self, fps = 20):
        pygame.init()

        self._clock = pygame.time.Clock()
        self._fps = fps
        
        self._surface = None
        self._image = None
        self._size = None

    def load(self, filename = "image.png"):
        self._image = pygame.image.load(filename)
        self._size = self._image.get_size()
        pygame.display.set_mode(self._size)
        self._surface = pygame.display.get_surface()
        self._surface.blit(self._image, (0,0))
        pygame.display.flip()

    def save(self,filename):
        if self._surface:
            pygame.image.save(self._surface,filename)

    def reset(self):
        self._surface.blit(self._image, (0,0) )
    def getEvents(self):
        events = []
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key in self._exit_keys:
                    events.append(UI.events.exit)
                elif e.key in self._save_keys:
                    events.append(UI.events.save)
                elif e.key in self._toggle_keys:
                    events.append(UI.events.toggle)
                elif e.key in self._reset_keys:
                    events.append(UI.events.reset)
            elif e.type == pygame.MOUSEBUTTONDOWN:
                events.append(UI.events.click)
        return events

    def getMouse(self):
        return pygame.mouse.get_pos()

    def getSize(self):
        return self._size

    def draw(self, updates, color):
        #updates is a list of pos-color tuples ( (x,y), (r,g,b) )
        pxa = pygame.PixelArray(self._surface)
        for x,y in updates:
            pxa[x,y] = color
        s = pxa.surface
        del pxa
        self._surface.blit(s, (0,0))

    def setFPS(self,fps):
        self._fps = fps

    def tick(self):
        pygame.display.flip()
        self._clock.tick(self._fps)

    def getp(self, pos):
        return self._surface.get_at(pos)

    def select(self, location):
        grid = []
        if self._surface:
            pxa = pygame.PixelArray(self._surface)
            w,h = self._size
            c = pxa[location]
            for y in range(h):
                grid.append([])
                for x in range(w):
                    if pxa[x,y] == c:
                        grid[y].append(1)
                    else:
                        grid[y].append(0)
        return grid

