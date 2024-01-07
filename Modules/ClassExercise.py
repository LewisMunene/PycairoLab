import cairo

#Setup Surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 100)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

#draw the image
ctx.rectangle(50,100,100,240)
ctx.set_source_rgb(1,0,0)
ctx.fill()

#Green Rectangle
ctx.rectangle(250,100,100,240)
ctx.set_source_rgb(0,1,0)
ctx.fill()

#draw Blue Square
ctx.rectangle(450,100,240,240)
ctx.set_source_rgb(0,0,1)
ctx.fill()

#Draw a Yellow Triangle
#define the points
x1=400
y1=200
x2=500
y2=800
x3=200
y3=800
x3
ctx.move_to(x1, y1)
ctx.line_to(x2, y2)
ctx.line_to(x3,y3)
ctx.set_source_rgb(1, 1.5, 0)
ctx.fill()
ctx.close_path()









surface.write_to_png('example.png')
