# Octoprint-WaitForCooldown
Watches gcode for an @WAITFORCOOLDOWN, then waits until hotend temperature is cooled off to the set temperature before continuing.  
I created this because M109 R60 wasn't waiting for cooldown on my printer.

## Setup
Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager) or manually from GitHub:
    https://github.com/ZombiePangolin/Octoprint-WaitForCooldown
