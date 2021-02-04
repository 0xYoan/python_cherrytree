"""Main module."""
import sys
import sqlite3
from tabulate import tabulate
import colorama
from colorama import Fore, Style
colorama.init()


def cprint(status, text):
    if status == "ERROR":
        print(Fore.RED + Style.BRIGHT + "[!] " + text + Style.RESET_ALL)
    elif status == "INFO":
        print(Fore.YELLOW + Style.BRIGHT + "[?] " + text + Style.RESET_ALL)
    elif status == "GOOD":
        print(Fore.GREEN + Style.BRIGHT + "[✓] " + text + Style.RESET_ALL)


class SqlManager:

    def __init__(self, filename):
        try:
            with open(filename):
                pass
        except IOError:
            cprint("ERROR", "File not found !")
            sys.exit(0)
        self.conn = sqlite3.connect(filename)
        self.cur = self.conn.cursor()

    def __del__(self):
        try:
            self.conn.commit()
            self.conn.close()
        except AttributeError:
            pass

    def show_nodes(self):
        try:
            self.cur.execute(
                "SELECT node_id,name,level FROM node ORDER BY node_id")
        except sqlite3.OperationalError:
            cprint("ERROR", "Can't find node table.")
            sys.exit(0)
        except sqlite3.DatabaseError:
            cprint("ERROR", "File is not a database.")
            sys.exit(0)
        results = self.cur.fetchall()
        tab = tabulate(results, headers=[
                       "node_id", "name", "level"], tablefmt="grid")
        print(tab)

    def change_node_name(self, new_name, node_id):
        info = (new_name, node_id)
        try:
            self.cur.execute("""
            UPDATE node
            SET name = ?
            WHERE node_id = ?
            """, info)
        except sqlite3.OperationalError:
            cprint("ERROR", "Can't change name.")
            sys.exit(0)

    def add_txt(self, txt, node_id):
        xml_data = '<?xml version="1.0" ?><node><rich_text>' + txt + '</rich_text></node>'
        info = (xml_data, node_id)
        try:
            self.cur.execute("""
            UPDATE node
            SET txt = ?
            WHERE node_id = ?
            """, info)
        except sqlite3.OperationalError:
            cprint("ERROR", "Can't add text into file.")
            sys.exit(0)

# FOR TESTING PURPOSE
if __name__ == '__main__':

    manager = SqlManager("/tmp/CTF_template.ctb")
    manager.show_nodes()
    manager.add_txt("Test", 34)
    manager.change_node_name("WebDav", 33)
