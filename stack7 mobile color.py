import flet as ft


def main(page: ft.Page):
    page.title = "My Page"
    page.bgcolor = ft.Colors.GREY_100

    page.appbar = ft.AppBar(
        bgcolor=ft.Colors.GREY,
        title=ft.Row(
            controls=[
                ft.Text("로고"),
                ft.Icon(ft.Icons.PETS),
                ft.Text("설정"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="HOME"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="LOG"),
            ft.NavigationBarDestination(icon=ft.Icons.STAR, label="SHOP"),
            ft.NavigationBarDestination(icon=ft.Icons.FAVORITE, label="AI"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="MY PAGE"),
        ],
        selected_index=2,
    )

    profile_section = ft.Container(
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6,
            controls=[
                ft.Container(
                    width=100,
                    height=100,
                    border_radius=50,
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                    bgcolor=ft.Colors.WHITE,
                    content=ft.Image(
                        src="dog.jpeg",
                        width=100,
                        height=100,
                        fit="cover",
                    ),
                )
            ],
        ),
        padding=ft.Padding.only(top=12, bottom=4),
    )

    summary_cards = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=12,
        controls=[
            ft.Container(
                width=150,
                height=90,
                bgcolor=ft.Colors.WHITE,
                border_radius=20,
                padding=12,
                shadow=ft.BoxShadow(
                    blur_radius=8,
                    spread_radius=1,
                    color=ft.Colors.BLACK12,
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("섭취량", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ],
                ),
            ),
            ft.Container(
                width=150,
                height=90,
                bgcolor=ft.Colors.WHITE,
                border_radius=20,
                padding=12,
                shadow=ft.BoxShadow(
                    blur_radius=8,
                    spread_radius=1,
                    color=ft.Colors.BLACK12,
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("음수량", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ],
                ),
            ),
        ],
    )

    long_box = ft.Container(
        width=320,
        height=68,
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        padding=12,
        shadow=ft.BoxShadow(
            blur_radius=8,
            spread_radius=1,
            color=ft.Colors.BLACK12,
        ),
        alignment=ft.Alignment(0, 0),
        content=ft.Text(
            "기록 요약",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLACK
        ),
    )

    def menu_box(icon, title):
        return ft.Container(
            width=86,
            height=86,
            bgcolor=ft.Colors.WHITE,
            border_radius=16,
            alignment=ft.Alignment(0, 0),
            shadow=ft.BoxShadow(
                blur_radius=8,
                spread_radius=1,
                color=ft.Colors.BLACK12,
            ),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5,
                controls=[
                    ft.Icon(icon, size=24, color=ft.Colors.BLACK),
                    ft.Text(title, size=10, color=ft.Colors.BLACK),
                ],
            ),
        )

    menu_grid = ft.Column(
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    menu_box(ft.Icons.RESTAURANT, "밥주기"),
                    menu_box(ft.Icons.WATER, "물주기"),
                    menu_box(ft.Icons.MEDICAL_SERVICES, "약먹기"),
                ],
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    menu_box(ft.Icons.PETS, "대소변기록"),
                    menu_box(ft.Icons.MONITOR_WEIGHT, "체중기록"),
                    menu_box(ft.Icons.EDIT, "관찰기록"),
                ],
            ),
        ],
    )

    body = ft.Container(
        expand=True,
        padding=ft.Padding.symmetric(horizontal=16, vertical=8),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=14,
            controls=[
                profile_section,
                summary_cards,
                long_box,
                menu_grid,
            ],
        ),
    )

    page.add(body)


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
