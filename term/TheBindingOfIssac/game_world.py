objects = [[],[],[]]
#objects = [[],[]]
LAYER_BG = 0
#layer_player = 1
LAYER_ISSAC = 1
LAYER_MONSTER = 2

def add_object(o, layer):
	objects[layer].append(o)

def remove_objects_at_layer(layer):
	for o in objects[layer]:
		# print('deleting', o)
		del o
	objects[layer] = []

def remove_object(o):
	for i in range(len(objects)):
		if o in objects[i]:
			print('deleting', o)
			objects[i].remove(o)
			del o
			break
def clear():
	for o in all_objects():
		del o
	objects.clear()

def all_objects():
	for i in range(len(objects)):
		for o in objects[i]:
			yield o

def issac_objects():
    for o in objects[LAYER_ISSAC]:
        yield o

def monster_objects():
    for o in objects[LAYER_MONSTER]:
        yield o

def bg_objects():
    for b in objects[LAYER_BG]:
        yield b

def GetMonsterNum():
    return len(objects[LAYER_MONSTER])

def background_objects():
    for o in objects[LAYER_BG]:
        yield o

def objects_at_layer(layer):
	for o in objects[layer]:
		yield o

def update():
	for o in all_objects():
		o.update()

def draw():
	for o in all_objects():
		o.draw()