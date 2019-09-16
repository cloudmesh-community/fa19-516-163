from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.eshell3.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class Eshell3Command(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_eshell3(self, args, arguments):
        """
        ::

          Usage:
                eshell3 --file=FILE
                eshell3 --name=NAME
                eshell3 list

          This command does some useful things.

          Arguments:
              FILE   a file name
              NAME   a new file name

          Options:
              -f      specify the file

        """
        arguments.FILE = arguments['--file'] or None
        arguments.NAME = arguments['--name'] or None

        VERBOSE(arguments)

        m = Manager()

        if arguments.FILE:
            print("option file")
            m.list(path_expand(arguments.FILE))

        if arguments.NAME:
            print(f"option name")
            m.list(arguments.NAME)

        elif arguments.list:
            print("option list")
            m.list("just calling list without parameter")

        Console.error("This is just a sample")
        return ""
