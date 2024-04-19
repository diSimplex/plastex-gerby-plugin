
from plasTeX.Logging import getLogger

pluginLog = getLogger('plugin.loading')

from gerbyPlasTeXPlugin.Renderers.Gerby.Config \
  import addConfig as addRendererConfig

def addConfig(config):
  print("Hello from Gerby Config PlasTeX Plugin : addConfig")
  addRendererConfig(config)

def updateConfig(config, fileName):
  pluginLog.info("Hello from Gerby Config PlasTeX Plugin : updateConfig")

def initPlugin(config, fileName, texStream, texDocument):
  pluginLog.info("Hello from Gerby Config PlasTeX Plugin : initPlugin")
  from gerbyPlasTeXPlugin import BaseLaTeXMacros
  texDocument.context.importMacros(vars(BaseLaTeXMacros))
