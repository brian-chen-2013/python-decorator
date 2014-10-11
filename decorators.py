class dec:
    def route(self, rargs='k', qargs='l'):
        print "decorator runing..."
        def deco(func):
            def _deco(*args, **kwargs):
                print "route decorator, before called, rargs = %s, gargs = %s" % (rargs, qargs)
                ret = func(*args, **kwargs)
                print "route decorator, after called"
                return ret
            return _deco
        return deco

    def freedec(self, *dargs, **dkwargs):
        def deco(func):
            def _deco(*args, **kwargs):
                print "freedec decorator, before called"
                print dargs
                print dkwargs
                ret = func(*args, **kwargs)
                print "freedec decorator, after called"
                return ret
            return _deco
        return deco

decco = dec()

@decco.route("route-parameters")
def x(a,b):
    print 'a,b = ', a, b
    return 1

print "-------------------------"
r = x('aaa', 'bbb')
print r


@decco.freedec("a","b","c", qq="1",)
@decco.route("route-parameters")
def y(a,b):
    print 'a,b = ', a, b
    return 1

print "-------------------------"
r = y('aaa', 'bbb')
print r


@decco.freedec("a","b","c", qq="1",)
def z(a,b):
    print 'a,b = ', a, b
    return 1

print "-------------------------"
r = z('aaa', 'bbb')
print r
