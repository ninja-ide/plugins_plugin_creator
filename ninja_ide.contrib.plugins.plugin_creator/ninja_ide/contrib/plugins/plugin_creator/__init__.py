from .plugin_creator import PluginCreatorPlugin as _PluginCreatorPlugin


PluginCreatorPlugin = _PluginCreatorPlugin()


def activate():
    PluginCreatorPlugin.activate()


__all__ = ["PluginCreatorPlugin"]