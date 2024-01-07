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

#Draw the Bezier Curve
ctx.move_to(0.5, 0.5)
ctx.curve_to(1, 0, 2, 1, 2.5, 0.5)
ctx.line_to(2.5, 1.5)
ctx.curve_to(1.5, 1.2, 1.5, 1.2, 0.5, 1.5)
ctx.close_path()
ctx.set_source_rgb(1, 0, 0.5)
ctx.set_line_width(0.04)
ctx.stroke()

surface.write_to_png('Bezier.png')