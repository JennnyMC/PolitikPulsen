import math
import flet as ft




def main(page: ft.Page):
    
    page.drawer = ft.NavigationDrawer(bgcolor="0xFFACE7F4",
            controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Hem",
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label="Åsiktsjämförelse", 
                selected_icon=ft.icons.ARROW_FORWARD_IOS,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label="Genomförda vallöften",
                selected_icon=ft.icons.ARROW_FORWARD_IOS,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label="Partiståndpunkter",
                selected_icon=ft.icons.ARROW_FORWARD_IOS,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label="Vad händer hos dig?",
                selected_icon=ft.icons.ARROW_FORWARD_IOS,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.STAR_ROUNDED),
                label="Quiz",
                selected_icon=ft.icons.STAR,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.STAR_ROUNDED),
                label="Topplista",
                selected_icon=ft.icons.STAR,
            )
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
                

                ],
                
            )
        )
    )

ft.app(target=main)