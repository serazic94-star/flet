import flet as ft

def main(page: ft.Page):

    page.title = "Mobile UI"
    page.theme_mode = ft.ThemeMode.LIGHT

    # 상단 앱바
    page.appbar = ft.AppBar(
        title=ft.Text("홈"),
        center_title=True,
        bgcolor=ft.Colors.BLUE_200
    )

    # 하단 네비게이션 바
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="홈"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="검색"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="프로필"),
        ]
    )

    # 플로팅 버튼
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD
    )

    # 본문 카드 메뉴
    page.add(
        ft.Column(
            controls=[

                ft.Card(
                    content=ft.Container(
                        padding=20,
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.FAVORITE, size=30),
                                ft.Text("좋아요 메뉴", size=18)
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
                                ft.Text("설정 메뉴", size=18)
                            ]
                        )
                    )
                ),

                ft.Card(
                    content=ft.Container(
                        padding=20,
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.PERSON, size=30),
                                ft.Text("프로필 메뉴", size=18)
                            ]
                        )
                    )
                ),

            ]
        )
    )

ft.app(main)