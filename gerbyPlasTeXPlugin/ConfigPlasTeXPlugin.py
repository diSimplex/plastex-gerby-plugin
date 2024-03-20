
from plasTeX.Logging import getLogger

pluginLog = getLogger('plugin.loading')

from gerbyPlasTeXPlugin.Renderers.Gerby.Config \
  import addConfig as addRendererConfig

def addConfig(config):
  print("Hello from Config PlasTeX Plugin : addConfig")
  addRendererConfig(config)

def updateCommandLineOptions(data):
  pluginLog.info("Hello from Config PlasTeX Plugin : updateCommandLineOptions")

def initPlugin(config, texStream, texDocument):
  pluginLog.info("Hello from Config PlasTeX Plugin : initPlugin")
  from gerbyPlasTeXPlugin import BaseLaTeXMacros
  texDocument.context.importMacros(vars(BaseLaTeXMacros))
