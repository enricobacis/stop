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

The script [`test/test.py`](test/test.py) prints gaussian data with mean *100*. Pipe it into `stop` to see the most common values and their count:

    test/test.py | ./stop.py

Output:

    1107  108
    1097  100
    1082  97
    1057  99
    1056  93
    1050  113
    1047  114
    1043  106
    1038  104
    1037  91
    1036  92
    1035  101

