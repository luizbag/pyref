import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(object):
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file("screens/layout.glade")
		builder = Gtk.Builder()
		builder.add_from_file("screens/layout.glade")
		win = builder.get_object("applicationwindow1")
		win.connect("delete-event", Gtk.main_quit)
		win.connect("activate", self.about_activated);
		win.show_all()
		Gtk.main()

	def about_activated(self, widget):
		pass

MainWindow()