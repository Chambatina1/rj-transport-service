"""Long-form content for service-area pages and blog posts (EN + ES)."""

# ---------------------------------------------------------------------------
# Service areas
# ---------------------------------------------------------------------------
AREAS = [
    {
        "key": "orlando",
        "slug": {"en": "orlando-fl", "es": "orlando-fl"},
        "name": {"en": "Orlando & Central Florida", "es": "Orlando y Florida Central"},
        "short": {"en": "Orlando", "es": "Orlando"},
        "card": {"en": "Home base. Fastest heavy towing response and daily freight runs across Orange, Osceola, Seminole and Lake counties.",
                 "es": "Nuestra base. La respuesta de grúa pesada más rápida y carga diaria en los condados Orange, Osceola, Seminole y Lake."},
        "schema_areas": ["Orlando, FL", "Orange County, FL", "Osceola County, FL", "Seminole County, FL", "Lake County, FL"],
        "content": {
            "en": {
                "title": "Heavy Towing & Freight Trucking in Orlando, FL | 24/7 | R&J Transport",
                "desc": "Orlando heavy towing 24/7 and local freight trucking from our yard at 4980 Patch Rd since 2004. Semis, buses, equipment. Call (407) 595-9726.",
                "kicker": "Orlando, FL · Home base since 2004",
                "h1": 'Heavy Towing &amp; Trucking in <span class="red-text">Orlando</span>',
                "lede": "Our yard is in southeast Orlando at 4980 Patch Rd. This is where our trucks and wreckers start every day — and where we respond fastest.",
                "tow_h": "24/7 heavy towing in Orlando",
                "tow_p": ["From I-4 through downtown to the Beachline (SR 528), SR 417 and the Florida Turnpike, we tow semis, tractor-trailers, box trucks, buses and heavy equipment around the clock.",
                          "Being based near Orlando International Airport means short drive times to the busiest commercial corridors in Central Florida, including the warehouse districts along the Beachline and the Turnpike."],
                "fr_h": "Local &amp; regional freight from Orlando",
                "fr_p": ["Central Florida is one of the busiest distribution hubs in the Southeast. We run local and regional freight for distributors, manufacturers and construction companies across the metro area.",
                         "Set up a dedicated schedule out of Orlando to Tampa, Jacksonville, Miami or further north — with the same dispatcher every time."],
                "cov_h": "Orlando metro &amp; surrounding counties",
                "cov_p": "Fastest response across Orange, Osceola, Seminole and Lake counties, and along I-4 from Volusia to Polk.",
                "places": ["Orlando", "Kissimmee", "Sanford", "Apopka", "Winter Park", "Lake Buena Vista", "Winter Garden", "Ocoee", "Clermont", "St. Cloud", "Oviedo", "Lake Nona", "Pine Castle", "Conway"],
                "faqs": [("Where is your Orlando yard?", "4980 Patch Rd, Orlando, FL 32822 — southeast Orlando, near Orlando International Airport and SR 528."),
                         ("Do you tow semis on I-4 at night?", "Yes. Heavy towing dispatch answers 24 hours a day at (407) 595-9726, including nights, weekends and holidays."),
                         ("Do you run local freight inside Orlando?", "Yes. Along with regional lanes, we handle local freight moves and recurring routes inside the Orlando metro area.")],
            },
            "es": {
                "title": "Grúa Pesada y Transporte de Carga en Orlando, FL | 24/7 | R&J Transport",
                "desc": "Grúa pesada 24/7 en Orlando y transporte de carga local desde nuestro patio en 4980 Patch Rd desde 2004. Semis, autobuses, equipo. Llame al (407) 595-9726.",
                "kicker": "Orlando, FL · Nuestra base desde 2004",
                "h1": 'Grúa Pesada y Carga en <span class="red-text">Orlando</span>',
                "lede": "Nuestro patio está en el sureste de Orlando, en 4980 Patch Rd. Aquí salen nuestros camiones y grúas cada día — y aquí respondemos más rápido.",
                "tow_h": "Grúa pesada 24/7 en Orlando",
                "tow_p": ["Desde la I-4 en el centro hasta la Beachline (SR 528), la SR 417 y el Florida Turnpike, remolcamos semis, tractocamiones, camiones caja, autobuses y equipo pesado a toda hora.",
                          "Estar cerca del Aeropuerto Internacional de Orlando nos da tiempos cortos hacia los corredores comerciales más activos de Florida Central, incluidas las zonas de almacenes junto a la Beachline y el Turnpike."],
                "fr_h": "Carga local y regional desde Orlando",
                "fr_p": ["Florida Central es uno de los centros de distribución más activos del Sureste. Movemos carga local y regional para distribuidores, fabricantes y constructoras en toda el área metropolitana.",
                         "Arme un horario dedicado desde Orlando hacia Tampa, Jacksonville, Miami o más al norte — con el mismo despachador siempre."],
                "cov_h": "Área metropolitana de Orlando y condados cercanos",
                "cov_p": "Respuesta más rápida en los condados Orange, Osceola, Seminole y Lake, y a lo largo de la I-4 de Volusia a Polk.",
                "places": ["Orlando", "Kissimmee", "Sanford", "Apopka", "Winter Park", "Lake Buena Vista", "Winter Garden", "Ocoee", "Clermont", "St. Cloud", "Oviedo", "Lake Nona", "Pine Castle", "Conway"],
                "faqs": [("¿Dónde está su patio en Orlando?", "4980 Patch Rd, Orlando, FL 32822 — sureste de Orlando, cerca del Aeropuerto Internacional de Orlando y la SR 528."),
                         ("¿Remolcan semis en la I-4 de noche?", "Sí. El despacho de grúa pesada atiende las 24 horas al (407) 595-9726, incluidas noches, fines de semana y feriados."),
                         ("¿Hacen carga local dentro de Orlando?", "Sí. Además de rutas regionales, hacemos movimientos locales y rutas recurrentes dentro del área metropolitana de Orlando.")],
            },
        },
    },
    {
        "key": "tampa",
        "slug": {"en": "tampa-fl", "es": "tampa-fl"},
        "name": {"en": "Tampa Bay", "es": "Tampa Bay"},
        "short": {"en": "Tampa", "es": "Tampa"},
        "card": {"en": "About 85 miles down I-4. Daily freight lanes to Tampa Bay and long-distance heavy towing to the west coast.",
                 "es": "Unas 85 millas por la I-4. Rutas de carga diarias a Tampa Bay y grúa pesada de larga distancia a la costa oeste."},
        "schema_areas": ["Tampa, FL", "Hillsborough County, FL", "Pinellas County, FL", "Polk County, FL"],
        "content": {
            "en": {
                "title": "Orlando to Tampa Freight Trucking & Heavy Towing | R&J Transport",
                "desc": "Freight lanes between Orlando and Tampa Bay on I-4, dedicated contract hauling and long-distance heavy towing. Orlando carrier since 2004. Call (407) 595-9726.",
                "kicker": "Tampa Bay · I-4 corridor",
                "h1": 'Freight &amp; Heavy Towing to <span class="red-text">Tampa Bay</span>',
                "lede": "The I-4 corridor between Orlando and Tampa is one of Florida's busiest freight lanes. We run it constantly.",
                "tow_h": "Heavy towing on the I-4 corridor",
                "tow_p": ["Breakdowns and accidents happen along I-4 through Polk County and into Hillsborough. We handle heavy towing and transport of trucks and equipment between Central Florida and the Tampa Bay area.",
                          "Need a disabled unit brought back to your Orlando shop, or moved from Tampa to your terminal? Call dispatch with the location and destination."],
                "fr_h": "Orlando ⇄ Tampa freight lanes",
                "fr_p": ["Roughly 85 road miles separate our yard from Tampa, which makes same-day turns realistic for recurring freight.",
                         "We serve distributors and builders moving freight to and from the Tampa Bay area, including loads tied to Port Tampa Bay and the Lakeland distribution corridor."],
                "cov_h": "Tampa Bay &amp; the I-4 corridor",
                "cov_p": "Hillsborough, Pinellas and Polk counties, plus everything along I-4 and I-75 on the west coast.",
                "places": ["Tampa", "St. Petersburg", "Clearwater", "Brandon", "Plant City", "Lakeland", "Winter Haven", "Riverview", "Wesley Chapel", "Sarasota"],
                "faqs": [("How far is Tampa from your yard?", "About 85 road miles via I-4, which keeps same-day round trips realistic."),
                         ("Do you offer dedicated Orlando–Tampa runs?", "Yes. We set up recurring and dedicated schedules on the Orlando–Tampa lane for companies with steady volume."),
                         ("Can you tow a truck from Tampa back to Orlando?", "Yes. We handle long-distance heavy towing and transport between Tampa Bay and Central Florida.")],
            },
            "es": {
                "title": "Transporte de Carga Orlando–Tampa y Grúa Pesada | R&J Transport",
                "desc": "Rutas de carga entre Orlando y Tampa Bay por la I-4, transporte dedicado por contrato y grúa pesada de larga distancia. Desde 2004. Llame al (407) 595-9726.",
                "kicker": "Tampa Bay · Corredor I-4",
                "h1": 'Carga y Grúa Pesada a <span class="red-text">Tampa Bay</span>',
                "lede": "El corredor I-4 entre Orlando y Tampa es una de las rutas de carga más activas de Florida. La recorremos constantemente.",
                "tow_h": "Grúa pesada en el corredor I-4",
                "tow_p": ["Las averías y accidentes ocurren en la I-4 por el condado Polk y hasta Hillsborough. Hacemos remolque pesado y traslado de camiones y equipo entre Florida Central y el área de Tampa Bay.",
                          "¿Necesita llevar una unidad averiada a su taller en Orlando o moverla de Tampa a su terminal? Llame al despacho con la ubicación y el destino."],
                "fr_h": "Rutas de carga Orlando ⇄ Tampa",
                "fr_p": ["Unas 85 millas por carretera separan nuestro patio de Tampa, lo que hace realistas los viajes de ida y vuelta el mismo día para carga recurrente.",
                         "Servimos a distribuidores y constructoras que mueven carga hacia y desde Tampa Bay, incluidas cargas ligadas a Port Tampa Bay y al corredor de distribución de Lakeland."],
                "cov_h": "Tampa Bay y el corredor I-4",
                "cov_p": "Condados Hillsborough, Pinellas y Polk, y todo lo que hay a lo largo de la I-4 y la I-75 en la costa oeste.",
                "places": ["Tampa", "St. Petersburg", "Clearwater", "Brandon", "Plant City", "Lakeland", "Winter Haven", "Riverview", "Wesley Chapel", "Sarasota"],
                "faqs": [("¿Qué tan lejos está Tampa de su patio?", "Unas 85 millas por carretera vía la I-4, lo que permite viajes de ida y vuelta el mismo día."),
                         ("¿Ofrecen viajes dedicados Orlando–Tampa?", "Sí. Armamos horarios recurrentes y dedicados en la ruta Orlando–Tampa para empresas con volumen constante."),
                         ("¿Pueden remolcar un camión de Tampa a Orlando?", "Sí. Hacemos remolque pesado y traslado de larga distancia entre Tampa Bay y Florida Central.")],
            },
        },
    },
    {
        "key": "miami",
        "slug": {"en": "miami-south-florida", "es": "miami-sur-de-florida"},
        "name": {"en": "Miami & South Florida", "es": "Miami y el Sur de Florida"},
        "short": {"en": "South Florida", "es": "el Sur de Florida"},
        "card": {"en": "About 235 miles via the Turnpike. Recurring freight to Miami-Dade, Broward and Palm Beach.",
                 "es": "Unas 235 millas por el Turnpike. Carga recurrente a Miami-Dade, Broward y Palm Beach."},
        "schema_areas": ["Miami, FL", "Miami-Dade County, FL", "Broward County, FL", "Palm Beach County, FL"],
        "content": {
            "en": {
                "title": "Orlando to Miami Freight Trucking & Heavy Transport | R&J Transport",
                "desc": "Recurring Orlando–Miami freight lanes via the Florida Turnpike and I-95. Miami-Dade, Broward, Palm Beach. Contract hauling and heavy transport since 2004.",
                "kicker": "South Florida · Turnpike &amp; I-95",
                "h1": 'Orlando to <span class="red-text">Miami</span> Freight &amp; Heavy Transport',
                "lede": "Orlando–Miami is one of the core lanes we have run for years. Recurring capacity into Miami-Dade, Broward and Palm Beach.",
                "tow_h": "Long-distance heavy towing &amp; transport",
                "tow_p": ["Need a disabled truck, bus or piece of equipment moved between South Florida and Central Florida? We handle long-distance heavy towing and transport along the Turnpike and I-95.",
                          "Call dispatch with the pickup location and destination and we will give you a straight answer on timing."],
                "fr_h": "Orlando ⇄ Miami freight lanes",
                "fr_p": ["South Florida's ports and distribution centers — PortMiami, Port Everglades and the Doral and Medley warehouse districts — move huge volumes north to Central Florida and back.",
                         "We run recurring and dedicated freight on this lane for companies that need consistent capacity, not a different broker truck every week."],
                "cov_h": "Miami-Dade, Broward &amp; Palm Beach",
                "cov_p": "The full South Florida metro, from the Palm Beaches down to Homestead.",
                "places": ["Miami", "Doral", "Hialeah", "Medley", "Miami Gardens", "Fort Lauderdale", "Pompano Beach", "West Palm Beach", "Boca Raton", "Homestead"],
                "faqs": [("How far is Miami from Orlando?", "About 235 road miles via the Florida Turnpike."),
                         ("Do you run recurring Miami freight?", "Yes. Orlando–Miami is one of our core lanes, with recurring and dedicated options for steady volume."),
                         ("Do you serve Port Everglades and PortMiami?", "We handle freight moving to and from South Florida's port and warehouse areas. Send your pickup and delivery details for a quote.")],
            },
            "es": {
                "title": "Transporte de Carga Orlando–Miami y Traslado Pesado | R&J Transport",
                "desc": "Rutas de carga recurrentes Orlando–Miami por el Florida Turnpike y la I-95. Miami-Dade, Broward, Palm Beach. Transporte por contrato y traslado pesado desde 2004.",
                "kicker": "Sur de Florida · Turnpike y I-95",
                "h1": 'Carga y Traslado Pesado de Orlando a <span class="red-text">Miami</span>',
                "lede": "Orlando–Miami es una de las rutas principales que cubrimos desde hace años. Capacidad recurrente hacia Miami-Dade, Broward y Palm Beach.",
                "tow_h": "Grúa pesada y traslado de larga distancia",
                "tow_p": ["¿Necesita mover un camión averiado, un autobús o equipo entre el Sur de Florida y Florida Central? Hacemos remolque pesado y traslado de larga distancia por el Turnpike y la I-95.",
                          "Llame al despacho con el lugar de recogida y el destino y le daremos una respuesta clara sobre los tiempos."],
                "fr_h": "Rutas de carga Orlando ⇄ Miami",
                "fr_p": ["Los puertos y centros de distribución del Sur de Florida — PortMiami, Port Everglades y las zonas de almacenes de Doral y Medley — mueven grandes volúmenes hacia Florida Central y de regreso.",
                         "Operamos carga recurrente y dedicada en esta ruta para empresas que necesitan capacidad constante, no un camión distinto de un bróker cada semana."],
                "cov_h": "Miami-Dade, Broward y Palm Beach",
                "cov_p": "Toda el área metropolitana del Sur de Florida, desde Palm Beach hasta Homestead.",
                "places": ["Miami", "Doral", "Hialeah", "Medley", "Miami Gardens", "Fort Lauderdale", "Pompano Beach", "West Palm Beach", "Boca Raton", "Homestead"],
                "faqs": [("¿Qué distancia hay de Orlando a Miami?", "Unas 235 millas por carretera vía el Florida Turnpike."),
                         ("¿Tienen carga recurrente a Miami?", "Sí. Orlando–Miami es una de nuestras rutas principales, con opciones recurrentes y dedicadas para volumen constante."),
                         ("¿Atienden Port Everglades y PortMiami?", "Movemos carga hacia y desde las zonas portuarias y de almacenes del Sur de Florida. Envíe los datos de recogida y entrega para cotizar.")],
            },
        },
    },
    {
        "key": "jacksonville",
        "slug": {"en": "jacksonville-fl", "es": "jacksonville-fl"},
        "name": {"en": "Jacksonville & North Florida", "es": "Jacksonville y el Norte de Florida"},
        "short": {"en": "Jacksonville", "es": "Jacksonville"},
        "card": {"en": "About 140 miles up I-95. Freight to JAXPORT and the I-95 / I-10 interchange — the gateway north.",
                 "es": "Unas 140 millas por la I-95. Carga a JAXPORT y al cruce I-95 / I-10 — la puerta hacia el norte."},
        "schema_areas": ["Jacksonville, FL", "Duval County, FL", "St. Johns County, FL", "Clay County, FL"],
        "content": {
            "en": {
                "title": "Orlando to Jacksonville Freight Trucking & Heavy Towing | R&J Transport",
                "desc": "Freight lanes between Orlando and Jacksonville on I-95, JAXPORT-area hauling and long-distance heavy towing. Orlando carrier since 2004. Call (407) 595-9726.",
                "kicker": "North Florida · I-95 &amp; I-10",
                "h1": 'Freight &amp; Heavy Towing to <span class="red-text">Jacksonville</span>',
                "lede": "Jacksonville is where Florida freight meets I-10 and the northbound I-95 corridor. It's a lane we run regularly — and the gateway to our Southeast routes.",
                "tow_h": "Heavy towing &amp; transport to North Florida",
                "tow_p": ["We move disabled trucks, buses and equipment between Central and North Florida along I-95 and I-4, for fleets, owner-operators and leasing companies.",
                          "Tell dispatch where the unit is and where it needs to go — we will give you a realistic timeline before we roll."],
                "fr_h": "Orlando ⇄ Jacksonville freight",
                "fr_p": ["Jacksonville's port (JAXPORT) and the large distribution centers along I-95 and I-10 make it a major hub for Florida-bound freight.",
                         "We run recurring loads between Orlando and Jacksonville and connect North Florida freight to lanes heading into Georgia and further north."],
                "cov_h": "Duval, St. Johns, Clay &amp; Nassau",
                "cov_p": "The full Jacksonville metro plus the I-95 corridor through Daytona Beach and St. Augustine.",
                "places": ["Jacksonville", "Orange Park", "St. Augustine", "Fernandina Beach", "Palatka", "Daytona Beach", "Palm Coast", "Lake City"],
                "faqs": [("How far is Jacksonville from your yard?", "About 140 road miles, mostly via I-95."),
                         ("Do you connect Jacksonville freight to Georgia?", "Yes. Jacksonville is the jumping-off point for our lanes into Savannah, Atlanta and further north."),
                         ("Can you tow a semi from Jacksonville to Orlando?", "Yes. Call (407) 595-9726 with the truck's location and destination.")],
            },
            "es": {
                "title": "Transporte de Carga Orlando–Jacksonville y Grúa Pesada | R&J Transport",
                "desc": "Rutas de carga entre Orlando y Jacksonville por la I-95, carga en el área de JAXPORT y grúa pesada de larga distancia. Desde 2004. Llame al (407) 595-9726.",
                "kicker": "Norte de Florida · I-95 y I-10",
                "h1": 'Carga y Grúa Pesada a <span class="red-text">Jacksonville</span>',
                "lede": "Jacksonville es donde la carga de Florida se une a la I-10 y al corredor I-95 hacia el norte. La cubrimos con frecuencia — y es la puerta a nuestras rutas del Sureste.",
                "tow_h": "Grúa pesada y traslado al Norte de Florida",
                "tow_p": ["Movemos camiones averiados, autobuses y equipo entre Florida Central y el Norte de Florida por la I-95 y la I-4, para flotas, operadores independientes y arrendadoras.",
                          "Dígale al despacho dónde está la unidad y a dónde va — le daremos un tiempo realista antes de salir."],
                "fr_h": "Carga Orlando ⇄ Jacksonville",
                "fr_p": ["El puerto de Jacksonville (JAXPORT) y los grandes centros de distribución en la I-95 y la I-10 lo hacen un centro clave para la carga que entra a Florida.",
                         "Operamos cargas recurrentes entre Orlando y Jacksonville y conectamos la carga del Norte de Florida con rutas hacia Georgia y más al norte."],
                "cov_h": "Duval, St. Johns, Clay y Nassau",
                "cov_p": "Toda el área metropolitana de Jacksonville y el corredor I-95 por Daytona Beach y St. Augustine.",
                "places": ["Jacksonville", "Orange Park", "St. Augustine", "Fernandina Beach", "Palatka", "Daytona Beach", "Palm Coast", "Lake City"],
                "faqs": [("¿Qué tan lejos está Jacksonville de su patio?", "Unas 140 millas por carretera, principalmente por la I-95."),
                         ("¿Conectan carga de Jacksonville con Georgia?", "Sí. Jacksonville es el punto de partida de nuestras rutas hacia Savannah, Atlanta y más al norte."),
                         ("¿Pueden remolcar un semi de Jacksonville a Orlando?", "Sí. Llame al (407) 595-9726 con la ubicación del camión y el destino.")],
            },
        },
    },
    {
        "key": "southeast",
        "slug": {"en": "southeast-us", "es": "sureste-eeuu"},
        "name": {"en": "Georgia, Alabama & the Southeast", "es": "Georgia, Alabama y el Sureste"},
        "short": {"en": "the Southeast", "es": "el Sureste"},
        "card": {"en": "Florida's neighbors and further north: Georgia, Alabama, the Carolinas and Tennessee via I-75 and I-95.",
                 "es": "Los vecinos de Florida y más al norte: Georgia, Alabama, las Carolinas y Tennessee por la I-75 y la I-95."},
        "schema_areas": ["Georgia", "Alabama", "South Carolina", "North Carolina", "Tennessee"],
        "content": {
            "en": {
                "title": "Florida to Georgia, Alabama & Carolinas Freight Trucking | R&J Transport",
                "desc": "Out-of-state freight lanes from Orlando to Georgia, Alabama, the Carolinas and Tennessee via I-75 and I-95. Contract hauling and heavy transport since 2004.",
                "kicker": "Out of state · I-75 &amp; I-95 northbound",
                "h1": 'Florida to the <span class="red-text">Southeast</span> &amp; Beyond',
                "lede": "We don't stop at the state line. From Orlando we run freight into Georgia and Alabama, and further north into the Carolinas and Tennessee.",
                "tow_h": "Long-distance heavy transport",
                "tow_p": ["Need a disabled truck, bus or piece of heavy equipment brought home to Florida from out of state — or delivered north? We handle long-distance heavy towing and transport across the Southeast.",
                          "Call dispatch with both locations and the vehicle details for a quote and timeline."],
                "fr_h": "Northbound &amp; southbound lanes",
                "fr_p": ["I-75 takes our trucks to Atlanta, Chattanooga and Nashville; I-95 runs to Savannah, Charleston and the Carolinas; I-10 connects west to Tallahassee, Mobile and Alabama.",
                         "For shippers with steady volume between Florida and the Southeast, we offer dedicated and recurring capacity with the same dispatcher on every load."],
                "cov_h": "States we run",
                "cov_p": "Approximate road miles from Orlando: Savannah ~280, Atlanta ~440, Charlotte ~525, Nashville ~685. Further destinations quoted on request.",
                "places": ["Georgia", "Alabama", "South Carolina", "North Carolina", "Tennessee", "Savannah", "Atlanta", "Mobile", "Birmingham", "Charleston", "Charlotte", "Nashville"],
                "faqs": [("Do you haul freight outside Florida?", "Yes. We run lanes from Florida into Georgia, Alabama, South Carolina, North Carolina, Tennessee and further north on request."),
                         ("Can you set up a dedicated Florida–Atlanta lane?", "Yes. Send your weekly volume and service windows and we will build a capacity plan."),
                         ("Do you bring disabled trucks back to Florida?", "Yes. We handle long-distance heavy transport of trucks, buses and equipment between the Southeast and Florida.")],
            },
            "es": {
                "title": "Transporte de Carga de Florida a Georgia, Alabama y las Carolinas | R&J Transport",
                "desc": "Rutas de carga interestatales desde Orlando a Georgia, Alabama, las Carolinas y Tennessee por la I-75 y la I-95. Transporte por contrato y traslado pesado desde 2004.",
                "kicker": "Fuera del estado · I-75 e I-95 al norte",
                "h1": 'De Florida al <span class="red-text">Sureste</span> y Más Allá',
                "lede": "No nos detenemos en la frontera del estado. Desde Orlando llevamos carga a Georgia y Alabama, y más al norte a las Carolinas y Tennessee.",
                "tow_h": "Traslado pesado de larga distancia",
                "tow_p": ["¿Necesita traer de vuelta a Florida un camión averiado, un autobús o equipo pesado desde otro estado — o llevarlo al norte? Hacemos remolque pesado y traslado de larga distancia en el Sureste.",
                          "Llame al despacho con ambas ubicaciones y los datos del vehículo para cotizar y darle tiempos."],
                "fr_h": "Rutas hacia el norte y hacia el sur",
                "fr_p": ["La I-75 lleva nuestros camiones a Atlanta, Chattanooga y Nashville; la I-95 a Savannah, Charleston y las Carolinas; la I-10 conecta al oeste con Tallahassee, Mobile y Alabama.",
                         "Para embarcadores con volumen constante entre Florida y el Sureste, ofrecemos capacidad dedicada y recurrente con el mismo despachador en cada carga."],
                "cov_h": "Estados que cubrimos",
                "cov_p": "Millas aproximadas por carretera desde Orlando: Savannah ~280, Atlanta ~440, Charlotte ~525, Nashville ~685. Otros destinos se cotizan bajo pedido.",
                "places": ["Georgia", "Alabama", "Carolina del Sur", "Carolina del Norte", "Tennessee", "Savannah", "Atlanta", "Mobile", "Birmingham", "Charleston", "Charlotte", "Nashville"],
                "faqs": [("¿Transportan carga fuera de Florida?", "Sí. Operamos rutas desde Florida hacia Georgia, Alabama, Carolina del Sur, Carolina del Norte, Tennessee y más al norte bajo pedido."),
                         ("¿Pueden armar una ruta dedicada Florida–Atlanta?", "Sí. Envíe su volumen semanal y ventanas de servicio y armamos un plan de capacidad."),
                         ("¿Traen camiones averiados de vuelta a Florida?", "Sí. Hacemos traslado pesado de larga distancia de camiones, autobuses y equipo entre el Sureste y Florida.")],
            },
        },
    },
]

# ---------------------------------------------------------------------------
# Blog posts (HTML bodies). Keep facts general and accurate; no invented stats.
# ---------------------------------------------------------------------------
BLOG_POSTS = [
    {
        "key": "breakdown",
        "date": "2026-11-13",
        "img": "wrecker",
        "mode": "tow",
        "slug": {"en": "semi-truck-breakdown-florida-what-to-do", "es": "camion-averiado-en-florida-que-hacer"},
        "category": {"en": "Heavy towing", "es": "Grúa pesada"},
        "title": {"en": "Semi Truck Broke Down in Florida? What to Do in the First 30 Minutes",
                  "es": "¿Se le averió el camión en Florida? Qué hacer en los primeros 30 minutos"},
        "seo_title": {"en": "Semi Truck Breakdown in Florida: What to Do First | R&J Transport",
                      "es": "Camión Averiado en Florida: Qué Hacer Primero | R&J Transport"},
        "excerpt": {"en": "A step-by-step checklist for drivers and fleet managers when a tractor-trailer goes down on I-4, the Turnpike or any Florida highway.",
                    "es": "Una lista paso a paso para choferes y gerentes de flota cuando un tractocamión se detiene en la I-4, el Turnpike o cualquier carretera de Florida."},
        "body": {
            "en": """
<p>A loaded tractor-trailer stopped on a Florida highway is a safety problem first and a money problem right after. What you do in the first half hour decides how fast the unit gets moving again — and how much the delay ends up costing.</p>
<h3>1. Get safe and visible</h3>
<p>Move as far onto the shoulder as you safely can. Turn on your hazard lights and put out your warning devices as federal rules require for stopped commercial vehicles. If anyone is hurt, or the truck is blocking a travel lane, call 911 before anything else.</p>
<h3>2. Figure out exactly where you are</h3>
<p>Dispatchers need a precise location to send the right truck to the right place. Note the highway, direction of travel, nearest mile marker or exit, and any landmarks. On I-4 through Orlando or the Turnpike, the mile marker and direction save a lot of back-and-forth.</p>
<h3>3. Know what you're hauling</h3>
<p>Whether the trailer is loaded matters a lot for heavy towing. Have the approximate weight, the type of freight and any hazmat information ready. A loaded trailer may need different equipment than a bobtail tractor.</p>
<h3>4. Call a heavy-duty tow company — not a light-duty one</h3>
<p>Standard tow trucks are not built for Class 8 trucks. Calling a heavy towing company directly avoids the delay of a light-duty truck showing up and having to call someone else. When you call, tell the dispatcher:</p>
<ul><li>Location, direction and mile marker</li><li>Truck and trailer type, and whether it's loaded</li><li>What happened — mechanical failure, tire, accident, stuck</li><li>Where the unit needs to go (your shop, a dealer, your terminal)</li><li>Fleet, insurance or purchase order information</li></ul>
<h3>5. Loop in your fleet manager and customer</h3>
<p>If freight is going to be late, the sooner the receiver knows, the better. Fleet managers should log the tow details, the destination shop and the expected timeline so the next decisions — repair, swap tractor, or transfer the load — happen quickly.</p>
<h3>Set your fleet up before it happens</h3>
<p>Companies running regular freight in Florida save time by setting up an account with a heavy towing provider ahead of time. Dispatch already has your billing, preferred shops and contact list on file, so the call is shorter and the truck rolls faster.</p>
<p>R&amp;J Transport Service Inc has been towing heavy vehicles out of Orlando since 2004. Our dispatch line, <a href="tel:+14075959726">(407) 595-9726</a>, is answered 24 hours a day.</p>
""",
            "es": """
<p>Un tractocamión cargado detenido en una carretera de Florida es primero un problema de seguridad y enseguida un problema de dinero. Lo que haga en la primera media hora decide qué tan rápido vuelve a moverse la unidad — y cuánto termina costando el retraso.</p>
<h3>1. Póngase a salvo y hágase visible</h3>
<p>Muévase lo más que pueda al acotamiento de forma segura. Encienda las luces intermitentes y coloque los dispositivos de advertencia como exigen las normas federales para vehículos comerciales detenidos. Si alguien está herido o el camión bloquea un carril, llame al 911 antes que nada.</p>
<h3>2. Ubique exactamente dónde está</h3>
<p>El despacho necesita una ubicación precisa para enviar la grúa correcta al lugar correcto. Anote la carretera, el sentido, el marcador de milla o salida más cercana y cualquier referencia. En la I-4 por Orlando o en el Turnpike, el marcador de milla y el sentido ahorran mucho tiempo.</p>
<h3>3. Sepa qué lleva</h3>
<p>Que el tráiler vaya cargado importa mucho para la grúa pesada. Tenga a mano el peso aproximado, el tipo de carga y cualquier información de materiales peligrosos. Un tráiler cargado puede necesitar equipo distinto al de un tractor solo.</p>
<h3>4. Llame a una grúa pesada — no a una liviana</h3>
<p>Las grúas estándar no están hechas para camiones Clase 8. Llamar directamente a una empresa de grúa pesada evita que llegue una grúa liviana y tenga que llamar a otra. Cuando llame, dígale al despachador:</p>
<ul><li>Ubicación, sentido y marcador de milla</li><li>Tipo de camión y tráiler, y si va cargado</li><li>Qué pasó — falla mecánica, llanta, accidente, atascado</li><li>A dónde hay que llevar la unidad (su taller, un concesionario, su terminal)</li><li>Datos de flota, seguro u orden de compra</li></ul>
<h3>5. Avise a su gerente de flota y a su cliente</h3>
<p>Si la carga va a llegar tarde, mientras antes lo sepa el receptor, mejor. Los gerentes de flota deben registrar los datos del remolque, el taller de destino y el tiempo estimado para que las siguientes decisiones — reparar, cambiar de tractor o transferir la carga — se tomen rápido.</p>
<h3>Registre su flota antes de que pase</h3>
<p>Las empresas que mueven carga con frecuencia en Florida ahorran tiempo abriendo una cuenta con una empresa de grúa pesada por adelantado. El despacho ya tiene su facturación, talleres preferidos y contactos, así que la llamada es más corta y la grúa sale más rápido.</p>
<p>R&amp;J Transport Service Inc remolca vehículos pesados desde Orlando desde 2004. Nuestra línea de despacho, <a href="tel:+14075959726">(407) 595-9726</a>, atiende las 24 horas.</p>
""",
        },
    },
    {
        "key": "dedicated",
        "date": "2026-11-13",
        "img": "cargo-flatbed",
        "mode": "freight",
        "slug": {"en": "dedicated-freight-vs-spot-loads-florida", "es": "carga-dedicada-vs-cargas-spot-florida"},
        "category": {"en": "Freight contracts", "es": "Contratos de carga"},
        "title": {"en": "Dedicated Freight Lanes vs. Spot Loads: What Florida Shippers Should Know",
                  "es": "Rutas de carga dedicadas vs. cargas spot: lo que deben saber las empresas en Florida"},
        "seo_title": {"en": "Dedicated Freight vs Spot Loads for Florida Shippers | R&J Transport",
                      "es": "Carga Dedicada vs Cargas Spot para Empresas en Florida | R&J Transport"},
        "excerpt": {"en": "When does it make sense to lock in a dedicated carrier instead of buying trucks load by load? A practical guide for logistics and procurement teams.",
                    "es": "¿Cuándo conviene asegurar un transportista dedicado en lugar de comprar camiones carga por carga? Una guía práctica para equipos de logística y compras."},
        "body": {
            "en": """
<p>Every shipper eventually faces the same question: keep buying trucks on the spot market one load at a time, or commit to a carrier on dedicated or contract lanes? Both have a place. Here is how to think about it.</p>
<h3>What "spot" really means</h3>
<p>Spot freight is priced and booked load by load, usually close to the ship date. It's flexible — you only pay for what you move — but price and availability move with the market. When capacity is tight, rates jump and trucks get harder to find. You may also see a different carrier, and a different driver, on every load.</p>
<h3>What "dedicated" or "contract" means</h3>
<p>With dedicated or contract freight, you agree with a carrier on lanes, volume and a schedule for a period of time. The carrier plans its trucks and drivers around your freight. In return you get predictable capacity, consistent service and a rate that doesn't swing every week.</p>
<h3>Signs you're ready for dedicated lanes</h3>
<ul><li>You ship the same origin and destination pairs every week</li><li>Missed or late pickups cause real problems on your dock or job site</li><li>You spend too much time re-booking trucks and chasing status</li><li>Your receivers expect the same appointment windows every time</li><li>You want one point of contact who already knows your freight</li></ul>
<h3>When spot still makes sense</h3>
<p>Truly one-off shipments, unpredictable seasonal peaks and lanes you rarely use are good candidates for the spot market. Many companies run a hybrid: core recurring lanes on contract, overflow on spot.</p>
<h3>Questions to ask a dedicated carrier</h3>
<ul><li>Are you an asset-based carrier or a broker?</li><li>How long have you been operating, and from where?</li><li>Which lanes do you already run regularly?</li><li>Who do I call for status, and are they reachable after hours?</li><li>What happens if a truck breaks down on my load?</li></ul>
<p>That last question matters. At R&amp;J Transport Service Inc we run heavy towing in-house, so a mechanical problem on a contract load doesn't turn into a search for a wrecker.</p>
<h3>How to start</h3>
<p>Pull a few months of shipment data, group it by lane and frequency, and share it with the carrier. A good carrier will come back with a rate and a realistic capacity commitment — not just a number. We have been running freight out of Orlando since 2004; <a href="/freight-trucking/#quote">send us your lanes</a> and we'll build a plan.</p>
""",
            "es": """
<p>Toda empresa que envía carga llega a la misma pregunta: ¿seguir comprando camiones en el mercado spot carga por carga, o comprometerse con un transportista en rutas dedicadas o por contrato? Ambos tienen su lugar. Así conviene pensarlo.</p>
<h3>Qué significa realmente "spot"</h3>
<p>La carga spot se cotiza y reserva carga por carga, normalmente cerca de la fecha de envío. Es flexible — solo paga lo que mueve — pero el precio y la disponibilidad cambian con el mercado. Cuando la capacidad escasea, las tarifas suben y cuesta más conseguir camiones. Además, puede tener un transportista y un chofer distinto en cada carga.</p>
<h3>Qué significa "dedicado" o "por contrato"</h3>
<p>Con carga dedicada o por contrato, usted acuerda con un transportista rutas, volumen y horario por un periodo. El transportista planifica camiones y choferes según su carga. A cambio, usted obtiene capacidad predecible, servicio constante y una tarifa que no cambia cada semana.</p>
<h3>Señales de que está listo para rutas dedicadas</h3>
<ul><li>Envía entre los mismos orígenes y destinos cada semana</li><li>Las recogidas perdidas o tardías causan problemas reales en su andén u obra</li><li>Pierde demasiado tiempo reservando camiones y persiguiendo estatus</li><li>Sus receptores esperan las mismas ventanas de cita siempre</li><li>Quiere un solo contacto que ya conozca su carga</li></ul>
<h3>Cuándo el spot sigue teniendo sentido</h3>
<p>Los envíos realmente únicos, los picos de temporada impredecibles y las rutas que casi no usa son buenos candidatos para el mercado spot. Muchas empresas usan un modelo mixto: rutas principales por contrato y el excedente en spot.</p>
<h3>Preguntas para un transportista dedicado</h3>
<ul><li>¿Tiene equipo propio o es un bróker?</li><li>¿Cuánto tiempo lleva operando y desde dónde?</li><li>¿Qué rutas ya cubre con regularidad?</li><li>¿A quién llamo para estatus y responde fuera de horario?</li><li>¿Qué pasa si un camión se avería con mi carga?</li></ul>
<p>Esa última pregunta importa. En R&amp;J Transport Service Inc tenemos grúa pesada propia, así que un problema mecánico en una carga por contrato no se convierte en una búsqueda de grúa.</p>
<h3>Cómo empezar</h3>
<p>Reúna unos meses de datos de envíos, agrúpelos por ruta y frecuencia y compártalos con el transportista. Un buen transportista le responderá con una tarifa y un compromiso de capacidad realista — no solo un número. Movemos carga desde Orlando desde 2004; <a href="/es/transporte-de-carga/#quote">envíenos sus rutas</a> y armamos un plan.</p>
""",
        },
    },
    {
        "key": "choose",
        "date": "2026-11-13",
        "img": "wrecker",
        "mode": "tow",
        "slug": {"en": "how-to-choose-heavy-towing-company", "es": "como-elegir-empresa-de-grua-pesada"},
        "category": {"en": "Fleet management", "es": "Gestión de flotas"},
        "title": {"en": "How to Choose a Heavy Towing Company for Your Fleet",
                  "es": "Cómo elegir una empresa de grúa pesada para su flota"},
        "seo_title": {"en": "How to Choose a Heavy Towing Company for Your Fleet | R&J Transport",
                      "es": "Cómo Elegir una Empresa de Grúa Pesada para su Flota | R&J Transport"},
        "excerpt": {"en": "Seven things fleet managers should check before a breakdown happens — from 24/7 dispatch to equipment, coverage area and track record.",
                    "es": "Siete cosas que un gerente de flota debe revisar antes de una avería — desde despacho 24/7 hasta equipo, cobertura y trayectoria."},
        "body": {
            "en": """
<p>The worst time to pick a heavy towing company is at 2 a.m. with a loaded truck on the shoulder. Fleet managers who choose ahead of time get faster, cheaper and less stressful recoveries. Here's what to check.</p>
<h3>1. Real 24/7 dispatch</h3>
<p>Breakdowns don't keep business hours. Call the number at night and see who answers. You want a dispatcher who can make decisions, not a voicemail.</p>
<h3>2. Heavy-duty equipment</h3>
<p>Ask what the company can tow: tractor-trailers, loaded trailers, buses, dump trucks, construction equipment. A company that specializes in heavy towing will tell you plainly what it can and can't handle.</p>
<h3>3. Coverage that matches your routes</h3>
<p>If your trucks run I-4, I-75 and I-95, your towing partner should cover those corridors — and be able to handle long-distance tows back to your home shop.</p>
<h3>4. Track record</h3>
<p>How long has the company been in business, and where is its yard? A business that has operated from the same city for many years has a reputation to protect.</p>
<h3>5. Clear communication</h3>
<p>You need an honest ETA, updates if something changes, and clear paperwork for billing and insurance. Ask how they keep fleet managers in the loop.</p>
<h3>6. Fleet accounts</h3>
<p>A fleet account means dispatch already has your billing details, preferred repair shops and contacts. That turns a long phone call into a short one.</p>
<h3>7. Bonus: freight capability</h3>
<p>A towing company that also runs freight understands what a stopped load means for your customer. At R&amp;J Transport Service Inc we've done both out of Orlando since 2004.</p>
<p>Want to set up your fleet before you need us? Call <a href="tel:+14075959726">(407) 595-9726</a> or <a href="/heavy-towing/#quote">send a request</a>.</p>
""",
            "es": """
<p>El peor momento para elegir una empresa de grúa pesada es a las 2 a.m. con un camión cargado en el acotamiento. Los gerentes de flota que eligen con anticipación logran rescates más rápidos, más baratos y con menos estrés. Esto es lo que debe revisar.</p>
<h3>1. Despacho 24/7 de verdad</h3>
<p>Las averías no respetan horarios. Llame al número de noche y vea quién contesta. Usted quiere un despachador que pueda tomar decisiones, no un buzón de voz.</p>
<h3>2. Equipo para trabajo pesado</h3>
<p>Pregunte qué pueden remolcar: tractocamiones, tráileres cargados, autobuses, volteos, equipo de construcción. Una empresa especializada en grúa pesada le dirá con claridad qué puede y qué no puede manejar.</p>
<h3>3. Cobertura que coincida con sus rutas</h3>
<p>Si sus camiones recorren la I-4, la I-75 y la I-95, su proveedor de grúa debe cubrir esos corredores — y poder hacer remolques de larga distancia hasta su taller.</p>
<h3>4. Trayectoria</h3>
<p>¿Cuánto tiempo lleva la empresa en el negocio y dónde está su patio? Un negocio que opera desde la misma ciudad por muchos años tiene una reputación que cuidar.</p>
<h3>5. Comunicación clara</h3>
<p>Necesita un tiempo de llegada honesto, avisos si algo cambia y documentación clara para facturación y seguros. Pregunte cómo mantienen informados a los gerentes de flota.</p>
<h3>6. Cuentas de flota</h3>
<p>Una cuenta de flota significa que el despacho ya tiene sus datos de facturación, talleres preferidos y contactos. Eso convierte una llamada larga en una corta.</p>
<h3>7. Extra: capacidad de carga</h3>
<p>Una empresa de grúas que también mueve carga entiende lo que significa una carga detenida para su cliente. En R&amp;J Transport Service Inc hacemos ambas cosas desde Orlando desde 2004.</p>
<p>¿Quiere registrar su flota antes de necesitarnos? Llame al <a href="tel:+14075959726">(407) 595-9726</a> o <a href="/es/grua-pesada/#quote">envíe una solicitud</a>.</p>
""",
        },
    },
]
