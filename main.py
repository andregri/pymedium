import requests
import os
import medium

def main():
    client = medium.Client(os.environ.get('MEDIUM_ACCESS_TOKEN'))

if __name__ == "__main__":
    main()