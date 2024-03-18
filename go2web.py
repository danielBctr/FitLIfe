#!/usr/bin/env python3

import sys




def print_help():
    print("  go2web -u    Make an HTTP request to the specified <URL> and print the response")
    print("  go2web -s    Make an HTTP request to search the <search-term> using Google and print top 10 results")
    print("  go2web -h    List available commands")


def main():
    args = sys.argv[1:]
    if len(args) < 2 or args[0] not in ['-u', '-s', '-h']:
        print_help()
        return



if __name__ == "__main__":
    main()
