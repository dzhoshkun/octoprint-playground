# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin


class MiniPlugin(octoprint.plugin.StartupPlugin):

	def on_after_startup(self):
		self._logger.info("Mini World!")


__plugin_name__ = "Mini Plugin"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Mini plugin with minimal settings"
__plugin_implementation__ = MiniPlugin()
