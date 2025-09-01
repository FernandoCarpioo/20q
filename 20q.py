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
            if ask("¿Es una actividad o deporte?"):
                if ask("¿Se juega con una pelota?"):
                    if ask("¿Se juega con los pies principalmente?"):
                        leaf("fútbol")
                    else:
                        if ask("¿Se juega con una red alta en el centro?"):
                            if ask("¿Se golpea la pelota con las manos?"):
                                leaf("voleibol")
                            else:
                                leaf("tenis")
                        else:
                            if ask("¿Se juega lanzando la pelota a un aro?"):
                                leaf("baloncesto")
                            else:
                                leaf("béisbol")
                else:
                    if ask("¿Se practica en el agua?"):
                        if ask("¿Se nada en carreras?"):
                            leaf("natación")
                    else:
                        if ask("¿Se practica en el hielo?"):
                            leaf("patinaje sobre hielo")
                        else:
                            if ask("¿Se practica con movimientos de defensa y ataque físico?"):
                                if ask("¿Proviene de Corea y usa muchas patadas altas?"):
                                    leaf("taekwondo")
                                else:
                                    if ask("¿Proviene de Japón y se centra en golpes con puños y patadas rectas?"):
                                        leaf("karate")
                                    else:
                                        leaf("artes marciales")
                            else:
                                leaf("atletismo")
            else:
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

