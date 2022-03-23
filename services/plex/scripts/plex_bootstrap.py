from ast import arg
import re
from time import sleep
from venv import create
from plexapi.myplex import MyPlexAccount
from plexapi.exceptions import NotFound, BadRequest
import argparse

def createLibraryWithRetries(name, type, location, language, agent, scanner):
    retries = 5

    while retries > 0:
        try:
            plexServer.library.add(
                name=name, 
                type=type, 
                location=location, 
                language=language, 
                agent=agent, 
                scanner=scanner)
            return
        except BadRequest:
            print('Got exception, will retry in 5 seconds ...')
            sleep(5)
            retries = retries - 1
            print('Retrying ... %d tries left' % retries)


def createLibrary(type, location):
    namesByType = { 'movie': 'Movies', 'show': 'Series', 'artist': 'Music' }
    agentByType = { 'movie': 'tv.plex.agents.movie', 'show': 'tv.plex.agents.series', 'artist': 'tv.plex.agents.music' }
    scannerByType = { 'movie': 'Plex Movie', 'show': 'Plex TV Series', 'artist': 'Plex Music' }
    languageByType = { 'movie': 'en-US', 'show': 'en-US', 'artist': 'en' }

    name = namesByType[type]
    
    try:
        print('Checking for existing library %s' % name)
        plexServer.library.section(name)
        print('Library %s already exists' % name)
    except NotFound:
        print('Library %s not found, attempting to create ...' % name)
        createLibraryWithRetries(
            name=name, 
            type=type, 
            location=location, 
            language=languageByType[type], 
            agent=agentByType[type], 
            scanner=scannerByType[type])
        print('Created Library %s' % name)


parser = argparse.ArgumentParser(description='Plex Bootstrap Script')
parser.add_argument('email', help='Plex account email address')
parser.add_argument('password', help='Plex account password')
parser.add_argument('server', help='Name of the server to bootstrap')
parser.add_argument('movies', help='Location of the Movies library')
parser.add_argument('series', help='Location of the Series library')
parser.add_argument('music', help='Location of the Music library')
args = parser.parse_args()

print('logging in ...')
account = MyPlexAccount(args.email, args.password)
print('logged in ...')
print('connecting to %s ...' % args.server)
plexServer = account.resource(args.server).connect()
print('connected to %s ...' % args.server)

createLibrary('movie', args.movies)
createLibrary('show', args.series)
createLibrary('artist', args.music)
