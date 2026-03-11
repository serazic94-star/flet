import flet as ft

def main(page: ft.Page):
    page.title = "Mobile Style App"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.appbar = ft.AppBar(
        title=ft.Text("홈"),
        center_title=True,
        bgcolor=ft.Colors.BLUE_200
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="홈"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="검색"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="내정보"),
        ]
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD
    )

    page.add(
        ft.Column(
            controls=[
                ft.Card(
                    content=ft.Container(
                        padding=20,
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.FAVORITE, size=30),
                                ft.Text("좋아요 메뉴", size=18),
                            ]
                        )
                    )
                ),
                ft.Card(
                    content=ft.Container(
                        padding=20,
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.SETTINGS, size=30),
                                ft.Text("설정 메뉴", size=18),
                            ]
                        )
                    )
                ),
            ]
        )
    )

ft.app(main)