class builtwith():
    def add_parser(self, parser):
        bwparser = parser.add_parser('builtwith', help='query builtwith.')
        bwsubparser = bwparser.add_subparsers()
        return bwsubparser

    def query():
        print("query func builtwith")
