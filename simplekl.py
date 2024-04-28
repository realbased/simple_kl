import keyboard
import requests
import platform
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0')
from gi.repository import Gtk, Wnck

WEBHOOK_URL = "your link here"
