# "open html content in w3m"
import config
from util.WebtopUtil import WebtopUtil


if WebtopUtil.isPackageInstalled("w3m"):
    html = config.mainWindow.fineTuneTextForWebBrowserDisplay()
    config.mainWindow.cliTool("w3m -T text/html -o confirm_qq=false", html)
else:
    config.mainWindow.printToolNotFound("w3m")
