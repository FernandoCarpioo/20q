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
                    if ask("¿Pasa la mayor parte del tiempo en el agua?"):
                        # Mamíferos marinos vs peces
                        if ask("¿Es un mamífero que respira aire por pulmones?"):
                            if ask("¿Tiene hocico alargado y sparece sonreir?"):
                                leaf("delfín")
                            elif ask("¿Echa agua al respirar por su espiráculo en la cabeza?"):
                                leaf("ballena")
                            elif ask("¿Tiene bigotes sensibles para cazar presas?"):
                                leaf("foca")
                            elif ask("¿Come pastos marinos y tiene cuerpo grande y aplanado?"):
                                leaf("manatí")
                            elif ask("¿Tiene colmillos largos y piel gruesa?"):
                                leaf("morsa")
                            else:
                                leaf("nutria")  
                        else:
                            if ask("¿Es un pez depredador, con dientes afilados y fuerte?"):
                                leaf("tiburón")
                            else:
                                leaf("piraña")
                    else:
    
                        if ask("¿Vive dentro de casas o granjas con personas?"):
                            # Mascotas vs animales de granja
                            if ask("¿Es una mascota común de casa?"):
                                if ask("¿ladra?"):
                                    leaf("perro")
                                elif ask("¿Es un felino?"):
                                    leaf("gato")
                                elif ask("¿Es pequeño y se mantiene en jaula o acuario?"):
                                    if ask("¿Tiene 4 patas y pelo?"):
                                        leaf("hámster")
                                    elif ask("¿Nada y tiene escamas?"):
                                        leaf("pez")
                                    else:
                                        leaf("tortuga")
                                elif ask("¿Vuela y canta en jaula?"):
                                    leaf("periquito")
                                else:
                                    leaf("conejo")
                            else:
                                # Animales de granja
                                if ask("¿Produce leche para el consumo humano?"):
                                    leaf("vaca")
                                elif ask("¿Es un ave que pone huevos?"):
                                    if ask("¿Nace de un huevo, no vuela ni nada?"):
                                        leaf("gallina")
                                    else:
                                        leaf("pato")
                                elif ask("¿Se usa para transporte o carga y tiene pezuñas?"):
                                    if ask("¿Es grande y fuerte?"):
                                        leaf("caballo")
                                    else:
                                        leaf("burro")
                                else:
                                    leaf("cerdo")
                        else:
                            # Animales salvajes terrestres
                            if ask("¿Puede volar?"):
                                if ask("¿Es un ave grande y depredadora?"):
                                    leaf("águila")
                                elif ask("¿Es muy pequeño y bate las alas muy rápido?"):
                                    leaf("colibrí")
                                elif ask("¿Es tropical y colorido?"):
                                    leaf("loro")
                                else:
                                    leaf("pingüino")
                            else:
                                if ask("¿Se parece a un perro domestico?"):
                                    leaf("lobo")
                                elif ask("¿Es un felino grande con melena?"):
                                    leaf("león")
                                elif ask("¿Es un felino grande, ágil y de pelaje rayado o manchado?"):
                                    leaf("tigre/pantera")
                                elif ask("¿Tiene trompa larga y colmillos visibles?"):
                                    leaf("elefante")
                                elif ask("¿Es muy alto, con cuello largo y come hojas de árboles altos?"):
                                    leaf("jirafa")
                                elif ask("¿Tiene rayas blancas y negras?"):
                                    leaf("cebra")
                                elif ask("¿Tiene pelaje grueso y come plantas y carne?"):
                                    leaf("oso")
                                elif ask("¿Salta y vive en Australia?"):
                                    leaf("canguro")
                                elif ask("¿Es un marsupial que vive en árboles y come hojas de eucalipto?"):
                                    leaf("koala")
                                else:
                                    leaf("rinoceronte")
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
                        if ask("¿Produce su propio alimento?"):
                            leaf("Hongo")
                        else:
                            if ask("¿Es alguna profesion o rol?"):
                                if ask("Esta relacionada con el area de la salud"):
                                    leaf("Doctor(a)/Enfermer@")
                                else:
                                    if ask("¿Esta relacionado con el ambito escolar?"):
                                        if ask("¿Esa profesion se encarga de estar al frente de una escuela?"):
                                            leaf("Director(a)")
                                        else:
                                            if ask("¿Esta profesion su funcion principal es impartir clases? "):
                                                leaf('Maestr@/Profesor(a)')
                                    else:
                                        if ask("¿Esta profesion cuentan con armas de fuego?"):
                                            if ask("¿Estan especializados en defender la seguridad nacional?"):
                                                leaf("Militares")
                                            else:
                                                if ask("¿Se centran en mantener el orden publico y seguridad del ciudadano?"):
                                                    leaf("Policias")
                                        else:
                                            if ask("¿Esta profesion apaga incendios?"):
                                                leaf("Bombero")
                                            else:
                                                if ask("¿Se dedica relacionado con la musica?"):
                                                    if ask("¿Su funcion principal es cantar?"):
                                                        leaf("Cantante")
                                                    else:
                                                        leaf("Musico")
                                                else:
                                                    if ask("¿Esta relacionado con algun deporte?"):
                                                        if ask("¿En ese deporte puede desempeñar el rol de portero, defensa, medio o delantero?"):
                                                            leaf("futbolista")
                                                        else:
                                                            if ask("¿Esta relacionado con la NBA?"):
                                                                leaf("Basquetbolista")
                                                            else:
                                                                if ask("¿Puede tomar el rol de coreback?"):
                                                                    leaf("Jugador de futbol americano")
                                                                else:
                                                                    if ask("¿Su funcion es desempeñar que el juego se lleve con forme a las reglas_"):
                                                                        leaf("Arbitro")
                                                    else:
                                                        if ask("¿Tiene que ver con alguno de las tres ramas de poder del estado en Mexico?"):
                                                            if ask("¿Se encarga de crear y aprobar leyes?"):
                                                                if ask("¿Se encarga de representar entidades federativas?"):
                                                                    leaf("Diputados")
                                                                else:
                                                                    if ask("¿Se encarga de representar al pueblo directamente?"):
                                                                        leaf("Senadores")
                                                            else:
                                                                if ask("¿Se encarga de ejecutar las leyes? "):
                                                                    leaf("Presidente")

            else:
            # NO vivo (objeto o natural)
                if ask("¿Es una parte del cuerpo humano o animal?"):
                    if ask("¿Está en la cabeza?"):
                        if ask("¿Se usa para ver?"):
                            leaf("ojo")
                        elif ask("¿Se usa para escuchar?"):
                            leaf("oreja")
                        elif ask("¿Se usa para oler?"):
                            leaf("nariz")
                        elif ask("¿Se usa para comer o hablar?"):
                            leaf("boca")
                        else:
                            leaf("cabeza")  
                    elif ask("¿Se usa principalmente para mover, levantar o manipular objetos con los brazos?"):
                        if ask("¿Se usa para sostener o manipular cosas con precisión?"):
                            leaf("mano")
                        elif ask("¿Se usa para levantar, empujar, tirar o mover objetos más grandes?"):
                              leaf("brazo")
                        else:
                            leaf("hombro")  # permite movimiento del brazo

                        if ask("¿Se usa para agarrar cosas?"):
                            leaf("mano")
                        elif ask("¿Conecta el brazo al tronco y permite movimiento?”"):
                            leaf("hombro")
                        else:
                            leaf("brazo")
                    elif ask("¿Está en las piernas o pies?"):
                        if ask("¿Se usa para caminar o correr?"):
                            leaf("pierna")
                        elif ask("¿Se usa para apoyar el cuerpo y equilibrarse?"):
                            leaf("pie")
                        else:
                            leaf("rodilla")
                    else:
                        leaf("tronco")


                else:
                    
                    if ask("¿Está hecho por humanos?"):
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
                            if ask("¿Se usa para el cuidado o higiene personal?"):
                                # Cabello
                                if ask("¿Está relacionado con el cabello?"):
                                    if ask("¿Sirve para lavarlo?"):
                                        if ask("¿Es líquido dentro de un envase?"):
                                            leaf("shampoo")
                                        else:
                                            leaf("acondicionador")
                                    else:
                                        if ask("¿Sirve para desenredar o acomodar el cabello?"):
                                            leaf("peine")
                                        else:
                                            leaf("cepillo para cabello")
                                elif ask("¿Sirve para limpiar el cuerpo?"):
                                    if ask("¿Es sólido y se frota directamente?"):
                                        leaf("jabón en barra")
                                elif ask("¿Está relacionado con los dientes?"):
                                    if ask("¿Sirve para cepillarlos?"):
                                        if ask("¿Tiene cerdas?"):
                                            leaf("cepillo de dientes")
                                    else:
                                        if ask("¿Es una pasta?"):
                                            leaf("pasta dental")
                                        else:
                                            leaf("enjuague bucal")
                                else:
                                    if ask("¿Sirve para después de bañarse o asearse?"):
                                        if ask("¿Absorbe agua del cuerpo?"):
                                            leaf("toalla")
                                        else:
                                            if ask("¿Sirve para evitar el mal olor corporal?"):
                                                leaf("desodorante")
                                            else:
                                                leaf("loción/perfume")
                                    else:
                                        if ask("¿Es para las manos y uñas?"):
                                            if ask("¿Corta las uñas?"):
                                                leaf("cortaúñas")
                                            else:
                                                if ask("¿Sirve para limar las uñas?"):
                                                    leaf("lima de uñas")
                                                else:
                                                    leaf("esmalte de uñas")
                                        else:
                                            if ask("¿Sirve para rasurarse o depilarse?"):
                                                if ask("¿Es desechable con cuchillas?"):
                                                    leaf("rastrillo/afeitadora manual")
                                                else:
                                                    leaf("crema depilatoria")
                                            else:
                                                if ask("¿Es una prenda de ropa interior?"):
                                                    leaf("Calzones")
                                                else:
                                                    leaf("algodón o hisopos")
                                
                            else:
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
                                                    if ask("¿Tiene una antena fisica o necesita de una para funcionar?"):
                                                        leaf("Radio")
                                                    else:
                                                        if ask("¿Es una red global que conecta computadoras, servidores y dispositivos en todo el mundo?"):
                                                            leaf("Internet")
                                                        else:
                                                            if ask("¿Forma parte del universo XBOX, Nintendo, Playstation?"):
                                                                leaf("Videojuegos")
                                                            else:
                                                                if ask("¿Permite crear perfiles, compartir fotos, videos, mensajes y mantener comunicación con otros usuarios?"):
                                                                    leaf("Redes Sociales")
                                                                else:
                                                                    if ask("¿Es una tecnologia de conexion inalambrica para conectar dispositivos?"):
                                                                        leaf("WI-FI")
                                                                    else:
                                                                        if ask("¿Es un dispositivo mecatronico?"):
                                                                            leaf("Robot")

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
                                                        if ask("¿Es un juguete?"):
                                                            if ask("¿Es redondo?"):
                                                                leaf("Balon/Pelota")
                                                                #Faltan cosas que agregar sobre juguetes
                                                        else:
                                                            if ask("¿Esta hecho para el aprendizaje?"):
                                                                if ask("¿Tiene paginas con texto para leer?"):
                                                                    leaf("Libro")
                                                                else:
                                                                    if ask("¿Esta hecho para escribir en el?"):
                                                                        leaf("Cuaderno")
                                                                    else:
                                                                        if ask("¿Se usa para escribir o dibujar cosas?"):
                                                                            if ask("¿Escribe con tinta?"):
                                                                                leaf("Pluma")
                                                                        else:
                                                                            if ask ("¿Escribe con grafito?"):
                                                                                leaf ("Lapiz")
                                                                            else:
                                                                                if ask("¿Se usa para colorear?"):
                                                                                    leaf("Lapices de colores")
                                                                                else:
                                                                                    if ask("¿Contiene una navaja en su interior?"):
                                                                                        leaf("Sacapuntas")
                                                                                    else:
                                                                                        if ask("¿Tu objeto se usa para corregir errores?"):
                                                                                            if ask ("¿Esta hecho de goma?"):
                                                                                                leaf("Goma para borrar")
                                                                                            else:
                                                                                                leaf("Corrector")
                                                                                        else:
                                                                                            if ask("¿El objetivo de tu objeto es  medir?"):
                                                                                                if ask("¿Tu objeto tiene forma de rectangulo?"):
                                                                                                    leaf("Regla")
                                                                                                else:
                                                                                                    if ask("¿Tiene forma de triangulo?"):
                                                                                                        leaf("Escuadras")
                                                                                                    else:
                                                                                                        leaf("Transportador")

                                                            else:
                                                                if ask("¿Fue hecho para tapar alguna parte del cuerpo?"):
                                                                    if ask("¿Es un objeto que va arriba de la cintura?"):
                                                                        if ask("¿Tiene una hebilla?"):
                                                                            leaf("Cinturon")
                                                                        else:
                                                                            if ask("¿Tu objeto va en la cabeza?"):
                                                                                if ask("¿Se usa para taparte del sol?"):
                                                                                    leaf("Gorra")
                                                                                else:
                                                                                    if ask("¿Es una prenda de ropa interior?"):
                                                                                        leaf("Brasier, Corpiño")
                                                                                    else:
                                                                                        leaf("Playera, Camisa, Saco, Blusa, Sueter")
                                                                    else:
                                                                        if ask("¿Sirve para cubrir tus pies?"):
                                                                            if ask("¿Va directamente sobre la piel del pie?"):
                                                                                leaf("Calcetin, Tin, Calcetas")
                                                                            else:
                                                                                leaf("Zapatos, Tenis, Botas, Zapatillas, Tacones")
                                                                        else:
                                                                            if ask("¿Cubre toda la pierna hasta el tobillo?"):
                                                                                leaf("Pantalones, Licras")
                                                                            else:
                                                                                leaf("Short, Falda")

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
                            if ask("¿Está en el espacio exterior?"):
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
                                                            if ask("¿Esta caracterizado por contar con edificios?"):
                                                                leaf("ciudad")
                                                            else:
                                                                if ask("¿A este en especifico van a estudiar?"):
                                                                    leaf ("Escuela")
                                                                else:
                                                                    if ask("¿Es donde se atienden a heridos o enfermos?"):
                                                                        leaf("Hospital")
                                                                        if ask("¿En este lugar se proyectan peliculas?"):
                                                                            leaf("Cine/Cinema")
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

            # 1) SENTIMIENTOS
            if ask("¿Es un sentimiento o emoción?"):
                if ask("¿Es positivo?"):
                    if ask("¿Es cariño profundo hacia alguien?"):
                        leaf("amor")
                    elif ask("¿Es bienestar o satisfacción general?"):
                        leaf("felicidad")
                    elif ask("¿Es una emoción repentina de alegría intensa?"):
                        leaf("entusiasmo")
                    elif ask("¿Es orgullo por un logro personal o ajeno?"):
                        leaf("orgullo")
                    else:
                        leaf("alegría")
                else:
                    if ask("¿Es tristeza por una pérdida o ausencia?"):
                        leaf("tristeza")
                    elif ask("¿Es enojo o ira ante algo que molesta?"):
                        leaf("enojo")
                    elif ask("¿Es asombro o impresión inesperada?"):
                        leaf("sorpresa")
                    elif ask("¿Es incomodidad por ser observado o expuesto?"):
                        leaf("vergüenza")
                    elif ask("¿Es culpa por algo que hiciste o dejaste de hacer?"):
                        leaf("culpa")
                    elif ask("¿Es repulsión hacia algo desagradable?"):
                        leaf("asco")
                    elif ask("¿Es ansiedad o preocupación por lo que pueda pasar?"):
                        leaf("ansiedad")
                    else:
                        leaf("miedo")

            # 2) EVENTOS Y CELEBRACIONES
            elif ask("¿Es el nombre que se le da a un evento o celebración?"):
                if ask("¿Es el día en que se conmemora tu nacimiento?"):
                    leaf("cumpleaños")
                elif ask("¿Es una celebración cristiana del 25 de diciembre?"):
                    leaf("navidad")
                elif ask("¿Es una ceremonia donde dos personas se casan?"):
                    leaf("boda")
                else:
                    leaf("fiesta o día festivo")


            # 3) ACTIVIDAD O DEPORTE
            elif ask("¿Es una actividad o deporte?"):
                if ask("¿Se juega con una pelota?"):
                    if ask("¿Se juega principalmente con los pies?"):
                        leaf("fútbol")
                    elif ask("¿Se juega con una red alta en el centro?"):
                        if ask("¿Se golpea la pelota con las manos?"):
                            leaf("voleibol")
                        else:
                            leaf("tenis")
                    elif ask("¿Se lanza la pelota a un aro?"):
                        leaf("baloncesto")
                    else:
                        leaf("béisbol")
                elif ask("¿Se practica en el agua?"):
                    if ask("¿Implica nadar en carreras?"):
                        leaf("natación")
                    else:
                        leaf("deporte acuático")
                elif ask("¿Se practica en el hielo?"):
                    leaf("patinaje sobre hielo")
                elif ask("¿Implica golpes o patadas?"):
                    if ask("¿Se pelea usando principalmente los puños?"):
                        leaf("boxeo")
                    elif ask("¿Es de Corea y usa patadas altas?"):
                        leaf("taekwondo")
                    elif ask("¿Es de Japón y usa golpes rectos?"):
                        leaf("karate")
                    else:
                        leaf("artes marciales")
                else:
                    leaf("atletismo")


            # 4) Disciplinas académicas (materias escolares)
            elif ask("¿Se imparte como materia académica?"):

                # Ciencias formales
                if ask("¿Pertenece a las ciencias formales de números o lógica?"):
                    leaf("matemáticas")

                # Ciencias naturales
                elif ask("¿Pertenece a las ciencias naturales?"):
                    if ask("¿Se centra en la materia y la energía?"):
                        leaf("física")
                    elif ask("¿Se centra en sustancias y transformaciones?"):
                        leaf("química")
                    elif ask("¿Se centra en los seres vivos?"):
                        leaf("biología")
                    else:
                        leaf("ciencias naturales")

                # Ciencias sociales y humanidades
                elif ask("¿Pertenece a las ciencias sociales o humanidades?"):
                    if ask("¿Se centra en hechos del pasado humano?"):
                        leaf("historia")
                    elif ask("¿Se centra en la Tierra y sus características?"):
                        leaf("geografía")
                    elif ask("Es el amor por la sabiduría"):
                        leaf("filosofía")
                    else:
                        leaf("ciencias sociales")

                # Artes
                elif ask("¿Pertenece a las artes o la expresión estética?"):
                    if ask("¿Se expresa con imágenes, pintura o escultura?"):
                        leaf("arte")
                    else:
                        leaf("música")

                # Ciencias de la computación y tecnología
                elif ask("¿Pertenece a las ciencias de la computación o tecnología?"):
                    if ask("¿Se centra en la inteligencia artificial?"):
                        leaf("inteligencia artificial")
                    elif ask("¿Se centra en el aprendizaje automático de datos?"):
                        leaf("machine learning")
                    else:
                        leaf("informática")

                else:
                    leaf("materia académica")


            # 6) TIEMPO (unidades)
            elif ask("¿Es una unidad de tiempo?"):
                # Subdía
                if ask("¿Es menor que un día?"):
                    if ask("¿Es la unidad base del tiempo en el SI?"):
                        leaf("segundo")
                    elif ask("¿Equivale a 60 segundos?"):
                        leaf("minuto")
                    elif ask("¿Equivale a 60 minutos?"):
                        leaf("hora")
                    else:
                        leaf("milisegundo")
                # Día y múltiplos
                elif ask("¿Es exactamente 24 horas?"):
                    leaf("día")
                elif ask("¿Es aproximadamente 7 días?"):
                    leaf("semana")
                elif ask("¿Es aproximadamente 15 días?"):
                    leaf("quincena")
                elif ask("¿Es aproximadamente 30 días?"):
                    leaf("mes")
                elif ask("¿Es aproximadamente 365 días?"):
                    leaf("año")
                elif ask("¿Dura diez años?"):
                    leaf("década")
                elif ask("¿Dura cien años?"):
                    leaf("siglo")
                elif ask("¿Dura mil años?"):
                    leaf("milenio")
                else:
                    leaf("vida")


            # 7) FILOSÓFICOS / GENERALES
            else:
                # 7.1 Existencia y universo
                if ask("¿Tiene que ver con la existencia o el universo?"):
                    if ask("¿Se refiere a la existencia de los seres vivos?"):
                        leaf("vida")
                    elif ask("¿Se refiere al fin de la vida?"):
                        leaf("muerte")
                    elif ask("¿Es ausencia total de cosas?"):
                        leaf("nada")
                    elif ask("¿Es un espacio sin materia dentro de algo?"):
                        leaf("vacío")
                    elif ask("¿No tiene límite?"):
                        leaf("infinito")
                    elif ask("¿Se trata del mundo externo, independiente de la mente del observador?"):
                        leaf("realidad")
                    elif ask("¿Es la experiencia de estar consciente de ti y del entorno?"):
                        leaf("conciencia")
                    elif ask("¿Es la idea de que nuestro futuro ya esta escrito?"):
                        leaf("destino")
                    else:
                        leaf("existencia")

                # 7.2 Valores y ética
                elif ask("¿Tiene que ver con valores o ética?"):
                    if ask("¿Es poder actuar sin obligación?"):
                        leaf("libertad")
                    elif ask("¿Es dar a cada quien lo que le corresponde?"):
                        leaf("justicia")
                    else:
                        leaf("ética")

                # 7.3 Espiritualidad y creencias
                elif ask("¿Tiene que ver con espiritualidad o creencias?"):
                    leaf("religión")

                # 7.4 Sociedad, gobierno, cultura y trabajo
                elif ask("¿Tiene que ver con la sociedad o el gobierno?"):
                    if ask("¿Se refiere a organización y decisiones públicas?"):
                        leaf("política")
                    elif ask("¿Se refiere a normas jurídicas obligatorias?"):
                        leaf("ley")
                    elif ask("¿Se refiere a costumbres, tradiciones y expresiones de un pueblo?"):
                        leaf("cultura")
                    elif ask("¿Se relaciona con ganarse la vida u ocupación?"):
                        leaf("trabajo")
                    else:
                        leaf("sociedad")

                # 7.5 Bienestar personal/colectivo
                elif ask("¿Tiene que ver con bienestar o armonía?"):
                    if ask("¿Es un estado de armonía y ausencia de conflicto?"):
                        leaf("paz")
                    elif ask("¿Se refiere al bienestar físico o mental?"):
                        leaf("salud")
                    else:
                        leaf("bienestar")

                # 7.6 Relaciones personales
                elif ask("¿Tiene que ver con relaciones personales cercanas?"):
                    if ask("Describe vínculos de amistad?"):
                        leaf("amistad")
                    else:
                        leaf("familia")

                # 7.7 Conflicto y cambio
                elif ask("¿Tiene que ver con conflicto o cambios sociales fuertes?"):
                    if ask("¿Es uso intencional de la fuerza para dañar o someter?"):
                        leaf("violencia")
                    elif ask("¿Es un cambio político o social abrupto?"):
                        leaf("revolución")
                    elif ask("¿Es conflicto armado entre grupos o países?"):
                        leaf("guerra")
                    else:
                        leaf("conflicto")

                # 7.8
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

