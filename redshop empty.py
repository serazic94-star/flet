import flet as ft


def red_custom_appbar(title="중앙 텍스트"):
    right_icons = ft.Row(
        spacing=8,
        controls=[
            ft.Icon(ft.Icons.SEARCH, color=ft.Colors.WHITE),
            ft.Icon(ft.Icons.NOTIFICATIONS, color=ft.Colors.WHITE),
        ],
    )

    return ft.Container(
        height=60,
        bgcolor=ft.Colors.RED,
        padding=ft.padding.symmetric(horizontal=16),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(width=56),
                ft.Text(
                    title,
                    size=20,
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(
                    width=56,
                    content=right_icons,
                    alignment=ft.Alignment(1, 0),
                ),
            ],
        ),
    )


def nav_item(icon, label, on_click=None):
    return ft.Container(
        expand=True,
        height=70,
        on_click=on_click,
        alignment=ft.Alignment(0, 0),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
            controls=[
                ft.Icon(icon, color=ft.Colors.WHITE, size=24),
                ft.Text(
                    label,
                    color=ft.Colors.WHITE,
                    size=12,
                    weight=ft.FontWeight.W_500,
                ),
            ],
        ),
    )


def Red_custom_bottom_appbar(on_tab_change=None):
    items = [
        (ft.Icons.HOME, "Home"),
        (ft.Icons.EDIT_NOTE, "Log"),
        (ft.Icons.MENU_BOOK, "Contents"),
        (ft.Icons.PERSON, "MyPage"),
    ]

    return ft.BottomAppBar(
        bgcolor=ft.Colors.RED,
        shape=ft.CircularRectangleNotchShape(),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                nav_item(
                    icon,
                    label,
                    on_click=(lambda e, idx=i: on_tab_change(idx) if on_tab_change else None),
                )
                for i, (icon, label) in enumerate(items)
            ],
        ),
    )

def super_long_box2(controls=None):
    return ft.Container(
        width=350,
        height=100,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=10,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=controls if controls else [],  # ✅ 핵심
        ),
    )

def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.WHITE  # ✅ 흰 배경 유지
    page.appbar = None

    def change_tab(index):
        print("선택된 탭:", index)

    # ✅ Pagelet 유지 (하단바 + FAB 구조 때문)
    pagelet = ft.Pagelet(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        content=ft.Container(),  # ✅ 이거 추가
    )

    # ✅ FAB 유지
    pagelet.floating_action_button = ft.FloatingActionButton(
        content=ft.Image(
            src="bowlradius_red.png",
            width=40,
            height=40,
            fit=ft.BoxFit.CONTAIN,
        ),
        bgcolor=ft.Colors.WHITE,
        shape=ft.CircleBorder(),
        elevation=0,
        on_click=lambda e: print("가운데 버튼 클릭"),
    )

    pagelet.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    # ✅ 하단 네비바
    pagelet.bottom_appbar = Red_custom_bottom_appbar(
        on_tab_change=change_tab,
    )

    # ✅ 본문은 앱바만 남김
    pagelet.content = ft.Column(
        expand=True,
        spacing=0,
        controls=[
            red_custom_appbar("개밥개밥푸드"),
            ft.Container(
                margin=ft.margin.symmetric(vertical=10)
            ),
            ft.Container(ft.Text("똑똑 배송 시작하기"),
                alignment=ft.Alignment(0, 0), # ✅ 중앙 정렬
                ),  
            ft.Divider(),
            ft.Container(
                super_long_box2(
                    controls=[
                        ft.Row(
                            spacing=5,
                            controls=[
                                ft.Checkbox(),
                                ft.Text("있다"),
                            ],
                        )
                    ]
                ),
                alignment=ft.Alignment(0, 0),
            ),
            ft.Container(
                margin=ft.margin.symmetric(vertical=10)
            ),
            ft.Container(
                super_long_box2(
                    controls=[
                        ft.Row(
                            spacing=5,
                            controls=[
                                ft.Checkbox(),
                                ft.Text("없다"),
                            ],
                        )
                    ]
                ),
                alignment=ft.Alignment(0, 0),
            ),
        ],
    )

    page.add(pagelet)


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