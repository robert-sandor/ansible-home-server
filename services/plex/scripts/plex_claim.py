from plexapi.myplex import MyPlexAccount
import argparse

parser = argparse.ArgumentParser(description='Plex Bootstrap Script')
parser.add_argument('email', help='Plex account email address')
parser.add_argument('password', help='Plex account password')
args = parser.parse_args()

account = MyPlexAccount(args.email, args.password)
print(account.claimToken(), end='')
