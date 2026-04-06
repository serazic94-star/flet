import asyncio
import flet as ft


def custom_appbar(title="중앙 텍스트"):
    right_icons = ft.Row(
        spacing=8,
        controls=[
            ft.Icon(ft.Icons.SEARCH, color=ft.Colors.BLACK),
            ft.Icon(ft.Icons.NOTIFICATIONS, color=ft.Colors.BLACK),
        ],
    )

    return ft.Container(
        height=60,
        padding=ft.padding.symmetric(horizontal=16),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(width=56),  # 왼쪽 빈자리
                ft.Text(
                    title,
                    size=20,
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.BLACK,
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


def nav_item(icon, label, selected=False, on_click=None):
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
                ft.Icon(
                    icon,
                    color=ft.Colors.BLACK,
                    size=24,
                ),
                ft.Text(
                    label,
                    color=ft.Colors.BLACK,
                    size=12,
                    weight=ft.FontWeight.W_500,
                ),
            ],
        ),
    )


def custom_bottom_appbar(selected_index=0, on_tab_change=None):
    items = [
        (ft.Icons.HOME, "Home"),
        (ft.Icons.EDIT_NOTE, "Log"),
        (ft.Icons.MENU_BOOK, "Contents"),
        (ft.Icons.PERSON, "MyPage"),
    ]

    return ft.BottomAppBar(
        bgcolor=ft.Colors.YELLOW,
        shape=ft.CircularRectangleNotchShape(),
        content=ft.Row(
            spacing=8,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                nav_item(
                    icon,
                    label,
                    selected=(i == selected_index),
                    on_click=(lambda e, idx=i: on_tab_change(idx) if on_tab_change else None),
                )
                for i, (icon, label) in enumerate(items)
            ],
        ),
    )


def home_view(page: ft.Page):
    def change_tab(index):
        if index == 0:
            asyncio.create_task(page.push_route("/"))
        elif index == 1:
            asyncio.create_task(page.push_route("/log"))
        elif index == 2:
            asyncio.create_task(page.push_route("/contents"))
        elif index == 3:
            asyncio.create_task(page.push_route("/mypage"))

    def profile_card(image_src, name, weight):
        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            controls=[
                ft.Container(
                    width=100,
                    height=100,
                    border_radius=50,
                    alignment=ft.Alignment(0, 0),
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                    content=ft.Image(
                        src=image_src,
                        fit=ft.BoxFit.COVER,
                        width=100,
                        height=100,
                    ),
                ),
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        ft.Container(
                            margin=ft.margin.only(left=60),
                            content=ft.Text(
                                name,
                                size=14,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK,
                            ),
                        ),
                        ft.Container(
                            margin=ft.margin.only(left=60),
                            content=ft.Text(
                                weight,
                                size=11,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK,
                            ),
                        ),
                    ],
                ),
            ],
        )

    def menu_box(icon, title):
        return ft.Container(
            width=95,
            height=95,
            bgcolor=ft.Colors.YELLOW_600,
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
                    ft.Icon(icon, size=28, color=ft.Colors.BLACK),
                    ft.Text(title, size=11, color=ft.Colors.BLACK),
                ],
            ),
        )

    def super_long_box(controls=None):
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
                controls=controls or [],
            ),
        )

    def mini_box(text):
        return ft.Container(
            width=70,
            height=60,
            bgcolor=ft.Colors.YELLOW,
            border_radius=10,
            alignment=ft.Alignment(0, 0),
            content=ft.Text(
                text,
                size=18,
                weight=ft.FontWeight.W_700,
                color=ft.Colors.BLACK,
            ),
        )

    def micro_box(text):
        return ft.Container(
            padding=ft.padding.symmetric(horizontal=8, vertical=4),
            bgcolor=ft.Colors.GREY_200,
            border_radius=6,
            content=ft.Text(
                text,
                size=10,
                color=ft.Colors.BLACK,
            ),
        )

    def record_card(date_text, title_text, info_list):
        return ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            controls=[
                mini_box(date_text),
                ft.Column(
                    spacing=6,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Row(
                            spacing=6,
                            controls=[
                                ft.Text("🔥"),
                                ft.Text(
                                    title_text,
                                    size=16,
                                    weight=ft.FontWeight.W_600,
                                    color=ft.Colors.BLACK,
                                ),
                            ],
                        ),
                        ft.Row(
                            spacing=6,
                            controls=[micro_box(info) for info in info_list],
                        ),
                    ],
                ),
            ],
        )

    def invisible_middle_box(image_src):
        return ft.Container(
            width=200,
            height=200,
            bgcolor=ft.Colors.TRANSPARENT,
            border=None,
            border_radius=20,
            alignment=ft.Alignment(0, 0),
            content=ft.Image(
                src=image_src,
                fit=ft.BoxFit.COVER,
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

    pagelet = ft.Pagelet(
        expand=True,
        bgcolor=ft.Colors.YELLOW,
        floating_action_button=ft.FloatingActionButton(
            content=ft.Container(
                width=60,
                height=60,
                alignment=ft.Alignment(0, 0),
                content=ft.Image(
                    src="bowlradius.png",
                    fit=ft.BoxFit.CONTAIN,
                ),
            ),
            bgcolor=ft.Colors.WHITE,
            shape=ft.CircleBorder(),
            elevation=0,
            on_click=lambda e: print("가운데 버튼 클릭"),
        ),
        floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
        bottom_appbar=custom_bottom_appbar(
            selected_index=0,
            on_tab_change=change_tab,
        ),
        content=ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(0, 1),
                end=ft.Alignment(0, -1),
                colors=[
                    ft.Colors.WHITE,
                    ft.Colors.WHITE,
                    ft.Colors.YELLOW,
                ],
            ),
            content=ft.SafeArea(
                expand=True,
                content=ft.Column(
                    expand=True,
                    spacing=0,
                    controls=[
                        custom_appbar("Thur, 10 Oct"),
                        ft.Container(
                            expand=True,
                            padding=20,
                            content=ft.Column(
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    profile_card("dog.jpeg", "츄츄(2021.05.25)", "7.3kg"),
                                    ft.Container(
                                        height=100,
                                        bgcolor=ft.Colors.WHITE,
                                        alignment=ft.Alignment(0, 0),
                                        content=invisible_middle_box("surplus.png"),
                                    ),
                                    super_long_box([
                                        record_card(
                                            "3/19",
                                            "오늘의 기록",
                                            ["급여량: 43g", "음수량: 100ml", "산책: 30분"],
                                        )
                                    ]),
                                    menu_grid,
                                ],
                            ),
                        ),
                    ],
                ),
            ),
        ),
    )

    return ft.View(
        route="/",
        padding=0,
        bgcolor=ft.Colors.TRANSPARENT,
        controls=[pagelet],
    )