#!/usr/bin/env python

from os import system
from argparse import ArgumentParser
from threading import Timer
from subprocess import check_output
from collections import Counter


class StdinParser:
    def __init__(self, lines, every):
        self._lines = lines
        self._every = every
        self._timer = None
        self._counter = Counter()

    def parse(self):
        self._printdata()
        try:
            while True:
                self._counter[raw_input()] += 1
        except:
            self._printdata(start_timer=False)
            if self._timer:
                self._timer.cancel()

    def _printdata(self, start_timer=True):
        rows, columns = self._getsize()
        system('clear')
        print '\n'.join('%5d  %s' % (n, s)[:columns] for (s, n)
                        in self._counter.most_common(max(rows-1, self._lines)))
        if start_timer:
            self._timer = Timer(self._every, self._printdata)
            self._timer.start()

    def _getsize(self):
        command = 'stty size </dev/tty 2>/dev/null'
        return map(int, check_output(command, shell=True).split())


if __name__ == '__main__':
    parser = ArgumentParser(description='Show most common lines from stdin')
    parser.add_argument('-l', '--lines', metavar='L', type=int, default=10, help='print L lines')
    parser.add_argument('-e', '--every', metavar='S', type=float, default=1, help='print every S seconds')
    args = parser.parse_args()
    StdinParser(args.lines, args.every).parse()

