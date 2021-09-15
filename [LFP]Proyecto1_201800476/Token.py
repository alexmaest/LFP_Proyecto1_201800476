class Token:
    lexema = ""
    type = 0
    row = 0
    column = 0
 
    RESERVEDWORD = "Palabra reservada"
    STRING = "Cadena"
    NUMBER = "Numero"
    COLOR = "Color"
    SYMBOL = "Simbolo"
    BOOLEAN = "Booleano"
    UNKNOWN = "Desconocido"

    def __init__(self, lexema, type, row, column):
        self.lexema = lexema
        self.type = type
        self.row = row
        self.column = column

    def getLexema(self):
        return self.lexema
    
    def getRow(self):
        return self.row
    
    def getColumns(self):
        return self.column
    
    def getType(self):
        if self.type == self.RESERVEDWORD:
            return "PALABRA_RESERVADA"
        elif self.type == self.STRING:
            return "CADENA"
        elif self.type == self.NUMBER:
            return "NUMERO"
        elif self.type == self.ID:
            return "ID"
        elif self.type == self.REST:
            return "RESTO"
        elif self.type == self.COLOR:
            return "COLOR"
        elif self.type == self.SYMBOL:
            return "SIMBOLO" 