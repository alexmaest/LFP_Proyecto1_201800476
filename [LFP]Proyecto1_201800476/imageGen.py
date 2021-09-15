import imgkit
class imageGen:
    def __init__(self, images):      
        self.images = images
        imagenes = images      
 
        for image in imagenes:
            title = image.titulo
            weight = image.ancho
            height = image.alto
            rows = image.filas
            columns = image.columnas
            colors = image.celdas

            lenRows = int(image.filas)
            lenColumns =  int(image.columnas)
            imageName0 =  str(image.titulo)
            imageName1 = imageName0.replace("\"", "")
            imageName = imageName1.lower()

            html = open("template/images/" + str(imageName) + "_normal.html", "w")
            html.write("""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                    <style>
                    table {
                width: 30%;
                border-collapse: collapse;
                }
                td {
                position: relative;
                border: 1px solid rgb(61, 61, 61);
                
                }

                td:after {
                content: '';
                display: block;
                margin-top: 100%;
                }
                td .content {
                position: absolute;
                top: 0;
                bottom: 0;
                left: 0;
                right: 0;
                }
                    </style>
                </head>
                <body>
                <table>""")
            value = 0
            for contY in range(lenRows):
                html.write("<tr>")
                for contX in range(lenColumns):
                    if value != contY:
                        html.write("</tr>")
                        value = contY
                    Encontrado = False
                    for color in image.celdas:
                        hexa = color.hexColor
                        booleano = color.boolean
                        celdaX = color.posX
                        celdaY = color.posY
                        if int(contX) == int(celdaX) and int(contY) == int(celdaY):
                            #print("x: " + str(contX) + ", y: " + str(contY) + ", celdaX: " + str(celdaX) + ", celdaY: " +  str(celdaY))
                            boo = booleano.lower() 
                            if boo == "true":

                                Encontrado = True
                                #CrearCeldaPintada
                                html.write("""<td><div style= "background-color: """ + str(hexa) + """;" class="content"></div></td>""")

                            else:
                                Encontrado = True
                                html.write("""<td><div style= "background-color: #FFFFFF;" class="content"></div></td>""")
                                #CrearCeldaVacias
                        #else:
                            #continue
                    if Encontrado == False:
                        html.write("""<td><div style= "background-color: #FFFFFF;" class="content"></div></td>""")

            html.write("""</table>
                </body>
                </html>
            """)
            html.close()
            options = {
                'format': 'png',
                'crop-h': '800',
                'crop-w': '320',
                'crop-x': '0',
                'crop-y': '0',
                'encoding': "UTF-8",
                'custom-header': [
                    ('Accept-Encoding', 'gzip')
                ]
            }
            imgkit.from_file("template/images/" + str(imageName) + "_normal.html", "template/images/png/" + str(imageName) + "_normal.jpg", options=options)

            filthers = image.filtros
            for filther in filthers:
                if filther == "mirrorx":
                    html = open("template/images/" + str(imageName) + "_mirrorx.html", "w")
                    html.write("""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                    <style>
                    table {
                width: 30%;
                border-collapse: collapse;
                }
                td {
                position: relative;
                border: 1px solid rgb(61, 61, 61);
                
                }

                td:after {
                content: '';
                display: block;
                margin-top: 100%;
                }
                td .content {
                position: absolute;
                top: 0;
                bottom: 0;
                left: 0;
                right: 0;
                }
                    </style>
                </head>
                <body>
                <table>""")

                    value2 = 0
                    for contY in range(lenRows):
                        html.write("<tr>")
                        contX = lenColumns - 1
                        while contX >= 0:

                            if value2 != contY:
                                html.write("</tr>")
                                value2 = contY
                            Encontrado = False
                            for color in image.celdas:
                                hexa = color.hexColor
                                booleano = color.boolean
                                celdaX = color.posX
                                celdaY = color.posY
                                if int(contX) == int(celdaX) and int(contY) == int(celdaY):
                                    #print("x: " + str(contX) + ", y: " + str(contY) + ", celdaX: " + str(celdaX) + ", celdaY: " +  str(celdaY))
                                    boo = booleano.lower() 
                                    if boo == "true":
                                        Encontrado = True
                                        #CrearCeldaPintada
                                        html.write("""<td><div style= "background-color: """ + str(hexa) + """;" class="content"></div></td>""")
                                        contX -= 1
                                    else:
                                        Encontrado = True
                                        html.write("""<td><div style= "background-color: #FFFFFF;" class="content"></div></td>""")
                                        contX -= 1
                                        #CrearCeldaVacias
                                #else:
                                    #continue
                            if Encontrado == False:
                                html.write("""<td><div style= "background-color: #FFFFFF;" class="content"></div></td>""")
                                contX -= 1

                    html.write("""</table>
                    </body>
                    </html>""")
                    html.close()
                    options = {
                        'format': 'png',
                        'crop-h': '800',
                        'crop-w': '320',
                        'crop-x': '0',
                        'crop-y': '0',
                        'encoding': "UTF-8",
                        'custom-header': [
                            ('Accept-Encoding', 'gzip')
                        ]
                    }
                    imgkit.from_file("template/images/" + str(imageName) + "_mirrorx.html", "template/images/png/" + str(imageName) + "_mirrorx.jpg", options=options)

                elif filther == "mirrory":
                    html = open("template/images/" + str(imageName) + "_mirrory.html", "w")
                    html.write("""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                    <style>
                    table {
                width: 30%;
                border-collapse: collapse;
                }
                td {
                position: relative;
                border: 1px solid rgb(61, 61, 61);
                
                }

                td:after {
                content: '';
                display: block;
                margin-top: 100%;
                }
                td .content {
                position: absolute;
                top: 0;
                bottom: 0;
                left: 0;
                right: 0;
                }
                    </style>
                </head>
                <body>
                <table>""")
                    value3 = 0
                    contY = lenRows - 1
                    while contY >= 0:
                        html.write("<tr>")
                        for contX in range(lenColumns):
                            if value3 != contY:
                                html.write("</tr>")
                                value3 = contY
                            Encontrado = False
                            for color in image.celdas:
                                hexa = color.hexColor
                                booleano = color.boolean
                                celdaX = color.posX
                                celdaY = color.posY
                                if int(contX) == int(celdaX) and int(contY) == int(celdaY):
                                    #print("x: " + str(contX) + ", y: " + str(contY) + ", celdaX: " + str(celdaX) + ", celdaY: " +  str(celdaY))
                                    boo = booleano.lower() 
                                    if boo == "true":
                                        Encontrado = True
                                        #CrearCeldaPintada
                                        html.write("""<td><div style= "background-color: """ + str(hexa) + """;" class="content"></div></td>""")
                                    else:
                                        Encontrado = True
                                        html.write("""<td><div style= "background-color: #FFFFFF;" class="content"></div></td>""")
                                        #CrearCeldaVacias
                                #else:
                                    #continue
                            if Encontrado == False:
                                html.write("""<td><div style= "background-color: #FFFFFF;" class="content"></div></td>""")
                        contY -= 1

                    html.write("""</table>
                    </body>
                    </html>""")
                    html.close()
                    options = {
                        'format': 'png',
                        'crop-h': '800',
                        'crop-w': '320',
                        'crop-x': '0',
                        'crop-y': '0',
                        'encoding': "UTF-8",
                        'custom-header': [
                            ('Accept-Encoding', 'gzip')
                        ]
                    }
                    imgkit.from_file("template/images/" + str(imageName) + "_mirrory.html", "template/images/png/" + str(imageName) + "_mirrory.jpg", options=options)

                elif filther == "doublemirror":
                    html = open("template/images/" + str(imageName) + "_doublemirror.html", "w")
                    html.write("""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                    <style>
                    table {
                width: 30%;
                border-collapse: collapse;
                }
                td {
                position: relative;
                border: 1px solid rgb(61, 61, 61);
                
                }

                td:after {
                content: '';
                display: block;
                margin-top: 100%;
                }
                td .content {
                position: absolute;
                top: 0;
                bottom: 0;
                left: 0;
                right: 0;
                }
                    </style>
                </head>
                <body>
                <table>""")
                    value4 = 0
                    contY = lenRows - 1
                    while contY >= 0:
                        html.write("<tr>")
                        contX = lenColumns - 1
                        while contX >= 0:
                            if value4 != contY:
                                html.write("</tr>")
                                value4 = contY
                            Encontrado = False
                            for color in image.celdas:
                                hexa = color.hexColor
                                booleano = color.boolean
                                celdaX = color.posX
                                celdaY = color.posY
                                if int(contX) == int(celdaX) and int(contY) == int(celdaY):
                                    #print("x: " + str(contX) + ", y: " + str(contY) + ", celdaX: " + str(celdaX) + ", celdaY: " +  str(celdaY))
                                    boo = booleano.lower() 
                                    if boo == "true":
                                        Encontrado = True
                                        #print("posX: " + str(contX) + ", posY: " + str(contY) + ", Se pinta: " + str(booleano) + ", color: " + str(hexa))
                                        #CrearCeldaPintada
                                        html.write("""<td><div style= "background-color: """ + str(hexa) + """;" class="content"></div></td>""")
                                        contX -= 1
                                    else:
                                        Encontrado = True
                                        #print("posX: " + str(contX) + ", posY: " + str(contY) + ", Se pinta: " + str(booleano) + ", color: " + str(hexa))
                                        html.write("""<td><div style= "background-color: #FFFFFF;" class="content"></div></td>""")
                                        contX -= 1
                                        #CrearCeldaVacias
                                #else:
                                    #continue
                            if Encontrado == False:
                                #print("posX: " + str(contX) + ", posY: " + str(contY) + ", No se pinta")
                                html.write("""<td><div style= "background-color: #FFFFFF;" class="content"></div></td>""")
                                contX -= 1
                        contY -= 1

                    html.write("""</table>
                    </body>
                    </html>""")
                    html.close()
                    options = {
                        'format': 'png',
                        'crop-h': '800',
                        'crop-w': '320',
                        'crop-x': '0',
                        'crop-y': '0',
                        'encoding': "UTF-8",
                        'custom-header': [
                            ('Accept-Encoding', 'gzip')
                        ]
                    }
                    imgkit.from_file("template/images/" + str(imageName) + "_doublemirror.html", "template/images/png/" + str(imageName) + "_doublemirror.jpg", options=options)

            print("\n")
            print("Reporte creado con exito")
            print("\n")
