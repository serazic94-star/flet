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
                ft.Text("민서우", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("반려동물과 함께하는 마이페이지", size=12, color=ft.Colors.GREY_700),
            ],
        ),
        padding=ft.padding.only(top=20, bottom=10),
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
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Text("내 반려동물", size=13, color=ft.Colors.GREY_700),
                        ft.Text("2마리", size=24, weight=ft.FontWeight.BOLD),
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
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Text("구독 상태", size=13, color=ft.Colors.GREY_700),
                        ft.Text("이용 중", size=24, weight=ft.FontWeight.BOLD),
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

    menu_grid = ft.Column(
        spacing=14,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=14,
                controls=[
                    menu_box(ft.Icons.PETS, "반려동물"),
                    menu_box(ft.Icons.RECEIPT_LONG, "결제내역"),
                    menu_box(ft.Icons.FAVORITE, "찜 목록"),
                ],
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=14,
                controls=[
                    menu_box(ft.Icons.SETTINGS, "설정"),
                    menu_box(ft.Icons.NOTIFICATIONS, "알림"),
                    menu_box(ft.Icons.HELP, "고객센터"),
                ],
            ),
        ],
    )

    body = ft.Container(
        expand=True,
        padding=ft.padding.symmetric(horizontal=20, vertical=10),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                profile_section,
                summary_cards,
                ft.Container(height=10),
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