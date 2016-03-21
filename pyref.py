import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(object):

	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file("layout.glade")
		builder.connect_signals({
			"on_aboutMenuItem_activate": self.on_aboutMenuItem_activate,
			"on_main_window_delete_event": Gtk.main_quit
		})
		self.about = builder.get_object("about_dialog")
		self.win = builder.get_object("main_window")
		self.win.show_all()

	def on_aboutMenuItem_activate(self, widget):
		self.about.run()
		self.about.hide()

if __name__ == "__main__":
    app = MainWindow();
    Gtk.main()