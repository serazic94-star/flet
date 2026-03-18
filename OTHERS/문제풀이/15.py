import flet as ft

def main(page: ft.Page):

    text = ft.Text("홈 화면")

    page.appbar = ft.AppBar(
        title=ft.Text("홈"),
        bgcolor=ft.Colors.BLUE
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="홈"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="검색"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="프로필"),
        ]
    )

    page.add(text)

ft.app(main)