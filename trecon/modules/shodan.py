class shodan():
    def add_parser(self, parser):
        shodanparser = parser.add_parser('shodan', help='query shodan.')
        shodanparser.set_defaults(func=shodan.query)
        return shodanparser

    def query():
        print("query func shodan")
