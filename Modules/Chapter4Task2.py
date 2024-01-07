import cairo
import math

#Setup Surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 1000)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0,0,0)
ctx.paint()



#draw Black Square
ctx.rectangle(150,100,500,500)

ctx.set_source_rgb(0,0,0)
ctx.fill()

#Draw arcs
#First Arc
ctx.arc(150,350 ,250 , (3*math.pi/2), (math.pi/2))
ctx.set_line_width(10)
ctx.set_source_rgb(1,0,0)
ctx.stroke()

#2nd Arc
ctx.arc(650,350 ,250 , (math.pi/2), (3*math.pi/2))
ctx.set_line_width(10)
ctx.set_source_rgb(0,0,1)
ctx.stroke()

# #3rd Arc
ctx.arc(400,100 ,250 ,0 ,math.pi )
ctx.set_line_width(10)
ctx.set_source_rgb(1,0,0)
ctx.stroke()
#
# #4th Arc
ctx.arc(400,600 ,250 , math.pi ,0)
ctx.set_line_width(10)
ctx.set_source_rgb(0,0,1)
ctx.stroke()

surface.write_to_png('Chapter4Task2.png')