import math
import flet as ft

def main(page: ft.Page):
    page.title = "PolitikPulsen"
    BG = "#1A5577"
    MC = "#60AEDA"

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
                        ft.dropdown.Option("Brott&Straff"),
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
                        ft.AppBar(title=ft.Text("Jämför Ståndpunkter"), bgcolor=MC),
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
                        ft.AppBar(title=ft.Text("Partiståndpunkter"), bgcolor=MC),
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
                        ft.AppBar(title=ft.Text("Partiståndpunkter - Moderaterna"), bgcolor=MC),
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