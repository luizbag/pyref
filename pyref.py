import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("layout.glade")
win = builder.get_object("applicationwindow1");
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()