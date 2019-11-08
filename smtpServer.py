#!/usr/bin/env python
# coding : utf-8
#
"""simple python smtp server for test purpose """

from datetime import datetime
import asyncore
from smtpd import SMTPServer, SMTPChannel
import sys

# don't forget to create a mail/ folder
folderForMail = "mail/"
defered_list = ['user10']
blocked_list = ['user11']

class MyChannel(SMTPChannel):
    def smtp_RCPT(self, arg):
        if not self.seen_greeting:
            self.push('503 Error: send HELO first');
            return
        print('===> RCPT', arg, file=DEBUGSTREAM)
        if not self.mailfrom:
            self.push('503 Error: need MAIL command')
            return
        syntaxerr = '501 Syntax: RCPT TO: <address>'
        if self.extended_smtp:
            syntaxerr += ' [SP <mail-parameters>]'
        if arg is None:
            self.push(syntaxerr)
            return
        arg = self._strip_command_keyword('TO:', arg)
        address, params = self._getaddr(arg)
        if not address:
            self.push(syntaxerr)
            return
        if not self.extended_smtp and params:
            self.push(syntaxerr)
            return
        self.rcpt_options = params.upper().split()
        params = self._getparams(self.rcpt_options)
        if params is None:
            self.push(syntaxerr)
            return
        # XXX currently there are no options we recognize.
        if len(params.keys()) > 0:
            self.push('555 RCPT TO parameters not recognized or not implemented')
            return
        self.rcpttos.append(address)
        for rcpt in defered_list:
            if address.startswith(rcpt):
                self.push('452 No space')
                return
        for rcpt in blocked_list:
            if address.startswith(rcpt):
                self.push('510 Check the address')
                return
        print('recips:', self.rcpttos, file=DEBUGSTREAM)
        self.push('250 OK')


class EmlServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data):
        filename = '%s-%d.eml' % (datetime.now().strftime('%Y%m%d%H%M%S'),
                self.no)
        with open(folderForMail+filename, 'w') as f:
            f.write(data)
        print('%s saved.' % filename)
        self.no += 1

    def __init__(self):
        self.channel_class =  MyChannel()


def run(server, host):
    foo = EmlServer((server, int(port)), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':

        if len(sys.argv) != 3:
                print("USAGE: host port")
        else:
                _, server, port = sys.argv
                run(server,port)