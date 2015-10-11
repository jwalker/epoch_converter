A simple python script which takes in multiple epoch times
and converts them to local time.

#### Help
```
python epoch_converter.py -h
usage: epoch_converter.py [-h] epochtime [epochtime ...]

Converts Epoch Time to localtime

positional arguments:
  epochtime   Example: 1444237762.53936

optional arguments:
  -h, --help  show this help message and exit
```

#### Usage
```
python epoch_converter.py 1442151157.86037 1442151159.6204 1442781286.83636 1442781417.54318 1442791680.71157 1442791688.01481 1444237762.53936 1444237769.40262
2015-09-13 06:32:37
2015-09-13 06:32:39
2015-09-20 13:34:46
2015-09-20 13:36:57
2015-09-20 16:28:00
2015-09-20 16:28:08
2015-10-07 10:09:22
2015-10-07 10:09:29
```
