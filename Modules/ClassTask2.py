import cairo

#Define the surface
surface= cairo.ImageSurface(cairo.FORMAT_RGB24,1000,1000)
ctx= cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

#Draw 1st Triangle
ctx.move_to(400,400)
ctx.line_to(400,700)
ctx.line_to(800,700)
ctx.close_path()
ctx.set_line_width(10)
ctx.set_source_rgb(1,0,0)
ctx.stroke()

#Draw 2nd Triangle
ctx.move_to(830,700)
ctx.line_to(830,400)
ctx.line_to(430,400)
ctx.close_path()
ctx.set_source_rgb(0,1,0)
ctx.set_line_width(10)
ctx.stroke()


surface.write_to_png('Task2.png')

