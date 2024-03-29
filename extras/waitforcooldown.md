---
layout: plugin

id: waitforcooldown
title: OctoPrint-WaitForCooldown
description: Watches gcode for an @WAITFORCOOLDOWN, then waits until hotend temperature is cooled off to the set temperature before continuing.
authors:
- ZombiePangolin
license: AGPLv3

# TODO
date: 2022-04-24

homepage: https://github.com/ZombiePangolin/OctoPrint-WaitForCooldown
source: https://github.com/ZombiePangolin/OctoPrint-WaitForCooldown
archive: https://github.com/ZombiePangolin/OctoPrint-WaitForCooldown/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
#tags:
#- a list
#- of tags
#- that apply
#- to your plugin
#- (take a look at the existing plugins for what makes sense here)

# TODO
# When registering a plugin on plugins.octoprint.org, all screenshots should be uploaded not linked from external sites.
#screenshots:
#- url: url of a screenshot, /assets/img/...
#  alt: alt-text of a screenshot
#  caption: caption of a screenshot
#- url: url of another screenshot, /assets/img/...
#  alt: alt-text of another screenshot
#  caption: caption of another screenshot
#- ...

# TODO
#featuredimage: url of a featured image for your plugin, /assets/img/...

# TODO
# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

compatibility:

  # List of compatible versions
  #
  # A single version number will be interpretated as a minimum version requirement,
  # e.g. "1.3.1" will show the plugin as compatible to OctoPrint versions 1.3.1 and up.
  # More sophisticated version requirements can be modelled too by using PEP440
  # compatible version specifiers.
  #
  # You can also remove the whole "octoprint" block. Removing it will default to all
  # OctoPrint versions being supported.

  octoprint:
  - 1.4.0

  # List of compatible operating systems
  #
  # Valid values:
  #
  # - windows
  # - linux
  # - macos
  # - freebsd
  #
  # There are also two OS groups defined that get expanded on usage:
  #
  # - posix: linux, macos and freebsd
  # - nix: linux and freebsd
  #
  # You can also remove the whole "os" block. Removing it will default to all
  # operating systems being supported.

  os:
  - linux
  - windows
  - macos
  - freebsd

  # Compatible Python version
  #
  # It is recommended to only support Python 3 for new plugins, in which case this should be ">=3,<4"
  # 
  # Plugins that wish to support both Python 2 and 3 should set it to ">=2.7,<4".
  #
  # Plugins that only support Python 2 will not be accepted into the plugin repository.

  python: ">=3,<4"

---

#**TODO**: Longer description of your plugin, configuration examples etc. This part will be visible on the page at
http://plugins.octoprint.org/plugin/waitforcooldown/
