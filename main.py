import math
import flet as ft

def main(page: ft.Page):
    page.title = "PolitikPulsen"
    BG = "#1A5577"
    MC = "#60AEDA"
    TC = "#B5FFB3"
    ITC= "#FBEDD2"
    EC= "#D7DBFD"

    a5 = ft.Stack(
        [
            ft.CircleAvatar(
                foreground_image_url="https://cdn-icons-png.flaticon.com/128/2202/2202112.png"
            ),
            ft.Container(
                content=ft.CircleAvatar(bgcolor=ft.colors.GREEN, radius=5),
                alignment=ft.alignment.bottom_left,

            ),
        ],
        width=40,
        height=40,
    )

    img_soc= "https://bilder.riksdagen.se/publishedmedia/e9omiy7wkxkhts7ptwal/Symbol_Socialdemokraterna-_134px.png"
    img_mod= "https://upload.wikimedia.org/wikipedia/commons/8/85/M_v1.svg"
    img_svd= "https://bilder.riksdagen.se/publishedmedia/6gxtyz3j95i9xr0ejrbn/Sveriedemokraterna_132px.png"
    img_mp= "https://bilder.riksdagen.se/publishedmedia/3sgk8lpoqlu2mht11nov/MP_partilogga.png"
    img_v= "https://upload.wikimedia.org/wikipedia/commons/0/00/V%C3%A4nsterpartiet_logo.svg"
    img_L= "https://upload.wikimedia.org/wikipedia/commons/c/c7/L_v1.svg"
    img_C= "https://upload.wikimedia.org/wikipedia/commons/3/33/C_v1.svg"
    img_kd= "https://bilder.riksdagen.se/publishedmedia/bnz3yl48fswzmc8cd4m8/KD_partilogga.png"
    img_gbg= "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Göteborg_kommunvapen_-_Riksarkivet_Sverige.svg/1024px-Göteborg_kommunvapen_-_Riksarkivet_Sverige.svg.png"
    img_arj= "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Arjeplog_vapen.svg/248px-Arjeplog_vapen.svg.png"
    img_kings= "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Kungälv_vapen.svg/248px-Kungälv_vapen.svg.png"

    

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
                                a5,
                                ft.Text("Peter Karlsson", size=15,text_align=ft.TextAlign.LEFT, color=ft.colors.WHITE),
                                ft.Text(" "),
                                ft.Image(
                                    src=f"/prevote.png",
                                    width=300,
                                    fit=ft.ImageFit.CONTAIN
                                ),
                                ft.ElevatedButton("Åsiktsjämförelse",bgcolor=EC,icon="ARROW_FORWARD_IOS", on_click=lambda _: page.go("/compare")),
                                ft.ElevatedButton("Genomförda Vallöften",bgcolor=EC, icon="ARROW_FORWARD_IOS", on_click=lambda _: page.go("/stats")),
                                ft.ElevatedButton("Partiståndpunkter", bgcolor=EC, icon="ARROW_FORWARD_IOS", on_click=lambda _: page.go("/values")),
                                ft.ElevatedButton("Vad Händer Hos Dig?", bgcolor=EC, icon="ARROW_FORWARD_IOS", on_click=lambda _:page.go("/local")),
                                ft.ElevatedButton("Quiz", bgcolor=EC, icon="STAR_ROUNDED", on_click=lambda _:page.go("/quest")),
                                ft.ElevatedButton("Topplista", bgcolor=EC, icon="STAR_ROUNDED", on_click=lambda _:page.go("/toplist")),
                                ft.IconButton(icon="settings_rounded", tooltip="Inställningar", icon_color=ft.colors.WHITE)
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
                    border_radius=15,
                    bgcolor=EC,
                    filled=True,
                    border_color=EC,
                    color=ft.colors.BLUE_800,
                    label="Välj område",
                    on_change=lambda _:page.go("/" + dd.value.lower() )  
            )
            
            page.views.append(
                ft.View(
                    "/compare",
                    [
                        ft.AppBar(title=ft.Text("Jämför Ståndpunkter"), bgcolor=MC),
                        #ft.ElevatedButton("Go Home", bgcolor=EC, on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            content= ft.Column(
                                controls=[
                                    ft.Text("\n "), 
                                    ft.Text("\n "), 
                                    ft.Text(" "),
                                    ft.Container(
                                        content=dd,
                                        alignment=ft.alignment.center,
                                    ),
                                    ft.Container(
                                        content=ft.Image(
                                            src=f"/jamfar.png",
                                            width=350,
                                            #height=50,
                                            fit=ft.ImageFit.CONTAIN
                                        ),
                                        alignment=ft.alignment.center
                                    )
                                ],
                            ),
                            alignment=ft.alignment.top_center
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
                        #ft.ElevatedButton("Go Home", bgcolor=EC, on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            padding= ft.padding.only(top=50, left=20, right=20, bottom=20),
                            content = ft.Column(
                                spacing=15,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Text(" "),
                                    ft.Image(
                                        src=img_mod,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Moderaterna betonar höjda kunskapskrav och ökad lärarkompetens med en inriktning på kärnämnena samt valfrihet för elever och föräldrar genom fler skolalternativ.", color=ft.colors.WHITE),
                                    ft.Image(
                                        src=img_soc,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Socialdemokraterna fokuserar på att förbättra likvärdigheten i skolan genom resurstillskott till socioekonomiskt utsatta områden och stärkande av läraryrkets status.", color=ft.colors.WHITE),
                                    ft.Image(
                                        src=img_v,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Vänsterpartiet arbetar för en jämlik skola med likvärdiga förutsättningar för alla elever genom åtgärder mot skolsegregation, offentlig kontroll över skolpengen och stopp för vinster i skolan.", color=ft.colors.WHITE),
                                    ft.Image(
                                        src=img_mp,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Miljöpartiet strävar efter en hållbar och inkluderande skola med satsningar på miljö- och utomhuspedagogik samt minskade klyftor genom resursförstärkningar till utsatta områden.", color=ft.colors.WHITE),
                                    ft.Image(
                                        src=img_C,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Centerpartiet strävar efter individanpassad undervisning och mindre klassstorlekar med ökad autonomi för skolor och satsningar på digitalisering och entreprenörskap.", color=ft.colors.WHITE),
                                    ft.Image(
                                        src=img_L,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Liberalerna fokuserar på att höja läraryrkets status och främja valfrihet för elever och föräldrar genom fler skolalternativ och kompetensbaserade lönesystem.", color=ft.colors.WHITE),
                                    ft.Image(
                                        src=img_svd,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Sverigedemokraterna fokuserar på att stärka den svenska skolan genom att betona trygghet, disciplin och nationellt fokus i undervisningen samt ökad kontroll över invandringens påverkan på skolan.", color=ft.colors.WHITE),
                                    ft.Image(
                                        src=img_kd,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Kristdemokraterna betonar trygghet och auktoritet i skolan genom stärkande av lärarnas roll och samarbete mellan skola, föräldrar och lokalsamhälle.", color=ft.colors.WHITE)
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
                        #ft.ElevatedButton("Go Home", bgcolor=EC, on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            padding= ft.padding.only(top=50, left=20, right=20, bottom=20),
                            content = ft.Column(
                                spacing=15,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Text(" "),
                                    ft.Image(
                                        src=img_mod,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Moderaterna förespråkar hårdare straff och restriktivare åtgärder för att bekämpa brottslighet", color=ft.colors.WHITE),
                                    ft.Image(
                                        src=img_soc,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Socialdemokraterna har en balanserad syn som värdesätter både förebyggande arbete och effektiva straffåtgärder för att minska brottsligheten", color=ft.colors.WHITE),
                                    ft.Image(
                                        src=img_v,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Vänsterpartiet betonar förebyggande åtgärder och alternativa straffmetoder för att minska brottsligheten", color=ft.colors.WHITE),
                                    ft.Image(
                                        src=img_mp,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Miljöpartiet lägger fokus på att adressera sociala orsaker till brottslighet och förespråkar alternativa metoder för att minska den", color=ft.colors.WHITE),
                                    ft.Image(
                                        src=img_C,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Centerpartiet betonar vikten av en balans mellan förebyggande åtgärder och straffåtgärder för att öka tryggheten i samhället", color=ft.colors.WHITE),
                                    ft.Image(
                                        src=img_L,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Liberalerna söker en balans mellan straff och rehabilitering, med en betoning på individuell ansvarighet och förebyggande arbete för att minska brottslighet", color=ft.colors.WHITE),
                                    ft.Image(
                                        src=img_svd,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Sverigedemokraterna lutar mot en hårdare linje med krav på strängare straff och en restriktiv invandringspolitik som kopplas till brottslighet", color=ft.colors.WHITE),
                                    ft.Image(
                                        src=img_kd,
                                        width=50,
                                        height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Kristdemokraterna fokuserar på att stärka brottsoffrens rättigheter och stödja hårdare straff för grova brott, samtidigt som de betonar vikten av förebyggande åtgärder och rehabilitering", color=ft.colors.WHITE)
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
                        #ft.ElevatedButton("Go Home", bgcolor=EC, on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            padding= ft.padding.only(top=0, left=20, right=20, bottom=20),
                            content = ft.Column(
                                spacing=15,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Text(" "),
                                    ft.Image(
                                        src=f"/partistatistik.png",
                                        width=350,
                                        #height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    )
                                ]
                            )
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
                    border_radius=15,
                    bgcolor=EC,
                    filled=True,
                    border_color=EC,
                    color=ft.colors.BLUE_800,
                    label="Välj parti",
                    on_change=lambda _:page.go("/" + dv.value.lower() )
            )
            page.views.append(
                ft.View(
                    "/values",
                    [
                        ft.AppBar(title=ft.Text("Sammanfattning Partiåsikter"), bgcolor=MC),
                        #ft.ElevatedButton("Go Home", bgcolor=EC, on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            content= ft.Column(
                                controls=[
                                    ft.Text("\n "),  
                                    ft.Text("\n "),
                                    ft.Text(" "),  
                                    ft.Container(
                                        content=dv,
                                        alignment=ft.alignment.center,
                                    ),
                                    ft.Container(
                                        content=ft.Image(
                                            src=f"/sammanfattning.png",
                                            width=350,
                                            #height=50,
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        alignment=ft.alignment.center
                                    )
                                ],  
                            ),
                            alignment=ft.alignment.top_center
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
                        #ft.ElevatedButton("Go Home", bgcolor=EC, on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            padding= ft.padding.only(top=50, left=20, right=20, bottom=20),
                             content = ft.Column(
                                spacing=10,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Image(
                                        src=img_mod,
                                        width=100,
                                        height=100,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text(" "),
                                    ft.Text(" "),
                                    ft.Text("   Brott och Straff", size=15, color=TC, text_align=ft.TextAlign.CENTER),
                                    ft.Text("- Till år 2026 ökar regeringen anslaget till polisen 10 miljarder kronor.", color=ft.colors.WHITE),
                                    ft.Text("- Moderaterna vill ha hårdare straff för grova brott för att minska kriminaliteten och öka samhällets trygghet.", color=ft.colors.WHITE),
                                    ft.Text("- Partiet vill förändra svensk rättspolitik för att bättre värna brottsoffrens rättigheter och öka respekten för dem.", color=ft.colors.WHITE),
                                    ft.Text("- Kommande åtgärder inkluderar översyn av ersättningssystemet för brottsoffer, straffskalor, kamerabevakningslagar och förebyggande tvångsåtgärder mot brottsnätverk.", color=ft.colors.WHITE),
                                    ft.Text("- Målet är att skapa ett tryggare samhälle där alla kan känna sig säkra och där rättssystemet fungerar effektivt och rättvist", color=ft.colors.WHITE),
                                    ft.Text("  "),
                                    ft.Text("   Skola", size=15, color=TC, text_align=ft.TextAlign.CENTER),
                                    ft.Text("- Återupprätta kunskapsfokus", color=ft.colors.WHITE),
                                    ft.Text("- Stärka lärarrollen", color=ft.colors.WHITE),
                                    ft.Text("- Öka trygghet och studiero i klassrummet", color=ft.colors.WHITE),
                                    ft.Text("- Centralt rättade nationella prov och en starkare Skolinspektion ska säkerställa kvalitet och jämförbara resultat.", color=ft.colors.WHITE),
                                    ft.Text("- Stärkt lärarroll genom höjd status, praktiknära utbildningar och minskad administrativ börda.", color=ft.colors.WHITE),
                                    ft.Text(" "),
                                    ft.Text("   Välfärd", size=15, color=TC, text_align=ft.TextAlign.CENTER),
                                    ft.Text("- Prioriterar effektivitet och ansvar.", color=ft.colors.WHITE),
                                    ft.Text("- Balans mellan statlig hjälp och individuellt ansvar.", color=ft.colors.WHITE),
                                    ft.Text("- Strävar efter modernisering för att möta framtidens behov.", color=ft.colors.WHITE),
                                    ft.Text("- Äldreomsorgen behöver utvecklas för att möta det ökade vårdbehovet, med fokus på att ha tillräckligt med läkare och sjuksköterskor.", color=ft.colors.WHITE),
                                    ft.Text("- Förbättrade arbetsvillkor inom vård- och omsorgssektorn är nödvändiga för att öka personalkontinuiteten och kvaliteten i vården.", color=ft.colors.WHITE),
                                    ft.Text(" "),
                                    ft.Text("   Försvar", size=15, color=TC, text_align=ft.TextAlign.CENTER),
                                    ft.Text("- Slutföra den militära integrationen med Nato", color=ft.colors.WHITE),
                                    ft.Text("- Prioriterar en stark och modern försvarsmakt.", color=ft.colors.WHITE),
                                    ft.Text("- Kriget i Ukraina definierar Sveriges utrikes- och säkerhetspolitik framöver", color=ft.colors.WHITE),
                                    ft.Text("- Den moderatledda regeringen genomför den största upprustningen av totalförsvaret sedan 1950-talet.", color=ft.colors.WHITE),
                                    ft.Text("- Vill investera i försvarets för långsiktig försvarsförmåga.", color=ft.colors.WHITE)
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
                        #ft.ElevatedButton("Go Home", bgcolor=EC, on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            padding= ft.padding.only(top=50, left=20, right=20, bottom=20),
                            content = ft.Column(
                                spacing=10,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Image(
                                        src=img_soc,
                                        width=100,
                                        height=100,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text(" "),
                                    ft.Text(" "),
                                    ft.Text("   Brott och Straff", size=15, color=TC, text_align=ft.TextAlign.CENTER),
                                    ft.Text("- Öka antalet anställda hos polisen till 50 000, varav över 34 000 ska vara poliser, för att öka närvaron över hela landet.", color=ft.colors.WHITE),
                                    ft.Text("- Bekämpa gängkriminaliteten genom en nationell offensiv mot gängskjutningar och intensifierad samverkan mellan myndigheter.", color=ft.colors.WHITE),
                                    ft.Text("- Höja minimistraffet för våldtäkt, öppna fler våldtäktsmottagningar och skärpa behandlingskraven för dömda.", color=ft.colors.WHITE),
                                    ft.Text("- Öka tryggheten med fler kameror och ta bort tillståndskravet för kommunala kamerainsättningar.", color=ft.colors.WHITE),
                                    ft.Text("- Införa specialgrupper för att identifiera och stödja unga i riskzonen och införa vistelseförbud för ungdomar som är på väg in i kriminalitet.", color=ft.colors.WHITE),
                                    ft.Text("- Inrätta ungdomskriminalitetsnämnder för unga som begår allvarliga brott för att förebygga återfall och erbjuda stöd.", color=ft.colors.WHITE),
                                    ft.Text("  "),
                                    ft.Text("   Skola", size=15, color=TC, text_align=ft.TextAlign.CENTER),
                                    ft.Text("- Satsa miljarder på 150 skolor med störst behov för att förbättra kunskapsresultaten, inklusive att anställa fler lärare och förbättra elevhälsan.", color=ft.colors.WHITE),
                                    ft.Text("- Införa ett rättvist skolval och omforma skolpengen för ökad likvärdighet.", color=ft.colors.WHITE),
                                    ft.Text("- Ge kommunerna vetorätt vid etablering av friskolor och förbjuda vinstuttag.", color=ft.colors.WHITE),
                                    ft.Text("- Förbjuda religiösa friskolor och fortsätta investera i skolan för att minska ojämlikheten.", color=ft.colors.WHITE),
                                    ft.Text("- Införa nolltolerans mot skolfrånvaro och satsa på skolsocionomer i utsatta områden.", color=ft.colors.WHITE),
                                    ft.Text("- Införa strängare straff för brott mot utbildningspersonal och garantera läxhjälp för elever i behov.", color=ft.colors.WHITE),
                                    ft.Text(" "),
                                    ft.Text("   Välfärd", size=15, color=TC, text_align=ft.TextAlign.CENTER),
                                    ft.Text("- Återta demokratisk kontroll över välfärden och avskaffa vinstjakten.", color=ft.colors.WHITE),
                                    ft.Text("- Förhindra utförsäljningar och skapa en jämlik vård.", color=ft.colors.WHITE),
                                    ft.Text("- Investera i en förbättrad välfärd genom att anställa fler vård- och skolpersonal för att minska köerna.", color=ft.colors.WHITE),
                                    ft.Text("- Ge vård efter behov, inte plånbok, för att korta vårdköerna och prioritera de mest behövande.", color=ft.colors.WHITE),
                                    ft.Text("- Införa fast omsorgskontakt i hemtjänsten och främja social samvaro samt idrott och friluftsliv för äldre.", color=ft.colors.WHITE),
                                    ft.Text("- Kräva öppenhet och transparens i friskolor och privata utförare inom vård och omsorg, på samma sätt som för offentliga aktörer.", color=ft.colors.WHITE),
                                    ft.Text(" "),
                                    ft.Text("   Försvar", size=15, color=TC, text_align=ft.TextAlign.CENTER),
                                    ft.Text("- Stärka Sveriges totalförsvarsförmåga genom att öka det militära försvarets anslag till 2 procent av BNP och förbättra den operativa förmågan.", color=ft.colors.WHITE),
                                    ft.Text("- Förstärka beredskapen för att möta nya och komplexa hot, både inom och utanför landets gränser.", color=ft.colors.WHITE),
                                    ft.Text("- Säkerställa tillgången på personal inom Försvarsmakten och göra det till en attraktiv arbetsgivare.", color=ft.colors.WHITE),
                                    ft.Text("- Integrera svenskt försvar inom ramen för Nato för ökad samverkan och säkerhet.", color=ft.colors.WHITE),
                                    ft.Text("- Skapa beredskapslager av livsmedel, läkemedel och drivmedel för att säkra resurser vid kriser.", color=ft.colors.WHITE),
                                    ft.Text("- Öka stödet till frivilliga försvarsorganisationer och uppmärksamma och stödja veteraner för deras tjänstgöring.", color=ft.colors.WHITE),
                                    ft.Text(" "),
                                    ft.Text("   Klimat", size=15, color=TC, text_align=ft.TextAlign.CENTER),
                                    ft.Text("- Sänka bilkostnader för glesbygdsinvånare och öka användningen av biodrivmedel.", color=ft.colors.WHITE),
                                    ft.Text("- Öka tillgängligheten av laddstolpar och underlätta användningen av elbilar.", color=ft.colors.WHITE),
                                    ft.Text("- Erbjuda ekonomiskt stöd för energieffektivisering i flerbostadshus.", color=ft.colors.WHITE),
                                    ft.Text("- Stärka industriklivet och klimatberedskapen genom ökade investeringar.", color=ft.colors.WHITE),
                                    ft.Text("- Reformera reseavdraget och erbjuda avgiftsfri kollektivtrafik för studenter.", color=ft.colors.WHITE),
                                    ft.Text("- Förbättra järnvägsinfrastrukturen och effektivisera tillståndsprocesser för verksamheter.", color=ft.colors.WHITE)
                                ]
                             )  
                        )
                    ]
                )
            )
        if page.route == "/sverigedemokraterna":
            page.views.append(
                ft.View(
                    "/sverigedemokraterna",
                    [
                        ft.AppBar(title=ft.Text("Sammanfattning Partiåsikter - Sverigedemokraterna"), bgcolor=MC),
                        #ft.ElevatedButton("Go Home", bgcolor=EC, on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            padding= ft.padding.only(top=50, left=20, right=20, bottom=20),
                            content = ft.Column(
                                spacing=10,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Image(
                                        src=img_svd,
                                        width=100,
                                        height=100,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text(" "),
                                    ft.Text(" "),
                                    ft.Text("   Brott och Straff", size=15, color=TC, text_align=ft.TextAlign.CENTER),
                                    ft.Text("- Stödja ett starkt mellanstatligt samarbete inom EU för att bekämpa gränsöverskridande brottslighet och terrorism.", color=ft.colors.WHITE),
                                    ft.Text("- Utveckla effektiv registeranvändning för rättsväsendets myndigheter och förstärka EU:s gränspolis.", color=ft.colors.WHITE),
                                    ft.Text("- Koppla samman europeiska data- och registersystem för att underlätta informationsutbyte.", color=ft.colors.WHITE),
                                    ft.Text("- Försvåra och helst omöjliggöra asylbedrägerier genom ett utökat samarbete inom EU.", color=ft.colors.WHITE),
                                    ft.Text("  "),
                                    ft.Text("   Asyl och migration", size=15, color=TC, text_align=ft.TextAlign.CENTER),
                                    ft.Text("- Avskaffa missbruket av asylrätten genom att ansöka om asyl i första säkra land och återvända efter avslag.", color=ft.colors.WHITE),
                                    ft.Text("- Bevaka EU:s yttre gränser noggrant och ge medlemsländerna utökad rätt att bevaka sina egna gränser.", color=ft.colors.WHITE),
                                    ft.Text("- Betona att svensk migrationspolitik bör beslutas nationellt medan EU gemensamt övervakar den yttre gränsen.", color=ft.colors.WHITE),
                                    ft.Text("- Genom samarbete inom EU bekämpa asylbedrägerier och människosmuggling.", color=ft.colors.WHITE),
                                    ft.Text("- Genomföra asylutredningar utanför EU och utvisa uppenbart ogrundade asylansökningar efter snabbutredning.", color=ft.colors.WHITE),
                                    ft.Text(" "),
                                    ft.Text("   Välfärd", size=15, color=TC, text_align=ft.TextAlign.CENTER),
                                    ft.Text("- Sänka elskatten, bygga ny kärnkraft och motverka höga bränslepriser för att stärka ekonomin.", color=ft.colors.WHITE),
                                    ft.Text("- Stärka välfärden med schysta arbetsvillkor för personal inom vård och omsorg samt höjda pensioner.", color=ft.colors.WHITE),
                                    ft.Text("- Ha en realistisk klimatpolitik som säkerställer att svenskarna har råd att leva i både stad och land.", color=ft.colors.WHITE),
                                    ft.Text(" "),
                                    ft.Text("   Försvar", size=15, color=TC, text_align=ft.TextAlign.CENTER),
                                    ft.Text("- Behålla nationellt försvar och försvarssamarbeten som en nationell kompetens.", color=ft.colors.WHITE),
                                    ft.Text("- Betonar att den strategiska kompassens civila delar är positiva för civilförsvarssamarbeten, men att den militära delen riskerar att skapa en parallell struktur till Nato, vilket kan vara negativt för säkerheten.", color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text(" "),
                                    ft.Text("   Klimat", size=15, color=TC, text_align=ft.TextAlign.CENTER),
                                    ft.Text("- Att EU tar sin del av det globala ansvaret för att minska beroendet av fossila bränslen.", color=ft.colors.WHITE),
                                    ft.Text("- Framhålla att EU:s roll är främst att utveckla och exportera tekniskt kunnande för övergången till miljövänlig produktion globalt.", color=ft.colors.WHITE),
                                    ft.Text("- Genomföra utsläppsminskningar där de ger störst nytta av de investerade resurserna.", color=ft.colors.WHITE),
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
                        ft.dropdown.Option("Kungälv"),
                        ft.dropdown.Option("Arjeplog"),
                        ft.dropdown.Option("Orsa"),
                        ft.dropdown.Option("Hofors"),
                        ft.dropdown.Option("Stockholm"),
                    ],
                    width=200,
                    border_radius=15,
                    bgcolor=EC,
                    filled=True,
                    border_color=EC,
                    color=ft.colors.BLUE_800,
                    label="Välj kommun",
                    on_change=lambda _:page.go("/" + dl.value.lower() )
            )
            page.views.append(
                ft.View(
                    "/local",
                    [
                        ft.AppBar(title=ft.Text("Vad Händer Hos Dig?"), bgcolor=MC),
                        #ft.ElevatedButton("Go Home", bgcolor=EC, on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            content= ft.Column(
                                controls=[
                                    ft.Text("\n "),
                                    ft.Text("\n "),
                                    ft.Text(" "),
                                    ft.Container(
                                        content=dl,
                                        alignment=ft.alignment.center,
                                    ),
                                    ft.Container(
                                        content=ft.Image(
                                            src=f"/local.png",
                                            width=350,
                                            #height=50,
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        alignment=ft.alignment.center
                                    )
                                ],  
                            ),
                            alignment=ft.alignment.top_center
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
                        #ft.ElevatedButton("Go Home", bgcolor=EC, on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            padding= ft.padding.only(top=50, left=20, right=20, bottom=5),
                            content = ft.Column(
                                spacing=10,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Image(
                                        src=img_gbg,
                                        width=150,
                                        height=150,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Parkering i centrala Göteorg görs om till sommartorg:", color=ITC),
                                    ft.Markdown("[Se här](https://sverigesradio.se/artikel/kommunen-skrotar-p-platser-i-centrum-blir-sommartorg)", auto_follow_links=True),
                                    ft.Text("Skola ger upp vegetarisk bamba - tar tillbaka kött:", color=ITC),
                                    ft.Markdown("[Se här](https://www.gp.se/nyheter/goteborg/klara-teoretiska-gymnasium-tar-tillbaka-kott-i-bamba.8647097d-c505-4194-be63-e2107db401ca)", auto_follow_links=True),
                                    ft.Text("Träd i Eriksberg räddas när cykelbana breddas:", color=ITC),
                                    ft.Markdown("[Se här](https://goteborg.se/wps/portal/aktuelltarkivet/aktuellt/377ab02a-97e8-4d49-88ad-b7472a560486)", auto_follow_links=True),
                                    ft.Text("De får åka gratis kollektivt hela sommaren:", color=ITC),
                                    ft.Markdown("[Se här](https://goteborg.se/wps/portal/aktuelltarkivet/aktuellt/2f384fd8-3aad-446c-a8ce-92f2fb238444)", auto_follow_links=True),
                                    ft.Text("VÄSTLÄNKEN - ny trafikbro i Rosenlund:", color= ITC),
                                    ft.Markdown("[Se här](https://www.trafikverket.se/vara-projekt/projekt-i-vastra-gotalands-lan/vastlanken/nyheter-for-projekt-vastlanken/2024/mars/ny-trafikbro-i-rosenlund/)", auto_follow_links=True),
                                    ft.Text("VÄSTLÄNKEN - Pelarna börjar ta form på korsvägen:", color=ITC),
                                    ft.Markdown("[Se här](https://www.trafikverket.se/vara-projekt/projekt-i-vastra-gotalands-lan/vastlanken/nyheter-for-projekt-vastlanken/2024/april/pelarna-i-korsvagen/)", auto_follow_links=True)
                                ]
                            )    
                        )
                    ]
                )
            )

        if page.route == "/kungälv":
            page.views.append(
                ft.View(
                    "/kungälv",
                    [
                        ft.AppBar(title=ft.Text("Detta händer i Kungälv"), bgcolor=MC),
                        #ft.ElevatedButton("Go Home", bgcolor=EC, on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            padding= ft.padding.only(top=50, left=20, right=20, bottom=5),
                            content = ft.Column(
                                spacing=10,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Image(
                                        src=img_kings,
                                        width=150,
                                        height=150,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Snart får vi ett nytt utomhusgym i Älvparken:", color=ITC),
                                    ft.Markdown("[Se här](https://www.kungalv.se/kommun--politik/nyheter/nytt-utegym-pa-gang/)", auto_follow_links=True),
                                    ft.Text("Kommunen hyllar talangerna Adam Hilmersson och Isak Muminhodzic:", color=ITC),
                                    ft.Markdown("[Se här](https://www.kungalv.se/kommun--politik/nyheter/pristagare/)", auto_follow_links=True),
                                    ft.Text("Hur gick det för Kungälvs kommun 2023?", color=ITC),
                                    ft.Markdown("[Se här](https://www.kungalv.se/kommun--politik/nyheter/hur-gick-det-for-kungalvs-kommun-2023/)", auto_follow_links=True),
                                    ft.Text("Projekt för en hållbar livsstil i Kungälvs kommun:", color=ITC),
                                    ft.Markdown("[Se här](https://www.kungalv.se/kommun--politik/nyheter/projekt-for-en-hallbar-livsstil-i-kungalvs-kommun/)", auto_follow_links=True),
                                    ft.Text("Försvarsmakten övar på västkusten:", color=ITC),
                                    ft.Markdown("[Se här](https://www.kungalv.se/kommun--politik/nyheter/forsvarsmakten-ovar-pa-vastkusten-13-20-mars/)", auto_follow_links=True)

                                ]
                            )    
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
                        #ft.ElevatedButton("Go Home", bgcolor=EC, on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            padding= ft.padding.only(top=50, left=20, right=20, bottom=5),
                            content = ft.Column(
                                spacing=10,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Image(
                                        src=img_arj,
                                        width=150,
                                        height=150,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text("Hemtjänsten söker feriearbetare:", color=ITC),
                                    ft.Markdown("[Se här](https://www.arjeplog.se/nyheter/nyheter-startsida-2024/2024-05-07-hemtjansten-soker-feriearbetare)", auto_follow_links=True),
                                    ft.Text("Välkomna att träffa personal från samhällsbyggnadsenheten i Mellanström:", color=ITC),
                                    ft.Markdown("[Se här](https://www.arjeplog.se/nyheter/nyheter-startsida-2024/2024-05-06-valkomna-att-traffa-personal-fran-samhallsbyggnadsenheten-i-mellanstrom)", auto_follow_links=True),
                                    ft.Text("Skoterförbud inom Luokta Mavas samebys renskötselområde:", color=ITC),
                                    ft.Markdown("[Se här](https://www.arjeplog.se/nyheter/nyheter-startsida-2024/2024-05-02-skoterforbud-inom-luokta-mavas-samebys-renskotselomrade)", auto_follow_links=True),
                                    ft.Text("Eventuella vattenstörningar i Adolfsström:", color=ITC),
                                    ft.Markdown("[Se här](https://www.arjeplog.se/nyheter/nyheter-startsida-2024/2024-04-09-eventuella-vattenstorningar-i-adolfsstrom)", auto_follow_links=True)
                                ]
                            )    
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
                        #ft.ElevatedButton("Go Home", bgcolor=EC, on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            padding= ft.padding.only(top=0, left=20, right=20, bottom=20),
                            content = ft.Column(
                                spacing=15,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Text(" "),
                                    ft.Image(
                                        src=f"/quiz.png",
                                        width=350,
                                        #height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    )
                                ]
                            )
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
                        #ft.ElevatedButton("Go Home", bgcolor=EC, on_click=lambda _: page.go("/")),
                        ft.Container(
                            width=350,
                            height=700,
                            bgcolor=BG,
                            border_radius=35,
                            padding= ft.padding.only(top=0, left=20, right=20, bottom=20),
                            content = ft.Column(
                                spacing=15,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Text(" "),
                                    ft.Image(
                                        src=f"/topplista.png",
                                        width=350,
                                        #height=50,
                                        fit=ft.ImageFit.CONTAIN
                                    )
                                ]
                            )
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