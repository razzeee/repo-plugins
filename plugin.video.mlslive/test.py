#!/usr/bin/python

import mlslive, sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-u', '--user', type='string', dest='user',
                  help="Username for authentication")
parser.add_option('-p', '--password', type='string', dest='password',
                  help="Password for authentication")
parser.add_option('-g', '--game', type='string', dest='game',
                  help="Game to display")
parser.add_option('-m', '--month', type='string', dest='month',
                  help="List games of the month")
parser.add_option('-x', '--x-forward-for', type='string', dest='xff',
                  help="X-Forward-For header value")

(options, args) = parser.parse_args()


my_mls = mlslive.MLSLive()

if options.user != None and options.password != None:
    if not my_mls.login(options.user, options.password, options.xff):
        print "*** Unable to authenticte with MLS live. please set username and password."
        sys.exit(1)
    else:
        print "Logon successful..."

if options.game == None:
    games = my_mls.getGames(xff = options.xff)
    for game in games:
        game_str = my_mls.getGameString(game, 'at')
        print '\t{0}) {1}'.format(game['optaId'], game_str) 
else:
    streams = my_mls.getStreams(options.game, options.xff)
    if streams == None:
        print "Unable to get streams..."
        sys.exit(1)
    for stream in streams.keys():
        print stream + ' ' + streams[stream]
sys.exit(0)