class CommandManager:
    
    def __init__(self):
        self.name = "cmd-manager"
        self.commands = []
        self.executes = {}
        self.info = {}
        
    def addCommand(self, cmd, ex, info):
        self.commands.append(cmd)
        self.executes[cmd] = ex
        self.info[cmd] = info
    
    def executeCommand(self, cmd):
        ex = self.executes[cmd]
        return exec(ex)