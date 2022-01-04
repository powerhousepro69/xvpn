#!/usr/bin/python
import os
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

def main():
  indicator = appindicator.Indicator.new("customtray", "semi-starred-symbolic" , appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  gtk.main()

def menu():
  menu = gtk.Menu()
  exittray = gtk.MenuItem('Disconnect VPN')
  exittray.connect('activate', quit)
  menu.append(exittray)
  
  menu.show_all()
  return menu
  
def quit(_):
    os.system("expressvpn disconnect")
    os.system("notify-send 'VPN Tray Icon - SHUTDOWN'") 
    gtk.main_quit()


if __name__ == "__main__":
  main()
