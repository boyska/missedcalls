from splinter import Browser


def read_pass_file(fname):
    with open(fname) as buf:
        user = buf.readline().strip()
        pwd = buf.readline().strip()
    return user, pwd


user, password = read_pass_file('cred.txt')

with Browser('phantomjs') as b:
    b.visit('https://www.messagenet.com/')
    b.fill('userid', user)
    b.fill('password', password)
    b.find_by_css('#login button').click()

    b.visit('https://www.messagenet.com/voip/log/?chiamate=ricevute')
    rows = b.find_by_css('.log .statusKO')
    for r in rows:
        cells = r.find_by_tag('td')[1:3]
        print '\t'.join(map(lambda c: c.value, cells))
