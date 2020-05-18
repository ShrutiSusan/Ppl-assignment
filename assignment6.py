import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from gi.repository import cairo


class MouseButtons:
    
    LEFT_BUTTON = 1
    RIGHT_BUTTON = 3
    
class Window(Gtk.Window):
	def __init__(self):
		super(Window,self).__init__();
		self.set_title("Paint Application");
		self.set_default_size(800,600);
		
		
		mb = Gtk.MenuBar.new()
		fm=Gtk.Menu.new()
		em=Gtk.Menu.new()
		bs=Gtk.Menu.new()
		bc=Gtk.Menu.new()
		fileMenu = Gtk.MenuItem.new_with_label("File")
		editMenu=Gtk.MenuItem.new_with_label("Edit")
		brushSize = Gtk.MenuItem.new_with_label("Brush Size")
		brushColor= Gtk.MenuItem.new_with_label("Brush Color")
		fileMenu.set_submenu(fm);
		editMenu.set_submenu(em);
		brushSize.set_submenu(bs);
		brushColor.set_submenu(bc);
		mb.append(fileMenu);
		mb.append(editMenu);
		mb.append(brushSize);
		mb.append(brushColor);
		
		save = Gtk.MenuItem.new_with_label("Save")
		clear = Gtk.MenuItem.new_with_label("Clear")
		preferences=Gtk.MenuItem.new_with_label("Preferences")
		help=Gtk.MenuItem.new_with_label("Help");
		fm.append(save)
		fm.append(clear)
		
		edit= Gtk.MenuItem.new_with_label("Edit")
		refactor= Gtk.MenuItem.new_with_label("Refactor")
		quit= Gtk.MenuItem.new_with_label("Quit")
		em.append(edit)
		em.append(refactor);
		em.append(quit);
		
		brushsize1 = Gtk.MenuItem.new_with_label("3x")
		brushsize2 = Gtk.MenuItem.new_with_label("5x")
		brushsize3 = Gtk.MenuItem.new_with_label("7x")
		brushsize4= Gtk.MenuItem.new_with_label("9x")
		bs.append(brushsize1)
		bs.append(brushsize2)
		bs.append(brushsize3)
		bs.append(brushsize4)
		
		black = Gtk.MenuItem.new_with_label("Black")
		red= Gtk.MenuItem.new_with_label("Red")
		green = Gtk.MenuItem.new_with_label("Green")
		yellow= Gtk.MenuItem.new_with_label("Yellow")
		bc.append(black)
		bc.append(red)
		bc.append(green)
		bc.append(yellow)
		self.connect("destroy",Gtk.main_quit);
		darea = Gtk.DrawingArea()
		darea.connect("draw", self.expose)
		darea.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)  
		self.coords= []   
		darea.connect("button-press-event",self.on_button_press); 
        
		hb = Gtk.HeaderBar()
		hb.pack_start(mb)
		box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
		box.pack_start(hb, False, False, 10)
		box.pack_start(darea, True, True, 10)
		self.add(box)
		self.show_all()
	        
	def expose(self, wid, cr):

		cr.set_source_rgb(0, 0, 0)
		cr.set_line_width(0.5)
		
		for i in self.coords:
		    for j in self.coords:
		        
		        cr.move_to(i[0], i[0])
		        cr.line_to(j[0], j[1]) 
		        cr.stroke()

		del self.coords[:]
	def on_button_press(self,w,e):
		if e.type == Gdk.EventType.BUTTON_PRESS \
		    and e.button == MouseButtons.LEFT_BUTTON:
		    
		    self.coords.append([e.x, e.y])
		if e.type == Gdk.EventType.BUTTON_PRESS \
		    and e.button == MouseButtons.RIGHT_BUTTON:
		    cr = w.get_property("window").cairo_create()
		    for i in range (len(self.coords)-1):
		    	cr.move_to(self.coords[i][0],self.coords[i][1])
		    	cr.line_to(self.coords[i+1][0],self.coords[i+1][1])
		    	cr.stroke();
            
        	
Window();

Gtk.main();
