import cairo
import math

surface= cairo.ImageSurface(cairo.FORMAT_RGB24,1000,1000)
ctx= cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()


#RoundRec functions
def roundrect(ctx, x, y, width, height, r):
    ctx.arc(x + r, y + r, r, math.pi, 3 * math.pi / 2)
    ctx.arc(x + width - r, y + r, r, 3 * math.pi / 2, 0)
    ctx.arc(x + width - r, y + height - r, r, 0, math.pi / 2)
    ctx.arc(x + r, y + height - r, r, math.pi / 2, math.pi)
    ctx.close_path()


#Draw the Rectangle with arcs
# ctx.move_to(200,200)#Point A
# ctx.line_to(200,800)#Point B
# ctx.line_to(650,800)#Point C
# ctx.line_to(650,200)#Point D
# ctx.close_path()

roundrect(ctx, 300,100, 400, 800,50)
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(10)
ctx.stroke()

#Draw the lines to form an A
ctx.move_to(370,150)
ctx.line_to(390,220)

ctx.move_to(370,150)
ctx.line_to(340,220)

ctx.move_to(350,185)
ctx.line_to(380,185)


#Creating the Inverted A
ctx.move_to(370,150)
ctx.line_to(405,220)

ctx.move_to(370,150)
ctx.line_to(330,220)

ctx.move_to(350,185)
ctx.line_to(400,185)


ctx.set_source_rgb(1,0,0)
ctx.set_line_width(10)
ctx.stroke()





surface.write_to_png('Task4.png')


