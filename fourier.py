import pygame as pg
import math

pg.init()

black = (0, 0, 0)
white = (255, 255, 255)

width = 800
height = 600

screen = pg.display.set_mode((width, height))

pg.display.set_caption("Fourier Visualizations")

running = True

t = 0
wave_number = 1
points = []

font = pg.font.SysFont('Liberation Serif', 32, True, False)

while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_UP:
				if wave_number < 50:
					wave_number = wave_number + 1
			if event.key == pg.K_DOWN:
				if wave_number > 1:
					wave_number = wave_number - 1

	screen.fill(black)
	text = font.render("Wave Number = " + str(wave_number), False, white, black)
	screen.blit(text, (10, 10))

	

	starts = [[200, height / 2]];
	radii = [100]
	ends = [[starts[0][0] + radii[0]*math.cos(t), starts[0][1] - radii[0]*math.sin(t)]]
	centers = [[int(starts[0][0]), int(starts[0][1])]]

	for k in range(1, wave_number):
		starts.append(ends[-1])
		radii.append(radii[0] / (2*k+1))
		ends.append([starts[-1][0] + radii[-1]*math.cos((2*k+1)*t), starts[-1][1] - radii[-1]*math.sin((2*k+1)*t)])
		centers.append([int(starts[-1][0]), int(starts[-1][1])])

	for k in range(0, wave_number):
		pg.draw.line(screen, white, starts[k], ends[k], 1)
		pg.draw.circle(screen, white, centers[k], int(radii[k]), 1)

	projector_start = ends[-1]
	projector_end = [500, projector_start[1]]
	pg.draw.line(screen, white, projector_start, projector_end, 1)

	if len(points) == 600:
		points.pop()
	for p in points:
		p[0] = p[0] + 0.3
	points = [projector_end] + points
	for p in points:
		pg.draw.line(screen, white, p, p, 1)

	pg.display.update()
	t = t + 0.01
	if t == 314.16:
		t = 0