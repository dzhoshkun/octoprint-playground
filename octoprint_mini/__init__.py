# coding=utf-8
from __future__ import absolute_import

import flask
from octoprint.plugin import (
	StartupPlugin, TemplatePlugin, SettingsPlugin, ShutdownPlugin, AssetPlugin, BlueprintPlugin
)


class MiniPlugin(StartupPlugin, TemplatePlugin, SettingsPlugin, ShutdownPlugin, AssetPlugin, BlueprintPlugin):

	@BlueprintPlugin.route('/echo', methods=['GET'])
	def my_echo(self):
		print('DZHOSHKUN', 'got', flask.request.values)
		if "text" not in flask.request.values:
			return flask.make_response("Expected a text to echo back.", 400)
		return flask.request.values["text"]

	def is_blueprint_protected(self):
		return False

	def on_after_startup(self):
		self._logger.info("Mini World! (more: %s)" % self._settings.get(["url"]))

	def get_settings_defaults(self):
		return dict(url="https://en.wikipedia.org/wiki/Hello_world")

	def get_template_configs(self):
		return [
			dict(type="navbar", custom_bindings=False),
			dict(type="settings", custom_bindings=False)
		]

	def on_shutdown(self):
		self._logger.info("Mini URL: %s" % self._settings.get(["url"]))

	def get_assets(self):
		return dict(
			js=["js/mini.js"]
		)


__plugin_implementation__ = MiniPlugin()
