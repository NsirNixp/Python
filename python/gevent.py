#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
import gevent.monkey

gevent.monkey.patch_all()     

 tasks = [gevent.spawn(task, rQueue, wQueue, ackQueue) for i in xrange(50) ]
    gevent.joinall(tasks)

def task(rQueue, wQueue, ackQueue):
    while True:
        try:
            handle = Handle(wQueue)
            while True:
                msg = rQueue.get()
                try:
                    handle.handle(msg)
                except Exception,e:
                    errMsg=''
                    errss=traceback.format_exc().split('\n')
                    for ers in errss:
                        errMsg = errMsg + str(ers)
                    logger.error('task handler() error  %s',errMsg)
                ackQueue.put(msg) # ack anyway!
        except BaseException, e:
            logger.warn('Exception:%s', str(e))
            traceback.print_exc()
            break