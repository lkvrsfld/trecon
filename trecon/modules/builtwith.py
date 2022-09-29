class builtwith():
    def add_parser(self, parser):
        bwparser = parser.add_parser('builtwith', help='query builtwith.')
        bwparser.set_defaults(func=builtwith.query)
        return bwparser

    def query():
        print("query func builtwith")
