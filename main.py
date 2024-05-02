import math
import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"
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
                    ft.AppBar(title=ft.Text("Politik Pulsen"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.ElevatedButton("Åsiktsjämförelse", on_click=lambda _: page.go("/compare")),
                                ft.ElevatedButton("Genomförda Vallöften", on_click=lambda _: page.go("/stats")),
                                ft.ElevatedButton("Partiståndpunkter", on_click=lambda _: page.go("/values")),
                                ft.ElevatedButton("Vad Händer Hos Dig?", on_click=lambda _:page.go("/local")),
                                ft.ElevatedButton("Quiz", on_click=lambda _:page.go("/quest")),
                                ft.ElevatedButton("Topplista", on_click=lambda _:page.go("/toplist"))
                            ]
                        ),
                        bgcolor = ft.colors.BLUE_200,
                        border_radius= 5
                    )
                ],
            )
        )
        if page.route == "/compare":
            page.views.append(
                ft.View(
                    "/compare",
                    [
                        ft.AppBar(title=ft.Text("Jämför Ståndpunkter"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()
        if page.route == "/stats":
            page.views.append(
                ft.View(
                    "/stats",
                    [
                        ft.AppBar(title=ft.Text("Genomförda vallöften"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

        if page.route == "/values":
            page.views.append(
                ft.View(
                    "/values",
                    [
                        ft.AppBar(title=ft.Text("Partiståndpunkter"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.Text(
                            "Sammanfattning Partiåsikter",
                            size=50,
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.BLUE_400,
                            weight=ft.FontWeight.NORMAL,
                            ),
                        ft.Divider(),
                        ft.ElevatedButton("Välj Område"),
                        ft.Divider(),
                        ft.Text(
                            "Välj Parti:",
                            size=30,
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.BLUE_400,
                            weight=ft.FontWeight.NORMAL,
                            ),
                        add_images_to_values_view()
                    ]

                )
            )
        page.update()

        if page.route == "/local":
            page.views.append(
                ft.View(
                    "/local",
                    [
                        ft.AppBar(title=ft.Text("Vad Händer Hos Dig?"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ]
                )
            )
        page.update()
    
        if page.route == "/quest":
            page.views.append(
                ft.View(
                    "/quest",
                    [
                        ft.AppBar(title=ft.Text("Quiz"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ]
                )
            )
        page.update()

        if page.route == "/toplist":
            page.views.append(
                ft.View(
                    "/toplist",
                    [
                        ft.AppBar(title=ft.Text("Topplista"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
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