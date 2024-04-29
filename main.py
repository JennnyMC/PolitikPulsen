import math
import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"

   
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