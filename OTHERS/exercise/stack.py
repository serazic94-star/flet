import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.appbar = ft.AppBar(
        bgcolor=ft.Colors.GREY,
        title=ft.Row(
            controls=[ft.Text("로고"), ft.Icon(ft.Icons.PETS), ft.Text("설정")],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="HOME"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="LOG"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="MY PAGE"),
        ]
    )

    row_ui = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Stack(
                width=300,
                height=250,
                controls=[
                    ft.Container(
                        content=ft.Icon(ft.Icons.PETS, size=40),
                        width=120,
                        height=120,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=60,
                        alignment=ft.Alignment(0, 0),
                        left=10,
                        top=10,
                    ),
                    ft.Container(
                        content=ft.Icon(ft.Icons.PETS, size=40),
                        width=120,
                        height=120,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=60,
                        alignment=ft.Alignment(0, 0),
                        left=130,
                        top=10,
                    ),
                    ft.Container(
                        content=ft.Icon(ft.Icons.PETS),
                        width=60,
                        height=60,
                        bgcolor=ft.Colors.GREY,
                        alignment=ft.Alignment(0, 0),
                        left=130,
                        top=145,
                    ),
                    ft.Container(
                        content=ft.Icon(ft.Icons.PETS),
                        width=60,
                        height=60,
                        bgcolor=ft.Colors.GREY,
                        alignment=ft.Alignment(0, 0),
                        left=200,
                        top=145,
                    ),

                    # ⭐ 맨 위에 보일 노란 컨테이너
                    ft.Container(
                        content=ft.Icon(ft.Icons.PETS, size=40),
                        width=120,
                        height=120,
                        bgcolor=ft.Colors.YELLOW,
                        border_radius=60,
                        alignment=ft.Alignment(0, 0),
                        left=10,
                        top=10,
                    ),
                ],
            )
        ],
    )

    page.add(row_ui)


if __name__ == "__main__":
    import webbrowser
    import os

    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )