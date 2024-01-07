import cairo


#Setup Surface
width=3
height=2
PIXEL_SCALE=100
surface = cairo.ImageSurface(cairo.FORMAT_RGB24,width*PIXEL_SCALE,height*PIXEL_SCALE)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()
ctx.scale(PIXEL_SCALE,PIXEL_SCALE)


#Draw Polygons
ctx.move_to(1, 0.5)
ctx.line_to(2, 0.5)
ctx.line_to(2.2, 1.3)
ctx.line_to(1.5, 1.7)
ctx.line_to(0.8, 1.3)
ctx.close_path()

ctx.set_source_rgb(1, 0.5, 0)
ctx.fill_preserve()



surface.write_to_png('polygons.png')
