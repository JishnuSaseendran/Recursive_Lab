class Kangaroo(object):
    def __init__(self, contents=None):
        if contents == None:
            contents = []
        self.pouch = contents

    def put_in_pouch(self, item):
        self.pouch.append(item)

    def __str__(self):
        output_string = []
        for item in self.pouch:
            output_string.append(item)
        return str(output_string)

def main():
    print "Creating 'kanga' as Kangaroo object"
    kanga = Kangaroo()
    kanga.put_in_pouch('roo')

    print "Creating 'roo' as Kangaroo object"
    roo = Kangaroo()
    print "Putting 'roo' into 'kanga's pouch"
    print "Printing 'kanga'"
    print kanga

if __name__ == "__main__":
    main()
