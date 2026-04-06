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
        selected_index=2,  # 마이페이지 선택된 상태
    )

    profile_section = ft.Container(
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            controls=[
                ft.Container(
                    width=120,
                    height=120,
                    border_radius=60,
                    bgcolor=ft.Colors.WHITE,
                    alignment=ft.Alignment(0, 0),
                    shadow=ft.BoxShadow(
                        blur_radius=10,
                        spread_radius=1,
                        color=ft.Colors.BLACK12,
                    ),
                    content=ft.Icon(ft.Icons.PERSON, size=55),
                ),
            ],
        ),
        padding=ft.Padding.only(top=20, bottom=10),
    )

    summary_cards = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        controls=[
            ft.Container(
                width=160,
                height=100,
                bgcolor=ft.Colors.WHITE,
                border_radius=20,
                padding=15,
                shadow=ft.BoxShadow(
                    blur_radius=8,
                    spread_radius=1,
                    color=ft.Colors.BLACK12,
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("섭취량", size=24, weight=ft.FontWeight.BOLD),
                    ],
                ),
            ),
            ft.Container(
                width=160,
                height=100,
                bgcolor=ft.Colors.WHITE,
                border_radius=20,
                padding=15,
                shadow=ft.BoxShadow(
                    blur_radius=8,
                    spread_radius=1,
                    color=ft.Colors.BLACK12,
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("음수량", size=24, weight=ft.FontWeight.BOLD),
                    ],
                ),
            ),
        ],
    )

    def menu_box(icon, title):
        return ft.Container(
            width=95,
            height=95,
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
                spacing=8,
                controls=[
                    ft.Icon(icon, size=28),
                    ft.Text(title, size=11),
                ],
            ),
        )

    long_box = ft.Container(
        width=340,              # 가로 길이
        height=80,              # 세로 길이
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        padding=20,
        shadow=ft.BoxShadow(
            blur_radius=8,
            spread_radius=1,
            color=ft.Colors.BLACK12,
        ),
        alignment=ft.Alignment(0, 0),
        content=ft.Text(
            "기록 요약",
            size=20,
            weight=ft.FontWeight.BOLD,
        ),
    )

    menu_grid = ft.Column(
        spacing=14,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=14,
                controls=[
                    menu_box(ft.Icons.RESTAURANT, "밥주기"),
                    menu_box(ft.Icons.WATER, "물주기"),
                    menu_box(ft.Icons.MEDICAL_SERVICES, "약먹기"),
                ],
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=14,
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
        padding=ft.Padding.symmetric(horizontal=20, vertical=10),
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO, # 스크롤 기능 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                profile_section,
                summary_cards,
                ft.Container(height=10),
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