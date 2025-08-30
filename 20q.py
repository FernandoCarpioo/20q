import unicodedata

MAX_PREGUNTAS = 20
contador_preguntas = 0

SI = {"si", "s"} 
NO  = {"no", "n"}

#Limpia la entrada del usuario
def normalize(s: str) -> str:
    s = s.strip().lower()
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    return s

#Contador de 20 preguntas, ademas de llamar a normalize
def ask(prompt: str) -> bool:
    global contador_preguntas
    if contador_preguntas >= MAX_PREGUNTAS:
        raise RuntimeError("LIMITE_20")
    contador_preguntas += 1
    while True:
        ans = input(f"({contador_preguntas}) {prompt} [sí/no]: ")
        ans = normalize(ans)
        if ans in SI: return True
        if ans in NO:  return False
        print("Responde solo 'sí' o 'no' (puedes usar s/n).")

#Nos da la palabra final cuando el arbol llega a una hoja
def leaf(*opciones):
    """Imprime una única respuesta. Falla si hay 0 o >1 opciones."""
    if len(opciones) != 1:
        raise ValueError(f"leaf() espera 1 opción, recibidas: {len(opciones)} -> {opciones}")
    print(f"\n  Estás pensando en {opciones[0]} ✅\n")
    return opciones[0]

#Mensaje cuando se llega a las 20 preguntas sin resultado claro
def fin_limite():
    print("\nGame Over")

# ============================
# Árbol de decisiones
# ============================

def juego():
    global contador_preguntas
    contador_preguntas = 0

    print("Bienvenido a 20q Remaster")
    print("Piensa en algo: puede ser un objeto, un ser vivo o un concepto abstracto.")
    print("Responde 'sí' o 'no' a las preguntas.")
    print("Máximo 20 preguntas.\n")

    try:
        # 1) Tangible vs abstracto
        if ask("¿Lo que pensaste se puede tocar físicamente?"):
            # 2) Vivo vs no vivo
            if ask("¿Es un ser vivo?"):
                # 3) Animal vs planta/hongo
                if ask("¿Es un animal?"):
                    # 4) Hábitat: acuático vs terrestre
                    if ask("¿Vive la mayor parte del tiempo en el agua?"):
                        # Mamífero marino vs pez
                        if ask("¿Es un mamífero marino?"):
                            if ask("¿Tiene hocico alargado y parece sonreír?"):
                                leaf("delfín")
                            elif ask("¿Echa agua al respirar por sus aberturas nasales en la parte superior de la cabeza?"):
                                leaf("ballena")
                            elif ask("¿Tiene bigotes anchos y sensibles que sirven como órganos sensoriales para la caza?"):
                                leaf("foca")
                            elif ask("¿Tiene cuerpo grande, aplanado y se alimenta de pastos marinos?"):
                                leaf("manatí")
                            elif ask("¿Es pequeño y parecido a un delfín pero más robusto?"):
                                leaf("marsopa")
                            elif ask("¿Tiene colmillos largos y piel gruesa?"):
                                leaf("morsa")
                            else:
                                leaf("nutria")  # Mamífero marino común que queda como opción final
                        else:
                            leaf("pez")
                    else:
                        # Terrestres: domésticos vs salvajes
                        if ask("¿Vive con personas en casas o granjas?"):
                            # Mascotas vs animales de granja
                            if ask("¿Es una mascota común de casa?"):
                                if ask("¿Es un canino doméstico?"):
                                    leaf("perro")
                                elif ask("¿Es felino doméstico?"):
                                    leaf("gato")
                                else:
                                    leaf("conejo")  # otra mascota frecuente
                            else:
                                if ask("¿Da leche para consumo humano?"):
                                    leaf("vaca")
                                elif ask("¿Es un ave de granja que pone huevos?"):
                                    leaf("gallina")
                                elif ask("¿Se utiliza para trabajo en granja, transporte o carga?"):
                                    leaf("caballo")
                                else:
                                    leaf("cerdo")  # otro animal de granja común
                        else:
                            # Animales salvajes terrestres
                            if ask("¿Se desplaza principalmente volando?"):
                                if ask("¿Es un ave grande y depredadora?"):
                                    leaf("águila")
                                elif ask("¿Es pequeño y bate las alas muy rápido?"):
                                    leaf("colibrí")
                                else:
                                    leaf("loro")  # ave tropical común
                            else:
                                if ask("¿Es un animal salvaje parecido a un perro?"):
                                    leaf("lobo")
                                elif ask("¿Es un felino grande con melena?"):
                                    leaf("león")
                                elif ask("¿Tiene trompa larga y colmillos visibles?"):
                                    leaf("elefante")
                                elif ask("¿Es un animal muy alto con cuello largo que se alimenta de hojas altas?"):
                                    leaf("jirafa")
                                elif ask("¿Tiene rayas negras y blancas?"):
                                    leaf("cebra")
                                elif ask("¿Es un felino salvaje de tamaño mediano y manchas?"):
                                    leaf("leopardo")
                                elif ask("¿Tiene pelaje grueso y come plantas y carne?"):
                                    leaf("oso")
                                else:
                                    leaf("rinoceronte")  # animal terrestre grande que queda como opción final

                else:
                    # 3) Plantas y otros
                    if ask("¿Es una planta?"):
                        if ask("¿Tiene flores visibles?"):
                            if ask("¿Tiene espinas en el tallo?"):
                                leaf("rosa")
                            else:
                                if ask("¿La flor es grande y sigue al sol?"):
                                    leaf("girasol")
                                else:
                                    leaf("tulipán")
                        else:
                            if ask("¿Es un árbol?"):
                                if ask("¿Tiene hojas como agujas y produce conos?"):
                                    leaf("pino")
                                else:
                                    if ask("¿Da fruta comestible como manzanas?"):
                                        leaf("manzano")
                                    else:
                                        leaf("roble")
                            else:
                                if ask("¿Tiene tallos con espinas y aspecto carnoso?"):
                                    leaf("cactus")
                                else:
                                    if ask("¿Tiene hojas en forma de pluma y no tiene flores?"):
                                        leaf("helecho")
                                    else:
                                        if ask("¿Cubre zonas húmedas como una alfombra verde?"):
                                            leaf("musgo")
                                        else:
                                            leaf("alga")
                    else:
                        leaf("hongo")
            else:
            # NO vivo (objeto o natural)
                                
                # COMIDA O BEBIDA
                if ask("¿Es comida o bebida?"):
                    # COMIDA

                    if ask("¿Es comida?"):

                        if ask("¿Es dulce?"):  # Postres y frutas

                            # Frutas
                            if ask("¿Es una fruta?"):

                                # Frutas que crecen en racimos
                                if ask("¿Crece en racimos (de un mismo tallo)?"):
                                    if ask("¿Mide entre 1 y 3 cm?"):
                                        if ask("¿Su cáscara es delgada y puede ser verde, morada o negra?"):
                                            leaf("uva")
                                        else:
                                            leaf("cereza")

                                # Frutas que crecen en árbol
                                elif ask("¿Crece en un árbol?"):
                                    if ask("¿Es cítrica y se parte en gajos?"):
                                        if ask("¿Se pela fácilmente con las manos?"):
                                            leaf("mandarina")
                                        else:
                                            leaf("naranja")
                                    else:
                                        if ask("¿Es redonda y jugosa?"):
                                            leaf("manzana")
                                        else:
                                            leaf("pera")

                                # Otras frutas
                                else:
                                    if ask("¿Es roja y tiene semillas por fuera?"):
                                        leaf("fresa")
                                    elif ask("¿Se pela y es de color amarillo?"):
                                        if ask("¿Es alargada y curva?"):
                                            leaf("plátano")
                                        else:
                                            leaf("piña")
                                    elif ask("¿Es tropical y jugosa?"):
                                        if ask("¿Tiene un hueso grande en el centro?"):
                                            if ask("¿Es amarilla por dentro?"):
                                                leaf("mango")
                                            else:
                                                leaf("durazno")
                                        else:
                                            if ask("¿Es verde por fuera y roja por dentro con semillas negras?"):
                                                leaf("sandía")
                                            else:
                                                leaf("papaya")

                            # Postres (no frutas)
                            else:
                                if ask("¿Es frío y cremoso?"):
                                    leaf("helado")
                                elif ask("¿Es dulce horneado?"):
                                    leaf("pastel")
                                elif ask("¿Es pequeño y dulce?"):
                                    leaf("galletas")
                                else:
                                    leaf("gelatina")

                        # Comida salada
                        else:

                            # Comida rápida
                            if ask("¿Es comida rápida?"):
                                if ask("¿Es redonda con queso y toppings?"):
                                    leaf("pizza")
                                elif ask("¿Es carne dentro de pan redondo?"):
                                    leaf("hamburguesa")
                                elif ask("¿Es mexicano y enrollado o doblado con una tortilla?"):
                                    leaf("taco")
                                elif ask("¿Se come con palillos?"):
                                    if ask("¿Es fideos en sopa?"):
                                        leaf("ramen")
                                    else:
                                        leaf("sushi")
                                elif ask("¿Es un pan largo con salchicha dentro?"):
                                    leaf("hot dog")
                                else:
                                    leaf("sandwich")

                            # Platillos
                            elif ask("¿Es un platillo líquido que se come con cuchara?"):
                                leaf("sopa")
                            elif ask("¿Es un platillo hecho principalmente de vegetales?"):
                                if ask("¿Se come crudo y puede llevar aderezo?"):
                                    leaf("ensalada")

                            # Snacks (salados)
                            elif ask("¿Es un snack o botana?"):
                                if ask("¿Es salado y crujiente?"):
                                    leaf("papas fritas")

                    else:  # bebida

                        if ask("¿Es dulce?"):

                            if ask("¿Es caliente?"):
                                if ask("¿Contiene café?"):
                                    leaf("café")
                                else:
                                    leaf("chocolate caliente")
                            else:
                                if ask("¿Es con gas?"):
                                    leaf("refresco")
                                else:
                                    leaf("jugo")

                        else:  # no dulce

                                if ask("¿Es caliente?"):
                                    if ask("¿Contiene café?"):
                                        leaf("café")
                                    else:
                                        leaf("té")
                                else:
                                    if ask("¿Es con gas?"):
                                        if ask("Es una bebida alcoholica"):
                                            leaf("cerveza")
                                        else:
                                            leaf("refresco")
                                    else:
                                        leaf("agua")


                else:
                    
                    if ask("¿Está hecho por humanos?"):
                        # OBJETOS
                        if ask("¿Funciona con electricidad?"):
                            if ask("¿Se usa para comunicarse o informarse?"):
                                if ask("¿Cabe en el bolsillo y tiene pantalla táctil?"):
                                    leaf("smartphone")
                                else:
                                    if ask("¿Tiene teclado y una pantalla?"):
                                        leaf("Computadora")
                                    else:
                                        if ask("¿Tiene solamente pantalla?"):
                                            leaf("Televisor")
                                        else:
                                            leaf("Radio")
                            else:
                                #6
                                if ask("¿Tiene bocinas?"):
                                    if ask("¿Esta relacionado con la industria de videojuegos?"):
                                        leaf("Consola de videojuegos")
                                    else:
                                        if ask("¿Lo pones en tus o sobre tus oidos para escuchar la musica?"):
                                            leaf("Audifonos")
                                        else:
                                            leaf("Estereo")

                                else:
                                    if ask("¿Sirve para guardar comida fría?"):
                                        leaf("refrigerador")
                                    else:
                                        if ask("¿Sirve para calentar comida rápido?"):
                                            leaf("microondas")
                                        else:
                                            if ask("¿Sirve para iluminar un cuarto?"):
                                                leaf("foco")
                                            else:
                                                leaf("lavadora")
                        else:
                            if ask("¿Se usa para comer o beber?"):
                                if ask("¿Sirve para tomar líquidos?"):
                                    if ask("¿Tiene cuello y tapa?"):
                                        leaf("botella")
                                    else:
                                        leaf("vaso")
                                else:
                                    if ask("¿Es cóncavo y sirve para sopa?"):
                                        leaf("cuchara")
                                    else:
                                        if ask("¿Tiene púas para pinchar comida?"):
                                            leaf("tenedor")
                                        else:
                                            leaf("cuchillo")
                            else:
                                if ask("¿Es un mueble?"):
                                    if ask("¿Sirve para sentarse?"):
                                        leaf("silla")
                                    else:
                                        if ask("¿Sirve para poner cosas encima para comer o trabajar?"):
                                            leaf("mesa")
                                        else:
                                            if ask("¿Sirve para dormir?"):
                                                leaf("cama")
                                            else:
                                                leaf("escritorio")
                                else:
                                    if ask("¿Es una herramienta manual?"):
                                        if ask("¿Sirve para golpear clavos?"):
                                            leaf("martillo")
                                        else:
                                            if ask("¿Sirve para atornillar o desatornillar?"):
                                                leaf("destornillador")
                                            else:
                                                if ask("¿Corta al cerrar dos hojas?"):
                                                    leaf("tijeras")
                                                else:
                                                    leaf("llave inglesa")
                                    else:
                                        #Tipos de transporte
                                            if ask("¿Es un medio de transporte?"):
                                                if ask("¿Se mueve con la fuerza humana, sin motor?"):
                                                    if ask("¿Tiene dos ruedas?"):
                                                        leaf("bicicleta")
                                                    else:
                                                        if ask("¿Tiene una tabla con ruedas?"):
                                                            leaf("patineta")
                                                        else:
                                                            leaf("canoa")
                                                else:
                                                    if ask("¿Vuela por el aire?"):
                                                        if ask("¿Es más pequeño que un avión y puede tener hélices?"):
                                                            leaf("helicóptero")
                                                        else:
                                                            if ask("¿Es un vehículo aéreo no tripulado controlado a distancia?"):
                                                                leaf("dron")
                                                            else:
                                                                leaf("avión")
                                                    else:
                                                        if ask("¿Va por rieles?"):
                                                            if ask("¿Transporta muchas personas en la ciudad?"):
                                                                leaf("metro")
                                                            else:
                                                                leaf("tren")
                                                        else:
                                                            if ask("¿Navega en el agua?"):
                                                                if ask("¿Es pequeño y se mueve con motor o remos?"):
                                                                    leaf("lancha")
                                                                else:
                                                                    if ask("¿Es muy grande y transporta personas o mercancía?"):
                                                                        leaf("barco")
                                                                    else:
                                                                        leaf("submarino")
                                                            else:
                                                                if ask("¿Es un vehículo de dos ruedas con motor?"):
                                                                    leaf("motocicleta")
                                                                else:
                                                                    if ask("¿Es un vehículo personal de 4 llantas para carretera?"):
                                                                        leaf("coche")
                                                                    else:
                                                                        if ask("¿Es muy grande y transporta muchas personas o carga pesada?"):
                                                                            leaf("camión")
                                                                        else:
                                                                            leaf("autobús")

                                            else:
                                                if ask("¿Es un juguete que rebota?"):
                                                    leaf("pelota")
                                                else:
                                                    if ask("¿Tiene páginas con texto para leer?"):
                                                        leaf("libro")
                                                    else:
                                                        leaf("cuaderno")
                    else:
                        # NATURAL no fabricado
                        if ask("¿Es una sustancia básica de la naturaleza?"):
                            if ask("¿Es un líquido transparente que bebemos?"):
                                leaf("agua")
                            else:
                                if ask("¿Es el gas que respiramos?"):
                                    leaf("aire")
                                else:
                                    if ask("¿Es la tierra del suelo?"):
                                        leaf("tierra")
                                    else:
                                        if ask("¿Es fuego?"):
                                            leaf("fuego")
                                        else:
                                            if ask("¿Son granos sueltos finos de roca?"):
                                                leaf("arena")
                                            else:
                                                leaf("roca")
                        else:
                            if ask("¿Está en el espacio?"):
                                if ask("¿Brilla por sí mismo como una estrella?"):
                                    if ask("¿Es la estrella de nuestro sistema?"):
                                        leaf("sol")
                                    else:
                                        if ask("¿Es un destello breve en el cielo por un meteoro?"):
                                            leaf("estrella fugaz")
                                        else:
                                            leaf("estrella")
                                else:
                                    if ask("¿Gira alrededor de una estrella y no brilla por sí mismo?"):
                                        if ask("¿Es el planeta donde vivimos?"):
                                            leaf("Tierra")
                                        else:
                                            if ask("¿Es el planeta rojo?"):
                                                leaf("Marte")
                                            else:
                                                leaf("planeta")
                                    else:
                                        if ask("¿Gira alrededor de un planeta?"):
                                            leaf("satélite")
                                        else:
                                            if ask("¿Tiene cola cuando se acerca al Sol?"):
                                                leaf("cometa")
                                            else:
                                                if ask("¿Es un conjunto enorme de estrellas?"):
                                                    if ask("¿Incluye todo lo que existe?"):
                                                        leaf("universo")
                                                    else:
                                                        leaf("galaxia")
                                                else:
                                                    leaf("luna")
                            else:
                                if ask("¿Es un lugar o forma del terreno o del agua en la Tierra?"):
                                    if ask("¿Es una elevación muy alta del terreno?"):
                                        leaf("montaña")
                                    else:
                                        if ask("¿Es agua que corre por un cauce?"):
                                            leaf("río")
                                        else:
                                            if ask("¿Es una gran masa de agua salada?"):
                                                leaf("mar")
                                            else:
                                                if ask("¿Es agua rodeada de tierra por todos lados?"):
                                                    leaf("lago")
                                                else:
                                                    if ask("¿Es una zona muy seca con poca vegetación?"):
                                                        leaf("desierto")
                                                    else:
                                                        if ask("¿Es una zona con muchos árboles?"):
                                                            leaf("bosque")
                                                        else:
                                                            leaf("volcán")
                                else:
                                    if ask("¿Es algo del clima o del cielo?"):
                                        if ask("¿Es una nube en el cielo?"):
                                            leaf("nube")
                                        else:
                                            if ask("¿Es agua que cae de las nubes?"):
                                                leaf("lluvia")
                                            else:
                                                if ask("¿Es un rayo de electricidad en una tormenta?"):
                                                    leaf("relámpago")
                                                else:
                                                    leaf("viento")
        else:
            # ABSTRACTO (no tangible)
            if ask("¿Es un sentimiento?"):
                if ask("¿Es un sentimiento positivo?"):
                    if ask("¿Es cariño profundo hacia alguien?"):
                        leaf("amor")
                    else:
                        leaf("alegría")
                else:
                    if ask("¿Es tristeza por una pérdida?"):
                        leaf("tristeza")
                    else:
                        leaf("miedo")
            else:
                if ask("¿Es una idea o concepto que se usa para estudiar o pensar?"):
                    if ask("¿Sirve para contar o medir?"):
                        leaf("número")
                    else:
                        if ask("¿Es la capacidad para hacer algo o producir cambios?"):
                            leaf("energía")
                        else:
                            leaf("conocimiento")
                else:
                    if ask("¿Tiene que ver con el tiempo?"):
                        if ask("¿Ya pasó?"):
                            leaf("pasado")
                        else:
                            if ask("¿Es lo que está ocurriendo ahora?"):
                                leaf("presente")
                            else:
                                leaf("futuro")
                    else:
                        # Filosóficos / generales
                        if ask("¿Es la existencia de los seres vivos?"):
                            leaf("vida")
                        else:
                            if ask("¿Es cuando un ser vivo deja de vivir?"):
                                leaf("muerte")
                            else:
                                if ask("¿Es la ausencia total de cosas?"):
                                    leaf("nada")
                                else:
                                    if ask("¿Es un espacio sin materia dentro de algo?"):
                                        leaf("vacío")
                                    else:
                                        if ask("¿Es algo que no tiene límite?"):
                                            leaf("infinito")
                                        else:
                                            if ask("¿Es poder actuar sin estar obligado?"):
                                                leaf("libertad")
                                            else:
                                                if ask("¿Es dar a cada quien lo que le corresponde?"):
                                                    leaf("justicia")
                                                else:
                                                    leaf("idea")

    except RuntimeError as e:
        if str(e) == "LIMITE_20":
            fin_limite()
        else:
            raise



# ============================
# Main
# ============================

if __name__ == "__main__":
    juego()

