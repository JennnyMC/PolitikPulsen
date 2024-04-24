import math
import flet as ft




def main(page: ft.Page):

    page.drawer = ft.NavigationDrawer(
            controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                label="Item 2",
                selected_icon=ft.icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                label="Item 3",
                selected_icon=ft.icons.PHONE,
            ),
        ],
    )

    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    page.add(ft.ElevatedButton("Show drawer", on_click=show_drawer))

    page.add(
        ft.Container(
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.Alignment(0.8, 1),
                colors=[
                    "0xFF335D74",
                    "0xFF3E728E",
                    "0xFF60AEDA",
                    "0xFF235774",
                ],
                tile_mode=ft.GradientTileMode.MIRROR,
                rotation=math.pi / 3,
            ),
            width=393,
            height=652,
            border_radius=5,
            content=ft.Stack(
                controls=[
                

                ]
            )
        )
    )

ft.app(target=main)