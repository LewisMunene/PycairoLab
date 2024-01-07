import cairo

#set up surface
surface= cairo.ImageSurface(cairo.FORMAT_RGB24,1000,1000)
ctx=cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8 )
ctx.paint()

ctx.move_to(50,100)
ctx.line_to(200,50)
ctx.line_to(250,300)
ctx.line_to(100,200)
ctx.close_path()
ctx.set_line_width(10)
ctx.set_source_rgb(1,0,0)
ctx.stroke()

surface.write_to_png('Polygon1.png')