from plexapi.myplex import MyPlexAccount
import argparse

parser = argparse.ArgumentParser(description='Plex Get Server Token')
parser.add_argument('email', help='Plex account email address')
parser.add_argument('password', help='Plex account password')
parser.add_argument('server', help='Name of the server to get the token for')
args = parser.parse_args()

account = MyPlexAccount(args.email, args.password)
accessToken = account.resource(args.server).accessToken
print(accessToken, end='')
