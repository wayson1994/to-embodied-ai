# gdbcmd.py
import gdb
class HelloCmd(gdb.Command):
    def __init__(self): super().__init__("hello", gdb.COMMAND_USER)
    def invoke(self, arg, from_tty): print("Hello from GDB Python!")
HelloCmd()