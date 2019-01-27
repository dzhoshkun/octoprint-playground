# coding=utf-8
from __future__ import absolute_import

from octoprint.plugin import (
	StartupPlugin, TemplatePlugin, SettingsPlugin
)


class MiniPlugin(StartupPlugin, TemplatePlugin, SettingsPlugin):

	def on_after_startup(self):
		self._logger.info("Mini World! (more: %s)" % self._settings.get(["url"]))

	def get_settings_defaults(self):
		return dict(url="https://en.wikipedia.org/wiki/Hello_world")


__plugin_implementation__ = MiniPlugin()
