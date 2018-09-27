from pico2d import *
import random




def handle_events():
        global running
        events = get_events()
        for event in events:
                if event.type == SDL_MOUSEMOTION:
                    global MouseX, MouseY
                    MouseX = event.x
                    MouseY = 600 - event.y
                    #print(event.x, ", ", event.y)
                elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                    running = False
                elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
                    speed+=1
                elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
                    speed-=1
                elif event.type == SDL_MOUSEBUTTONUP:
                    tx, ty = event.x, 600 - event.y
                    global waypoints
                    waypoints += [ (tx, ty) ]
                    if event.button == 1:
                        tx, ty = event.x, 600 - event.y
                        waypoints += [ (tx, ty) ]
                    else:
                        waypoints = []
class Grass:
	def __init__(self):
		self.image = load_image('grass.png')
		print(self.image)
	def draw(self):
		self.image.draw(400, 300)

class Boy:
	def __init__(self):
		print("Creating..")
		self.x = random.randint(0, 200)
		self.y = random.randint(90, 550)
		self.speed = random.uniform(1.0, 3.0)
		self.frame = random.randint(0, 7)
		self.image = load_image('run_animation.png')

	def draw(self):
		self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

	def update(self, _MouseX, _MouseY):
		self.frame = (self.frame + 1) % 8
		if _MouseX > self.x:
			self.x += self.speed
		else:
			self.x -= self.speed

		if (0 != _MouseX - self.x):
			alpha = (_MouseY - self.y) / (_MouseX - self.x)
		else:
			if _MouseY > self.y:
					self.y += self.speed
					return
			else:
					self.y -= self.speed
					return
		beta = self.y - alpha * self.x
		if _MouseX > self.x:
			self.y = alpha * (self.x + self.speed) + beta
			return
		else:
			self.y = alpha * (self.x - self.speed) + beta
			return
	def GetX(self):
		return self.x
	def GetY(self):
		return self.y

open_canvas()



MouseX = 0
MouseY = 0
waypoints = []
g = Grass()
boys = [ Boy() for i in range(20) ]

running = True


while (True == running):
	handle_events()
	print(MouseX, ", ", MouseY)

	if len(waypoints) > 0:
		for b in boys:
			b.update(waypoints[0][0], waypoints[0][1])
		for b in boys:
			if b.GetX() <= waypoints[0][0] + 2 and b.GetX() >= waypoints[0][0] - 2 and b.GetY() <= waypoints[0][1] + 2 and b.GetY() >= waypoints[0][1] - 2:
				waypoints.reverse()
				waypoints.pop()
				waypoints.pop()
				waypoints.reverse()
				break

	clear_canvas()
	g.draw()
	for b in boys:
		b.draw()

	update_canvas()

	delay(0.03)
