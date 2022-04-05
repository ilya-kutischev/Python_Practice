import threading

_lock = threading.RLock()

def _acquireLock():
     if _lock:
        _lock.acquire()

def _releaseLock():
    if _lock:
        _lock.release()


"""def _nameToLevel(name):
    levels = [['CRITICAL', CRITICAL],
    ['FATAL', FATAL],
    ['ERROR', ERROR],
    ['WARN', WARNING],
    ['WARNING', WARNING],
    ['INFO', INFO],
    ['DEBUG', DEBUG],
    ['NOTSET', NOTSET]]
    for level in levels:
        if name == level[0]:
            return level[1]
    raise ValueError("Unknown level: %r" % level) """

_nameToLevel = {
    'CRITICAL': 50,
    'FATAL': 50,
    'ERROR': 40,
    'WARN': 30,
    'WARNING': 30,
    'INFO': 20,
    'DEBUG': 10,
    'NOTSET': 0,
}

def _checkLevel(level):
    if isinstance(level, int):
        rv = level
    elif str(level) == level:
        if level not in _nameToLevel:
            raise ValueError("Unknown level: %r" % level)
        rv = _nameToLevel[level]
    else:
        raise TypeError("Level not an integer or a valid string: %r" % level)
    return rv


class Filterer(object):
    def filter(self, record):
        rv = True
        for f in self.filters:
            if hasattr(f, 'filter'):
                result = f.filter(record)
            else:
                result = f(record)
            if not result:
                rv = False
                break
        return rv


class Logger(Filterer):
    def callHandlers(self, record):
        c = self
        found = 0
        while c:
            for hdlr in c.handlers:
                found = found + 1
                if record.levelno >= hdlr.level:
                    hdlr.handle(record)
            if not c.propagate:
                c = None
            else:
                c = c.parent
        if (found == 0):
            if lastResort:
                if record.levelno >= lastResort.level:
                    lastResort.handle(record)

    def getEffectiveLevel(self):
        logger = self
        while logger:
            if logger.level:
                return logger.level
            logger = logger.parent
        return NOTSET

    def isEnabledFor(self, level):
        try:
            return self._cache[level]
        except KeyError:
            _acquireLock()
            if self.manager.disable >= level:
                is_enabled = self._cache[level] = False
            else:
                is_enabled = self._cache[level] = level >= self.getEffectiveLevel()
            _releaseLock()
        return is_enabled

    def callHandlers(self, record):
        c = self
        found = 0
        while c:
            for hdlr in c.handlers:
                found = found + 1
                if record.levelno >= hdlr.level:
                    hdlr.handle(record)

    def handle(self, record):
        if (not self.disabled) and self.filter(record):
            self.callHandlers(record)




class Handler(Filterer):
    # ...
    def handle(self, record):
        rv = self.filter(record)
        if rv:
            self.acquire()
            try:
                self.emit(record)
            finally:
                self.release()
        return rv


class RootLogger(Logger):
    def __init__(self, level):
        Logger.__init__(self, "root", level)


if __name__ == '__main__':
    logging = Logger()
    print('set 1')
    logging.warning("To iterate is %s, to recurse %s", "human", "divine")