from view import UI
from model import BucketToolField as Field


def _normalize(i):
    return int( (65025 - i*i)**0.5 )


def heatmap(timestamp):
    timestamp %= 256*3
    epoch = timestamp / 256
    era = timestamp % 256
    if epoch == 0:
        return _normalize(era),era,0
    elif epoch == 1:
        return 0,_normalize(era),era
    else:
        return era,0,_normalize(era)


class Console:

    capture_path = "capture-{:0>3}.png"

    colors = {
            "white":   (255, 255, 255),
            "red":     (255,   0,   0),
            "yellow":  (255, 255,   0),
            "green":   (  0, 255,   0),
            "cyan":    (  0, 255, 255),
            "blue":    (  0,   0, 255),
            "magenta": (255,   0, 255),
            "black":   (  0,   0,   0)
            }

    def __init__(self):
        self.ui = UI()
        self.field = Field()
        self.heatmap = False
        self.color = Console.colors["blue"]

    def load_image(self, filename = "image.png"):
        self.ui.load(filename)

    def setFPS(self, fps):
        self.ui.setFPS(20)

    def useHeatMap(self):
        self.heatmap = True

    def useColor(self, color):
        self.heatmap = False
        self.color = color

    def run(self):
        exit_loop = False
        saves = 0
        ticks = 0
        while not exit_loop:
            for e in self.ui.getEvents():
                if e == UI.events.exit:
                    print e
                    exit_loop = True
                elif e == UI.events.click:
                    pos = self.ui.getMouse()
                    print e, pos
                    self.field.setGrid( self.ui.select(pos) )
                    self.field.seed(pos)
                elif e == UI.events.save:
                    print e
                    saves += 1
                    self.ui.save( Console.capture_path.format(saves) )
                elif e == UI.events.toggle:
                    print e
                    if self.heatmap:
                        self.useColor(Console.colors["blue"])
                    else:
                        self.useHeatMap()
                elif e == UI.events.reset:
                    print e
                    ticks = 0
                    self.ui.reset()
                    self.field.reset()
                else:
                    print "unknown event type:", e
            self.field.update()
            updates = self.field.getUpdates()
            if len(updates) > 0:
                if self.heatmap:
                    color = heatmap(ticks)
                    ticks += 1
                else:
                    color = self.color
                self.ui.draw(updates,color)
            self.ui.tick()
