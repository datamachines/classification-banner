import os
import pkg_resources
import platform

import classification_banner.utils.config         as utils_config
import classification_banner.utils.display        as utils_display

# GTK and GDK 
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
from gi.repository import Gtk, Gdk


def get_user():
  """Helper to get logged in username"""
  try:
      user = os.getlogin()
  except:
      user = 'UnknownUser'
  return user

def get_hostname():
  """Helper to get hostname"""
  return platform.node()


class ClassificationBanner:
  def __init__(self, classification=utils_config.get_system_classification(), location="top", banner_height=25):
    """Set up and display the main window """

    # Get and save the workable area of the manager supports it.
    work_area = utils_display.get_workable_area()

    # Prepare to use our stylesheet
    style_provider = Gtk.CssProvider()
    style_filename = 'style.css'
    style_path = "/etc/classification_banner/%s".format(style_filename)
    style_provider.load_from_path(style_path)
    Gtk.StyleContext.add_provider_for_screen(
      Gdk.Screen.get_default(),
      style_provider,
      Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

    # Set our current classficiation style class
    style_class = utils_config.get_classification_style_name(classification)

    # Get some screen information and save it off
    screen_size = utils_display.get_screen_size()
    self.hres = screen_size['width']
    self.vres = screen_size['height']

    # Create Main Window
    self.window = Gtk.Window(title="Classification Banner")
    self.window.set_position(Gtk.WindowPosition.CENTER)
    self.window.set_type_hint(Gdk.WindowTypeHint.DOCK)
    self.window.set_property('skip-taskbar-hint', True)
    self.window.set_property('skip-pager-hint', True)
    self.window.stick()
    self.window.set_decorated(False)
    self.window.set_keep_above(True)
    self.window.set_app_paintable(True)
    self.window.set_default_size(self.hres, 25)

    # Our main horizontal box for label containment
    hbox = Gtk.Box(spacing=10)
    hbox.get_style_context().add_class(style_class)

    # User label
    label_user = Gtk.Label(label=get_user())
    label_user.get_style_context().add_class(style_class)
    label_user.set_halign(Gtk.Align.START)

    # Classification label
    label_classification = Gtk.Label(label=utils_config.get_classification_label(classification))
    label_classification.get_style_context().add_class(style_class)
    label_classification.set_halign(Gtk.Align.CENTER)

    # Hostname label
    label_hostname = Gtk.Label(label=get_hostname())
    label_hostname.get_style_context().add_class(style_class)
    label_hostname.set_halign(Gtk.Align.END)

    # Pack up the horizontal box with the labels we made
    hbox.pack_start(label_user, True, True, 0)
    hbox.pack_start(label_classification, True, True, 0)
    hbox.pack_start(label_hostname, True, True, 0)

    # Add box to window
    self.window.add(hbox)
    
    # Show window and attach its life to Gtk
    self.window.show_all()
    self.window.connect("destroy", Gtk.main_quit)
    if location.lower() == "top":
      # Throw a hit at X11 to make room for static elements that need to cut down on workspace
      utils_display.hint_X11(
        window=self.window,
        top=(work_area['y'] + banner_height)
      )
      # Move window into place
      self.window.move(0, work_area['y'])
    elif location.lower() == "bottom":
      # Throw a hit at X11 to make room for static elements that need to cut down on workspace
      utils_display.hint_X11(
        window=self.window,
        bottom=banner_height
      )
      # Move window into place
      self.window.move(0, work_area['height']+2)
    

def main():
  if utils_display.detect_window_system() != "x11":
    print("You must be running X11 for this utility to work.")
    exit(1)

  ClassificationBanner(location="top")
  ClassificationBanner(location="bottom")

  Gtk.main()

if __name__ == "__main__":
    main()
