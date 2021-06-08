import classification_banner.utils.classification as utils_classification
import classification_banner.utils.display        as utils_display
import classification_banner.utils.system         as utils_system

import pkg_resources

# GTK and GDK 
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
from gi.repository import Gtk, Gdk


class ClassificationBanner:
  def __init__(self, classification="unclass", location="top", banner_height=25):
    """Set up and display the main window """

    # Get and save the workable area of the manager supports it.
    work_area = utils_display.get_workable_area()

    # Normalize the classification string
    classification = utils_classification.normalize(classification)

    # Prepare to use our stylesheet
    style_provider = Gtk.CssProvider()
    style_name = 'style.css'
    style_path = pkg_resources.resource_filename(__name__, style_name)
    style_provider.load_from_path(style_path)
    Gtk.StyleContext.add_provider_for_screen(
      Gdk.Screen.get_default(),
      style_provider,
      Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

    # Set our current classficiation style class
    style_class = utils_classification.get_style_class(classification)

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
    label_user = Gtk.Label(label=utils_system.get_user())
    label_user.get_style_context().add_class(style_class)
    label_user.set_halign(Gtk.Align.START)

    # Classification label
    label_classification = Gtk.Label(label="FAKE: " + utils_classification.format_classification_message(classification))
    label_classification.get_style_context().add_class(style_class)
    label_classification.set_halign(Gtk.Align.CENTER)

    # Hostname label
    label_hostname = Gtk.Label(label=utils_system.get_hostname())
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

    # Throw a hit at X11 to make room for static elements that need to cut down on workspace
    if location.lower() == "top":
      utils_display.hint_X11(
        window=self.window,
        top=(work_area['y'] + banner_height)
      )
      # Move window into place
      self.window.move(0, work_area['y'])
    elif location.lower() == "bottom":
      utils_display.hint_X11(
        window=self.window,
        bottom=banner_height
      )
      # Move window into place
      self.window.move(0, work_area['height']+2)
    

def main():
  ClassificationBanner(location="top")
  ClassificationBanner(location="bottom")

  Gtk.main()

if __name__ == "__main__":
    main()
