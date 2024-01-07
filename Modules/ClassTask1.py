import cairo
import math

surface= cairo.ImageSurface(cairo.FORMAT_RGB24,1000,1000)
ctx=cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8 )
ctx.paint()

#Draw the two line
ctx.move_to(250,300)#Point A
ctx.line_to(450,600)#Point B

ctx.move_to(650,200)#Point C
ctx.line_to(850,500)#Point D
ctx.set_line_width(10)
ctx.set_source_rgb(1,0,0)
ctx.stroke()


#Draw the 1st Curve
ctx.curve_to(570,350,230,400,250,300)
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(8)
ctx.stroke()


#Draw the 2nd Curve
ctx.curve_to(850,500,700,190,220,461)
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(8)
ctx.stroke()



surface.write_to_png('Task1.png')