# coding=utf-8
from __future__ import absolute_import

from octoprint.plugin import StartupPlugin, TemplatePlugin


class MiniPlugin(StartupPlugin, TemplatePlugin):

	def on_after_startup(self):
		self._logger.info("Mini World!")


__plugin_implementation__ = MiniPlugin()
