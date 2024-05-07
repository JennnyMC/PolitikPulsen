import math
import flet as ft

def main(page: ft.Page):
    page.title = "PolitikPulsen"
    BG = "#1A5577"
    MC = "#60AEDA"
    TC = "#B5FFB3"

    def add_images_to_values_view():
        # List of image URLs
        image_urls = [
            "https://upload.wikimedia.org/wikipedia/commons/0/00/V%C3%A4nsterpartiet_logo.svg",
            "https://bilder.riksdagen.se/publishedmedia/3sgk8lpoqlu2mht11nov/MP_partilogga.png",
            "https://bilder.riksdagen.se/publishedmedia/e9omiy7wkxkhts7ptwal/Symbol_Socialdemokraterna-_134px.png",
            "https://upload.wikimedia.org/wikipedia/commons/3/33/C_v1.svg",
            "https://upload.wikimedia.org/wikipedia/commons/c/c7/L_v1.svg",
            "https://upload.wikimedia.org/wikipedia/commons/8/85/M_v1.svg",
            "https://bilder.riksdagen.se/publishedmedia/bnz3yl48fswzmc8cd4m8/KD_partilogga.png",
            "https://bilder.riksdagen.se/publishedmedia/6gxtyz3j95i9xr0ejrbn/Sveriedemokraterna_132px.png",
        ]

        # Add images to the row
        images = ft.Row(expand=1, wrap=False, scroll="always")
        for url in image_urls:
            images.controls.append(
                ft.Image(
                    src=url,
                    width=100,
                    height=100,
                    fit=ft.ImageFit.FIT_HEIGHT,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                )
            )
        return images
    
    

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("PolitikPulsen"), bgcolor=MC),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.ElevatedButton("Åsiktsjämförelse",icon="ARROW_FORWARD_IOS", on_click=lambda _: page.go("/compare")),
                                ft.ElevatedButton("Genomförda Vallöften", icon="ARROW_FORWARD_IOS", on_click=lambda _: page.go("/stats")),
                                ft.ElevatedButton("Partiståndpunkter", icon="ARROW_FORWARD_IOS", on_click=lambda _: page.go("/values")),
                                ft.ElevatedButton("Vad Händer Hos Dig?", icon="ARROW_FORWARD_IOS", on_click=lambda _:page.go("/local")),
                                ft.ElevatedButton("Quiz", icon="STAR_ROUNDED", on_click=lambda _:page.go("/quest")),
                                ft.ElevatedButton("Topplista", icon="STAR_ROUNDED", on_click=lambda _:page.go("/toplist"))
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        bgcolor = BG,
                        border_radius=35,
                        width=350,
                        height=700,
                        alignment=ft.alignment.center
                    )
                ],
            )
        )
        print(page.route)
        if page.route == "/compare":
            dd = ft.Dropdown(
                    options=[
                        ft.dropdown.Option("Skola"),
                        ft.dropdown.Option("Brottsbekämpning"),
                        ft.dropdown.Option("Välfärd"),
                        ft.dropdown.Option("Integration"),
                        ft.dropdown.Option("Klimat"),
                        ft.dropdown.Option("Försvar"),
                    ],
                    width=200,
                    on_change=lambda _:page.go("/" + dd.value.lower() )
            )
            page.views.append(
                ft.View(
                    "/compare",
                    [
                        ft.AppBar(title=ft.Text("Jämför Ståndpunkter"), bgcolor=MC),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            content= ft.Stack(
                                controls=[
                                    ft.Text("\n "),  # newline added here
                                    ft.Text("\n "),  # additional newli
                                    ft.Text("         Välj parti", size=20, color=ft.colors.WHITE, italic=True),
                                    dd,
                                ],
                            )
                        )
                    ],
                )
            )
        page.update()

        if page.route == "/skola":
            page.views.append(
                ft.View(
                    "/skola",
                    [
                        ft.AppBar(title=ft.Text("Jämför Ståndpunkter - Skola"), bgcolor=MC),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            content = ft.Column(
                                spacing=15,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Text(" "),
                                    ft.Text(" "),
                                    ft.Text("   - Moderaterna betonar höjda kunskapskrav och ökad lärarkompetens med en inriktning på kärnämnena samt valfrihet för elever och föräldrar genom fler skolalternativ.", color=ft.colors.WHITE),
                                    ft.Text("   - Socialdemokraterna fokuserar på att förbättra likvärdigheten i skolan genom resurstillskott till socioekonomiskt utsatta områden och stärkande av läraryrkets status.", color=ft.colors.WHITE),
                                    ft.Text("   - Vänsterpartiet arbetar för en jämlik skola med likvärdiga förutsättningar för alla elever genom åtgärder mot skolsegregation, offentlig kontroll över skolpengen och stopp för vinster i skolan.", color=ft.colors.WHITE),
                                    ft.Text("   - Miljöpartiet strävar efter en hållbar och inkluderande skola med satsningar på miljö- och utomhuspedagogik samt minskade klyftor genom resursförstärkningar till utsatta områden.", color=ft.colors.WHITE),
                                    ft.Text("   - Centerpartiet strävar efter individanpassad undervisning och mindre klassstorlekar med ökad autonomi för skolor och satsningar på digitalisering och entreprenörskap.", color=ft.colors.WHITE),
                                    ft.Text("   - Liberalerna fokuserar på att höja läraryrkets status och främja valfrihet för elever och föräldrar genom fler skolalternativ och kompetensbaserade lönesystem.", color=ft.colors.WHITE),
                                    ft.Text("   - Sverigedemokraterna fokuserar på att stärka den svenska skolan genom att betona trygghet, disciplin och nationellt fokus i undervisningen samt ökad kontroll över invandringens påverkan på skolan.", color=ft.colors.WHITE),
                                    ft.Text("   - Kristdemokraterna betonar trygghet och auktoritet i skolan genom stärkande av lärarnas roll och samarbete mellan skola, föräldrar och lokalsamhälle.", color=ft.colors.WHITE)
                                ]
                            )
                        )
                    ]
                )
            )

        if page.route == "/brottsbekämpning":
            page.views.append(
                ft.View(
                    "/brottsbekämpning",
                    [
                        ft.AppBar(title=ft.Text("Jämför Ståndpunkter - Brottsbekämpning"), bgcolor=MC),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            content = ft.Column(
                                spacing=15,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Text(" "),
                                    ft.Text(" "),
                                    ft.Text("   - Moderaterna förespråkar hårdare straff och restriktivare åtgärder för att bekämpa brottslighet", color=ft.colors.WHITE),
                                    ft.Text("   - Socialdemokraterna har en balanserad syn som värdesätter både förebyggande arbete och effektiva straffåtgärder för att minska brottsligheten", color=ft.colors.WHITE),
                                    ft.Text("   - Vänsterpartiet betonar förebyggande åtgärder och alternativa straffmetoder för att minska brottsligheten", color=ft.colors.WHITE),
                                    ft.Text("   - Miljöpartiet lägger fokus på att adressera sociala orsaker till brottslighet och förespråkar alternativa metoder för att minska den", color=ft.colors.WHITE),
                                    ft.Text("   - Centerpartiet betonar vikten av en balans mellan förebyggande åtgärder och straffåtgärder för att öka tryggheten i samhället", color=ft.colors.WHITE),
                                    ft.Text("   - Liberalerna söker en balans mellan straff och rehabilitering, med en betoning på individuell ansvarighet och förebyggande arbete för att minska brottslighet", color=ft.colors.WHITE),
                                    ft.Text("   - Sverigedemokraterna lutar mot en hårdare linje med krav på strängare straff och en restriktiv invandringspolitik som kopplas till brottslighet", color=ft.colors.WHITE),
                                    ft.Text("   - Kristdemokraterna fokuserar på att stärka brottsoffrens rättigheter och stödja hårdare straff för grova brott, samtidigt som de betonar vikten av förebyggande åtgärder och rehabilitering", color=ft.colors.WHITE)
                                ]
                            )
                        )
                    ]
                )
            )
        if page.route == "/stats":
            page.views.append(
                ft.View(
                    "/stats",
                    [
                        ft.AppBar(title=ft.Text("Genomförda vallöften"), bgcolor=MC),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35
                        )
                    ],
                )
            )
        page.update()

        if page.route == "/values":
            dv = ft.Dropdown(
                    options=[
                        ft.dropdown.Option("Moderaterna"),
                        ft.dropdown.Option("Socialdemokraterna"),
                        ft.dropdown.Option("Sverigedemokraterna"),
                        ft.dropdown.Option("Vänsterpartiet"),
                        ft.dropdown.Option("Liberalerna"),
                        ft.dropdown.Option("Kristdemokraterna"),
                        ft.dropdown.Option("Miljöpartiet"),
                        ft.dropdown.Option("Centerpartiet"),
                    ],
                    width=200,
                    on_change=lambda _:page.go("/" + dv.value.lower() )
            )
            page.views.append(
                ft.View(
                    "/values",
                    [
                        ft.AppBar(title=ft.Text("Sammanfattning Partiåsikter"), bgcolor=MC),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            content= ft.Stack(
                                controls=[
                                    ft.Text("\n "),  # newline added here
                                    ft.Text("\n "),  # additional newli
                                    ft.Text("         Välj parti", size=20, color=ft.colors.WHITE, italic=True),
                                    dv,
                                ]
                            )
                        )
                    ]

                )
            )
        page.update()

        if page.route == "/moderaterna":
            page.views.append(
                ft.View(
                    "/moderaterna",
                    [
                        ft.AppBar(title=ft.Text("Sammanfattning Partiåsikter - Moderaterna"), bgcolor=MC),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                             content = ft.Column(
                                spacing=10,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                                                        ft.Text(" "),
                                    ft.Text(" "),
                                    ft.Text("   Brott och Straff", size=15, color=TC),
                                    ft.Text("   - Till år 2026 ökar regeringen anslaget till polisen 10 miljarder kronor.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Moderaterna vill ha hårdare straff för grova brott för att minska kriminaliteten och öka samhällets trygghet.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Partiet vill förändra svensk rättspolitik för att bättre värna brottsoffrens rättigheter och öka respekten för dem.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Kommande åtgärder inkluderar översyn av ersättningssystemet för brottsoffer, straffskalor, kamerabevakningslagar och förebyggande tvångsåtgärder mot brottsnätverk.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Målet är att skapa ett tryggare samhälle där alla kan känna sig säkra och där rättssystemet fungerar effektivt och rättvist", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("  "),
                                    ft.Text("   Skola", size=15, color=TC),
                                    ft.Text("   - Återupprätta kunskapsfokus", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Stärka lärarrollen", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Öka trygghet och studiero i klassrummet", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Centralt rättade nationella prov och en starkare Skolinspektion ska säkerställa kvalitet och jämförbara resultat.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Stärkt lärarroll genom höjd status, praktiknära utbildningar och minskad administrativ börda.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text(" "),
                                    ft.Text("   Välfärd", size=15, color=TC),
                                    ft.Text("   - Prioriterar effektivitet och ansvar.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Balans mellan statlig hjälp och individuellt ansvar.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Strävar efter modernisering för att möta framtidens behov.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Äldreomsorgen behöver utvecklas för att möta det ökade vårdbehovet, med fokus på att ha tillräckligt med läkare och sjuksköterskor.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Förbättrade arbetsvillkor inom vård- och omsorgssektorn är nödvändiga för att öka personalkontinuiteten och kvaliteten i vården.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text(" "),
                                    ft.Text("   Försvar", size=15, color=TC),
                                    ft.Text("   - Slutföra den militära integrationen med Nato", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Prioriterar en stark och modern försvarsmakt.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Kriget i Ukraina definierar Sveriges utrikes- och säkerhetspolitik framöver", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Den moderatledda regeringen genomför den största upprustningen av totalförsvaret sedan 1950-talet.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Vill investera i försvarets för långsiktig försvarsförmåga.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER)
                                ]
                             )  
                        )
                    ]
                )
            )
        if page.route == "/socialdemokraterna":
            page.views.append(
                ft.View(
                    "/socialdemokraterna",
                    [
                        ft.AppBar(title=ft.Text("Sammanfattning Partiåsikter - Socialdemokraterna"), bgcolor=MC),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            content = ft.Column(
                                spacing=10,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Text(" "),
                                    ft.Text(" "),
                                    ft.Text("   Brott och Straff", size=15, color=TC),
                                    ft.Text("   - Öka antalet anställda hos polisen till 50 000, varav över 34 000 ska vara poliser, för att öka närvaron över hela landet.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Bekämpa gängkriminaliteten genom en nationell offensiv mot gängskjutningar och intensifierad samverkan mellan myndigheter.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Höja minimistraffet för våldtäkt, öppna fler våldtäktsmottagningar och skärpa behandlingskraven för dömda.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Öka tryggheten med fler kameror och ta bort tillståndskravet för kommunala kamerainsättningar.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Införa specialgrupper för att identifiera och stödja unga i riskzonen och införa vistelseförbud för ungdomar som är på väg in i kriminalitet.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Inrätta ungdomskriminalitetsnämnder för unga som begår allvarliga brott för att förebygga återfall och erbjuda stöd.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("  "),
                                    ft.Text("   Skola", size=15, color=TC),
                                    ft.Text("   - Satsa miljarder på 150 skolor med störst behov för att förbättra kunskapsresultaten, inklusive att anställa fler lärare och förbättra elevhälsan.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Införa ett rättvist skolval och omforma skolpengen för ökad likvärdighet.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Ge kommunerna vetorätt vid etablering av friskolor och förbjuda vinstuttag.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Förbjuda religiösa friskolor och fortsätta investera i skolan för att minska ojämlikheten.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Införa nolltolerans mot skolfrånvaro och satsa på skolsocionomer i utsatta områden.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Införa strängare straff för brott mot utbildningspersonal och garantera läxhjälp för elever i behov.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text(" "),
                                    ft.Text("   Välfärd", size=15, color=TC),
                                    ft.Text("   - Återta demokratisk kontroll över välfärden och avskaffa vinstjakten.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Förhindra utförsäljningar och skapa en jämlik vård.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Investera i en förbättrad välfärd genom att anställa fler vård- och skolpersonal för att minska köerna.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Ge vård efter behov, inte plånbok, för att korta vårdköerna och prioritera de mest behövande.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Införa fast omsorgskontakt i hemtjänsten och främja social samvaro samt idrott och friluftsliv för äldre.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Kräva öppenhet och transparens i friskolor och privata utförare inom vård och omsorg, på samma sätt som för offentliga aktörer.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text(" "),
                                    ft.Text("   Försvar", size=15, color=TC),
                                    ft.Text("   - Stärka Sveriges totalförsvarsförmåga genom att öka det militära försvarets anslag till 2 procent av BNP och förbättra den operativa förmågan.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Förstärka beredskapen för att möta nya och komplexa hot, både inom och utanför landets gränser.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Säkerställa tillgången på personal inom Försvarsmakten och göra det till en attraktiv arbetsgivare.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Integrera svenskt försvar inom ramen för Nato för ökad samverkan och säkerhet.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Skapa beredskapslager av livsmedel, läkemedel och drivmedel för att säkra resurser vid kriser.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Öka stödet till frivilliga försvarsorganisationer och uppmärksamma och stödja veteraner för deras tjänstgöring.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text(" "),
                                    ft.Text("   Klimat", size=15, color=TC),
                                    ft.Text("   - Sänka bilkostnader för glesbygdsinvånare och öka användningen av biodrivmedel.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Öka tillgängligheten av laddstolpar och underlätta användningen av elbilar.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Erbjuda ekonomiskt stöd för energieffektivisering i flerbostadshus.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Stärka industriklivet och klimatberedskapen genom ökade investeringar.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Reformera reseavdraget och erbjuda avgiftsfri kollektivtrafik för studenter.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("   - Förbättra järnvägsinfrastrukturen och effektivisera tillståndsprocesser för verksamheter.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER)
                                ]
                             )  
                        )
                    ]
                )
            )

        if page.route == "/local":
            dl = ft.Dropdown(
                    options=[
                        ft.dropdown.Option("Göteborg"),
                        ft.dropdown.Option("Arjeplog"),
                        ft.dropdown.Option("Hovfors"),
                        ft.dropdown.Option("Orsa"),
                        ft.dropdown.Option("Stockholm"),
                        ft.dropdown.Option("Kungälv"),
                    ],
                    width=200,
                    on_change=lambda _:page.go("/" + dl.value.lower() )
            )
            page.views.append(
                ft.View(
                    "/local",
                    [
                        ft.AppBar(title=ft.Text("Vad Händer Hos Dig?"), bgcolor=MC),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            content= ft.Stack(
                                controls=[
                                    ft.Text("\n "),  # newline added here
                                    ft.Text("\n "),  # additional newli
                                    ft.Text("         Välj kommun", size=20, color=ft.colors.WHITE, italic=True),
                                    dl,
                                ]
                            )
                        )
                    ]
                )
            )
        page.update()
        if page.route == "/göteborg":
            page.views.append(
                ft.View(
                    "/göteborg",
                    [
                        ft.AppBar(title=ft.Text("Detta händer i Göteborg"), bgcolor=MC),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35
                        )
                    ]
                )
            )
        if page.route == "/göteborg":
            page.views.append(
                ft.View(
                    "/göteborg",
                    [
                        ft.AppBar(title=ft.Text("Detta händer i Göteborg"), bgcolor=MC),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35
                        )
                    ]
                )
            )
        if page.route == "/arjeplog":
            page.views.append(
                ft.View(
                    "/arjeplog",
                    [
                        ft.AppBar(title=ft.Text("Detta händer i Arjeplog"), bgcolor=MC),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35
                        )
                    ]
                )
            )
        if page.route == "/hovfors":
            page.views.append(
                ft.View(
                    "/hovfors",
                    [
                        ft.AppBar(title=ft.Text("Detta händer i Hovfors"), bgcolor=MC),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35
                        )
                    ]
                )
            )

    
        if page.route == "/quest":
            page.views.append(
                ft.View(
                    "/quest",
                    [
                        ft.AppBar(title=ft.Text("Quiz"), bgcolor=MC),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35
                        )
                    ]
                )
            )
        page.update()

        if page.route == "/toplist":
            page.views.append(
                ft.View(
                    "/toplist",
                    [
                        ft.AppBar(title=ft.Text("Topplista"), bgcolor=MC),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35
                        )
                    ]
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)