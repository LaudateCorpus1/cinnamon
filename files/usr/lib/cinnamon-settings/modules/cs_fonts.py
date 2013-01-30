#!/usr/bin/env python

from SettingsWidgets import *

class Module:
    def __init__(self, content_box):
        keywords = _("font, size, small, large")
        tooltip = _("Manage system fonts and text scaling")
        sidePage = SidePage(_("Fonts"), "fonts.svg", keywords, tooltip, content_box)
        self.sidePage = sidePage
        self.name = "fonts"
        self.category = "appear"
        sidePage.add_widget(GSettingsRangeSpin(_("Text scaling factor"), "org.gnome.desktop.interface", "text-scaling-factor", None, adjustment_step = 0.1))
        sidePage.add_widget(GSettingsFontButton(_("Default font"), "org.gnome.desktop.interface", "font-name", None))
        sidePage.add_widget(GSettingsFontButton(_("Document font"), "org.gnome.desktop.interface", "document-font-name", None))
        sidePage.add_widget(GSettingsFontButton(_("Monospace font"), "org.gnome.desktop.interface", "monospace-font-name", None))
        sidePage.add_widget(GSettingsFontButton(_("Window title font"), "org.gnome.desktop.wm.preferences", "titlebar-font", None))
        sidePage.add_widget(GSettingsComboBox(_("Hinting"), "org.gnome.settings-daemon.plugins.xsettings", "hinting", None, [(i, i.title()) for i in ("none", "slight", "medium", "full")]))
        sidePage.add_widget(GSettingsComboBox(_("Antialiasing"), "org.gnome.settings-daemon.plugins.xsettings", "antialiasing", None, [(i, i.title()) for i in ("none", "grayscale", "rgba")]))

