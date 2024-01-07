import cairo
import math
#Create Surface
width=3
height=2
PIXEL_SCALE=100
surface = cairo.ImageSurface(cairo.FORMAT_RGB24,width*PIXEL_SCALE,height*PIXEL_SCALE)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()
ctx.scale(PIXEL_SCALE,PIXEL_SCALE)

#arc
ctx.arc(0.5, 0.2, 0.5, 0, math.pi/2)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.04)
ctx.stroke()

#segment
ctx.arc(1, 1.2, 0.5, 0, math.pi/2)
ctx.close_path()
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

#sector
ctx.move_to(2, 0.2)
ctx.arc(2, 0.2, 0.5, 0, math.pi/2)
ctx.close_path()
ctx.set_source_rgb(0, 1, 0)
ctx.fill()

surface.write_to_png('Arcs.png')