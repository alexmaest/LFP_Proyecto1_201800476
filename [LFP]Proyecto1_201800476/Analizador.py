from Token import Token
from Imagen import Imagen
from Celda import Celda
import re

class Analizador:
    lexema = ""
    tokens = []
    state = 1
    row = 0
    column = 0
    generateImage = True
    types = Token("lexema", 0, 0, 0)
    aceptedSymbols = [",",";","{","}","="]

    Images = []
    Colors = []
    tempImage = []
    tempColors = []
    tempFilters = []
    tituloDetect = False
    anchoDetect = False
    altoDetect = False
    filasDetect = False
    columnasDetect = False
    celdasDetect = False
    singleCeldaDetect = False
    filtrosDetect = False
    singleFiltroDetect = False
    arrobaDetect = False

    def __init__(self, text):
        self.state = 1
        self.lexema = ""
        self.tokens = []
        self.row = 1
        self.column = 0
        self.generateImage = True
        text.append("$")
        #print(text)
        current = ""
        textLen = len(text)
        for index in range(textLen):
            #print("tituloDetect: " + str(self.tituloDetect) + ", anchoDetect: " + str(self.anchoDetect) + ", altoDetect: " + str(self.altoDetect) + ", filasDetect: " + str(self.filasDetect) + ", columnasDetect: " + str(self.columnasDetect) + ", celdasDetect: " + str(self.celdasDetect) + ", filtrosDetect: " + str(self.filtrosDetect) + ", singleFiltroDetect: " + str(self.singleFiltroDetect))
            columnLen = len(text[index])
            index2 = 0
            while index2 < columnLen:
                #print("index2: " + str(index2))
                current = text[index][index2]
                index2 += 1
                if self.state == 1:
                    if current.isalpha():
                        #print("Entra -> Current: " + str(current))
                        self.state = 2
                        self.column += 1
                        self.lexema += current
                        continue  
                    elif current.isdigit():
                        #print("Entra -> Current: " + str(current))
                        self.state = 3
                        self.column += 1
                        self.lexema += current
                        continue
                    elif current == "\"":
                        #print("Entra -> Current: " + str(current))
                        self.state = 4
                        self.column += 1
                        self.lexema += current
                        continue
                    elif current == "[":
                        contColor = - 1
                        colorCelda = ""
                        for i in range(50):
                            character = text[index][index2 + contColor]
                            #print("contColor: " + str(contColor) + ", character: " + str(character))
                            if str(character) != "]":
                                colorCelda += str(character)
                                contColor += 1
                            else:
                                colorCelda += str(character)
                                if self.isColor(colorCelda):
                                    self.column += len(colorCelda)
                                    self.lexema += colorCelda
                                    self.sortColors(colorCelda)
                                    self.tempColors.append(colorCelda)
                                    self.addToken(self.types.COLOR)
                                    index2 += len(colorCelda) - 1
                                    break
                        continue
                        """    
                    elif current == "#":
                        #print("Entra -> Current: " + str(current))
                        concatColor = text[index][index2 - 1] + text[index][index2] + text[index][index2 + 1] + text[index][index2 + 2] + text[index][index2 + 3] + text[index][index2 + 4] + text[index][index2 + 5]
                        #print("concatColor:" + str(concatColor))
                        if self.isColor(concatColor):
                            self.column += 7
                            self.lexema += concatColor
                            self.addToken(self.types.COLOR)
                            index2 += 6
                            continue
                    """
                    elif current in self.aceptedSymbols:
                        #print("Entra -> Current: " + str(current))
                        self.lexema += current
                        self.column += 1
                        self.tempImage.append(self.lexema)
                        self.addToken(self.types.SYMBOL)
                        cont = 0
                        for comma in self.tempImage:
                            if comma == ";":
                                cont += 1
                        #print("cont: " + str(cont))
                        if cont == 7:
                            #print("generateImage: " + str(self.generateImage) + ", tituloDetect: " + str(self.tituloDetect) + ", anchoDetect: " + str(self.anchoDetect) + ", altoDetect: " + str(self.altoDetect) + ", filasDetect: " + str(self.filasDetect) + ", columnasDetect: " + str(self.columnasDetect) + ", celdasDetect: " + str(self.celdasDetect) + ", filtrosDetect: " + str(self.filtrosDetect) + ", singleFiltroDetect: " + str(self.singleFiltroDetect))
                            if self.generateImage == True and self.tituloDetect == True and self.anchoDetect == True and self.altoDetect == True and self.filasDetect == True and self.columnasDetect == True and self.celdasDetect == True and self.filtrosDetect == True and self.singleFiltroDetect == True:
                                titulo = ""
                                ancho = 0
                                alto = 0
                                filas = 0
                                columnas = 0

                                contArray = 1
                                for element in self.tempImage:
                                    if contArray == 3:
                                        titulo = element
                                    elif contArray == 7:
                                        ancho = element
                                    elif contArray == 11:
                                        alto = element
                                    elif contArray == 15:
                                        filas = element
                                    elif contArray == 19:
                                        columnas = element
                                    
                                    contArray += 1
                                """
                                print("COLORES")
                                for c in self.tempColors:
                                    print(c)
                                print("FILTROS")
                                for f in self.tempFilters:
                                    print(f)
                                """
                                self.Images.append(Imagen(titulo, ancho, alto, filas, columnas, self.Colors, self.tempFilters))
                                self.tempFilters = []
                                self.tempColors = []
                                self.Colors = []
                                self.tempImage = []
                        continue
                    elif current == " ":
                        #print("Entra -> Current: " + str(current))
                        self.column += 1
                        self.state = 1
                        continue
                    elif current == "\n":
                        #print("Entra -> Current: " + str(current))
                        self.row += 1
                        self.column = 0
                        self.state = 1
                        continue
                    elif current == "\r":
                        #print("Entra -> Current: " + str(current))
                        self.state = 1
                        continue
                    elif current == "\t":
                        #print("Entra -> Current: " + str(current))
                        self.column += 5
                        self.state = 1
                        continue
                    elif current == "@":
                        sign = text[index][index2 - 1] + text[index][index2] + text[index][index2 + 1] + text[index][index2 + 2]
                        if sign == "@@@@":
                            self.lexema += sign
                            self.column += 4
                            self.addToken(self.types.SYMBOL)
                            #print("---------------------------ARROBA DETECT---------------------------")
                            self.tempColors = []
                            self.tempImage = []
                            self.tempFilters = []
                            self.tituloDetect = False
                            self.anchoDetect = False
                            self.altoDetect = False
                            self.filasDetect = False
                            self.columnasDetect = False
                            self.celdasDetect = False
                            self.filtrosDetect = False
                            self.singleFiltroDetect = False
    
                            index2 += 3
                            continue
                        else:
                            self.lexema += current
                            self.column += 1
                            self.generateImage = False
                            self.addToken(self.types.UNKNOWN)
                            continue  
                    elif current == "$" and index == textLen - 1:
                        #self.printTokens()
                        print("\n")
                        print("Analisis Finalizado mi pai")
                        print("\n")
                        break
                    else:
                        #print("Entra -> Current: " + str(current))
                        self.lexema += current
                        self.column += 1
                        self.generateImage = False
                        self.addToken(self.types.UNKNOWN)
                        continue

                elif self.state == 2:
                    #print("Entra -> Current: " + str(current))
                    if current.isalpha():
                        self.state = 2
                        self.column += 1
                        self.lexema += current
                        continue
                    else:
                        if self.isReservedWord(self.lexema):
                            lexemaLower = self.lexema.lower()
                            #print("lexemaLower: " + str(lexemaLower))
                            if lexemaLower == "titulo":
                                self.tituloDetect = True
                            if lexemaLower == "ancho":
                                self.anchoDetect = True
                            if lexemaLower == "alto":
                                self.altoDetect = True
                            if lexemaLower == "filas":
                                self.filasDetect = True
                            if lexemaLower == "columnas":
                                self.columnasDetect = True
                            if lexemaLower == "celdas":
                                self.celdasDetect = True
                            if lexemaLower == "filtros":
                                self.filtrosDetect = True
                            if lexemaLower == "mirrorx" or lexemaLower == "mirrory" or lexemaLower == "doublemirror":
                                self.singleFiltroDetect = True
                                self.tempFilters.append(lexemaLower)
                            self.tempImage.append(self.lexema)
                            self.addToken(self.types.RESERVEDWORD)
                            index2 -= 1
                            continue
                        elif self.isBooleanWord(self.lexema):
                            self.tempImage.append(self.lexema)
                            self.addToken(self.types.BOOLEAN)
                            index2 -= 1
                            continue
                        else:
                            self.lexema += current
                            self.column += 1
                            self.generateImage = False
                            self.addToken(self.types.UNKNOWN)
                            continue

                elif self.state == 3:
                    if current.isdigit():
                        self.state = 3
                        self.column += 1
                        self.lexema += current
                        continue
                    else:
                        self.tempImage.append(self.lexema)
                        self.addToken(self.types.NUMBER)
                        index2 = index2 - 1
                        continue

                elif self.state == 4:
                    if current != "\"":
                        self.state = 4
                        self.column += 1
                        self.lexema += current
                        continue
                    elif current == "\"":
                        self.lexema += current
                        self.column += 1
                        self.tempImage.append(self.lexema)
                        self.addToken(self.types.STRING)
                        continue
            
    def addToken(self, type):
        self.tokens.append(Token(self.lexema, type, self.row, self.column))
        self.lexema = ""
        self.state = 1
      
    def isReservedWord(self, text):
        text2 = text.lower()
        isReserved = False
        reservedWords = ["titulo","ancho","alto","filas","columnas","celdas","filtros","mirrorx","mirrory","doublemirror"]

        if text2 in reservedWords:
            isReserved = True
        return isReserved

    def isBooleanWord(self, text):
        text2 = text.lower()
        isBoolean = False
        booleanWords = ["true","false"]

        if text2 in booleanWords:
            isBoolean = True
        return isBoolean
    
    def isColor(self, color):
        lowerColor = color.lower()
        regex = "(\[([0-9]+\,){2}(true|false)\,(#[A-Fa-f0-9]{6})\])"
        if re.search(regex, lowerColor):
            return True
        else:
            return False
    
    def printTokens(self):
        tempRow = 0
        for token in self.tokens:
            if token.row != tempRow:
                print("\n")
                print("Lexema: " + str(token.lexema) + ", tipo: " + str(token.type) + ", fila: " + str(token.row) + ", columna: " + str(token.column))
                tempRow = token.row
            else:
                print("Lexema: " + str(token.lexema) + ", tipo: " + str(token.type) + ", fila: " + str(token.row) + ", columna: " + str(token.column))

    def sortColors(self, celda):
        #[5,8,TRUE,#000000]
        celda2 = celda.replace("[","")
        celda3 = celda2.replace("]","")
        singleColorArray = celda3.split(",")
        posX = singleColorArray[0]
        posY = singleColorArray[1]
        boolean = singleColorArray[2]
        color = singleColorArray[3]
        #print("posX: " + str(posX) + ", posY: " + str(posY) + ", boolean: " + str(boolean) + ", color: " + str(color))
        self.Colors.append(Celda(posX, posY, boolean, color))

    def getImages(self):
        return self.Images
    
    def getTokens(self):
        return self.tokens