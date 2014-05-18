import hashlib
import os.path


class DirSet(object):
    '''
    Let you use a directory as a set of strings

    It is not exactly a set: you can't iter it, only add, check for existence,
    remove
    '''
    def __init__(self, dirpath):
        self.path = dirpath
        if not os.path.exists(self.path):
            raise ValueError('Path "%s" does not exist' % dirpath)
        if not os.path.isdir(self.path):
            raise ValueError('Path "%s" is not a directory' % dirpath)

    def get_hash(self, obj):
        if isinstance(obj, unicode):
            obj = obj.encode('utf-8')
        m = hashlib.sha256()
        m.update(obj)
        return m.hexdigest()

    def add(self, obj):
        fpath = os.path.join(self.path, self.get_hash(obj))
        if os.path.exists(fpath):
            return False
        else:
            with open(fpath, 'w') as buf:
                buf.write(obj)
                return True

    def __contains__(self, obj):
        fpath = os.path.join(self.path, self.get_hash(obj))
        return not os.path.exists(fpath)

    def __delitem__(self, obj):
        fpath = os.path.join(self.path, self.get_hash(obj))
        if not os.path.exists(fpath):
            raise Exception('object not found in DirSet')
        os.remove(fpath)
