import simple_draw as sd

sd.resolution = (1200,600)

def bubble(point,step):

    radius = 50
    for _ in range(3):

        radius += step

        sd.circle(center_position=point, radius=radius,) 
    

for x in range(100, 1100, 100):
    point = sd.get_point(x,100)
    bubble(point=point,step=3) 
sd.pause()
