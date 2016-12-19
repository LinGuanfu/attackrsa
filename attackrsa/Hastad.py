#!/usr/bin/env python

import gmpy2 as gmpy
import Utils

class Hastad(object):
    '''
    Hastad Broadcast Attack
    '''
    def __init__(self, ns, e, cs):
        '''
        ns: array of n
        e: public exponent
        cs: array of cipher text
        '''
        self.ns = ns
        self.e = e
        self.cs = cs
    def decrypt(self,precision):
        s = Utils.CRT(self.ns, self.cs)
        #gmpy.get_context().precision = precision
        if s == 'no inverse':
            print self.ns
        else:
            pt,perfect = gmpy.iroot(s, self.e)
            if perfect:
                print 'hello,it works:'
                return pt
            else:
                pass
                #print "Cannot find %dth root of %s" % (self.e, s),pt 