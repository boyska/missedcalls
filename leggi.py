import json
import sys
from itertools import imap

from splinter import Browser

from dirset import DirSet


def read_pass_file(fname):
    with open(fname) as buf:
        user = buf.readline().strip()
        pwd = buf.readline().strip()
    return user, pwd


def get_calls(user, password):
    with Browser('phantomjs') as b:
        b.visit('https://www.messagenet.com/')
        b.fill('userid', user)
        b.fill('password', password)
        b.find_by_css('#login button').click()

        b.visit('https://www.messagenet.com/voip/log/?chiamate=ricevute')
        rows = b.find_by_css('.log .statusKO')
        for r in rows:
            cells = r.find_by_tag('td')[1:3]
            yield tuple(imap(lambda c: c.value, cells))


def save_calls(calls, datadir):
    s = DirSet(datadir)
    for call in imap(lambda t: '\t'.join(t), calls):
        if s.add(call):  # wasn't existing before
            print 'NEW: %s' % call


if __name__ == '__main__':
    conf = json.load(open('defaultconf.json'))
    if len(sys.argv) == 2:
        conf.update(json.load(open(sys.argv[1])))
    user, password = read_pass_file(conf['credfile'])
    calls = tuple(get_calls(user, password))
    save_calls(calls, conf['datadir'])
