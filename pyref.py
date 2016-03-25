#-*- coding: utf-8-unix; -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import models

class MainWindow(object):

        def __init__(self):
                builder = Gtk.Builder()
                builder.add_from_file("layout.glade")
                builder.connect_signals({
                        "on_novo_menu_item_activate": self.on_novo_menu_item_activate,
                        "on_abrir_menu_item_activate": self.on_abrir_menu_item_activate,
                        "on_salvar_menu_item_activate": self.on_salvar_menu_item_activate,
                        "on_salvar_como_menu_item_activate": self.on_salvar_como_menu_item_activate,
                        "on_fechar_arquivo_menu_item_activate": self.on_fechar_arquivo_menu_item_activate,
                        "on_aboutMenuItem_activate": self.on_aboutMenuItem_activate,
                        "on_sair_menu_item_activate": Gtk.main_quit,
                        "on_main_window_delete_event": Gtk.main_quit
                })
		self.about = builder.get_object("about_dialog")
                self.file_chooser = builder.get_object("file_chooser_dialog")
                self.win = builder.get_object("main_window")
                self.win.show_all()

	def on_novo_menu_item_activate(self, widget):
                self.file_chooser.set_action(Gtk.FileChooserAction.SAVE)
                response = self.file_chooser.run()
                if response == Gtk.ResponseType.OK:
                        models.init(self.file_chooser.get_filename())
                        models.open()
                        models.create_tables()
                self.file_chooser.hide()

	def on_abrir_menu_item_activate(self, widget):
                self.file_chooser.set_action(Gtk.FileChooserAction.OPEN)
                response = self.file_chooser.run()
                if response == Gtk.ResponseType.OK:
                        models.init('database.db')
                self.file_chooser.hide()

	def on_salvar_menu_item_activate(self, widget):
                pass

	def on_salvar_como_menu_item_activate(self, widget):
                pass
        
        def on_fechar_arquivo_menu_item_activate(self, widget):
                pass

	def on_aboutMenuItem_activate(self, widget):
                self.about.run()
                self.about.hide()

if __name__ == "__main__":
        app = MainWindow()
        Gtk.main()
