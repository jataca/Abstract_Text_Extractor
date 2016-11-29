class InstrumentType:
    """The Base Class"""
    #pass # The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.

    def __init__(self):
       self.type = ''
       self.date = ''
       self.amount = ''
       self.batch = ''
       self.docid = ''

class Lien(InstrumentType):

    def __init__(self):
        #super().__init__()
        InstrumentType.__init__(self)
        self.type = 'Lien'
        self.address = '' # claiment address


class Mortgage(InstrumentType):

    def __init__(self):
        InstrumentType.__init__(self)
        self.type = 'Mortgage'
        self.mortgager = ''
        self.address = '' #mortgagee address


x = InstrumentType()
y = Lien()
