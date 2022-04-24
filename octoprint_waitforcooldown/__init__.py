# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from octoprint.events import Events
import threading
import time

class WaitForCooldownPlugin(octoprint.plugin.EventHandlerPlugin,
                            octoprint.plugin.SettingsPlugin,
                            octoprint.plugin.StartupPlugin,
                            octoprint.plugin.TemplatePlugin):

    ##~~ StartupPlugin mixin

    def on_after_startup(self):
        self._events = dict(cooldownevent=threading.Event())
        self._logger.debug("Current command: {}".format(self._settings.get_boolean(["isenabled"])))

    def _gcode_waitforcooldown(self):
        targettemp=self._settings.get_int(["cooldowntemp"])
        self._logger.debug("Waiting for hotend to reach {}\N{DEGREE SIGN}C".format(targettemp))

        tool = self._printer._comm.getCurrentTool()
        cmd = 'M104 T{} S0'.format(tool)
        self._printer._comm._do_send(cmd, gcode='M104')
        cmd = 'M117 Cooldown to {}C'.format(targettemp)
        self._printer._comm._do_send(cmd, gcode='M117')
 
        self._events['cooldownevent'].set()
        while self._events['cooldownevent'].is_set():
            heaters = self._printer.get_current_temperatures()
            currenttemp = heaters['tool' + str(tool)]['actual']
            self._logger.debug("Hotend {} current temperature: {}\N{DEGREE SIGN}C".format(tool, currenttemp))
            if currenttemp <= targettemp:
                break
            time.sleep(3)

    def hook_gcode_sending(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
        if self._settings.get_boolean(["isenabled"]) and cmd.strip() == "@WAITFORCOOLDOWN":
            self._printer.set_job_on_hold(True, blocking=False)
            self._gcode_waitforcooldown()
            self._printer.set_job_on_hold(False)
            return

    ##~~ EventHandlerPlugin mixin

    def on_event(self, event, payload):
        if event in [Events.DISCONNECTING,
                     Events.ERROR]:
            for k, e in self._events.items():
                if e.is_set():
                    self._logger.debug("Aborting {}".format(k))
                    e.clear()

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return dict(isenabled=True,
                    cooldowntemp = 60,
                    installed_version = self._plugin_version)

    def get_template_configs(self):
        return [dict(type="settings", custom_bindings=False)]

    ##~~ Softwareupdate hook

    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software Update
        # Plugin here. See https://docs.octoprint.org/en/master/bundledplugins/softwareupdate.html
        # for details.
        return {
            "waitforcooldown": {
                "displayName": "WaitForCooldown Plugin",
                "displayVersion": self._plugin_version,

                # version check: github repository
                "type": "github_release",
                "user": "ZombiePangolin",
                "repo": "OctoPrint-WaitForCooldown",
                "current": self._plugin_version,

                # update method: pip
                "pip": "https://github.com/ZombiePangolin/OctoPrint-WaitForCooldown/archive/{target_version}.zip",
            }
        }


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Wait For Cooldown"


# Set the Python version your plugin is compatible with below. Recommended is Python 3 only for all new plugins.
# OctoPrint 1.4.0 - 1.7.x run under both Python 3 and the end-of-life Python 2.
# OctoPrint 1.8.0 onwards only supports Python 3.
__plugin_pythoncompat__ = ">=3,<4"  # Only Python 3

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = WaitForCooldownPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information,
        "octoprint.comm.protocol.gcode.sending": __plugin_implementation__.hook_gcode_sending
    }
