# stop

*stdin top*

Show the most common stdin entries from a pipe.

## Usage

    usage: stop.py [-h] [-l L] [-e S]

    Show most common lines from stdin

    optional arguments:
      -h, --help       show this help message and exit
      -l L, --lines L  print L lines
      -e S, --every S  print every S seconds

## Example

The script [`test/test.py`](test/test.py) prints gaussian data. Pipe it into `stop` to see the most common values:

    test/test.py | ./stop.py
