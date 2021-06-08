import gi
gi.require_version("Gdk", "3.0")
from gi.repository import Gdk

# TODO(mmay): X11 specific imports, import only when needed
from Xlib.display import Display
from Xlib import X


def get_screen_size():
  display = Gdk.Display.get_default()
  # monitor = display.get_primary_monitor()
  monitor = display.get_monitor(0)
  geometry = monitor.get_geometry()
  scale_factor = monitor.get_scale_factor()
  width = scale_factor * geometry.width
  height = scale_factor * geometry.height
  return {'width': width, 'height': height}

def get_workable_area():
  display = Gdk.Display.get_default()
  # monitor = display.get_primary_monitor()
  monitor = display.get_monitor(0)
  w_area = monitor.get_workarea()
  return { 
    'x': w_area.x, 
    'y': w_area.y,
    'width': w_area.width,
    'height': w_area.height
  }

def hint_X11(window, top=0, bottom=0):
  """ Hint to X11 that we have something statically taking up space """
  display = Display()
  try:
    top_window = display.create_resource_object('window', window.get_toplevel().get_window().get_xid())
    top_window.change_property(
      display.intern_atom('_NET_WM_STRUT'),
      display.intern_atom('CARDINAL'),
      32,
      [0, 0, top, bottom],
      X.PropModeReplace
    )
    top_window.change_property(
      display.intern_atom('_NET_WM_STRUT_PARTIAL'),
      display.intern_atom('CARDINAL'),
      32,
      [0, 0, top, bottom, 0, 0, 0, 0, 0, 0, 0, 0],
      X.PropModeReplace
    )
  except:
    print("Not running X11, not going to be able to use strut partial")
  return None