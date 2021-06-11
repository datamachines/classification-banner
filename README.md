# Installation
## Dependencies
* Ubuntu: `apt install python3-gobject python3-xlib python3-yaml gtk3`
* CentOS:
  * `dnf install epel-release`
  * `dnf install python3-gobject python3-xlib python3-pyyaml gtk3`

## Configurations
### Required
* `cp -R etc/classification-banner /etc`
### Autostart
* `cp etc/xdg/autostart/classification-banner.desktop /etc/xdg/autostart/`

## Running from CLI
* `python3 test.py`

# Limitations
Currently works with X11. Wayland does not support struts which limits our
ability to edit the workable area (the area not taken up by taskbar, menubar,
and now the classification bar). 