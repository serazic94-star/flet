import flet as ft

def micro_box(text, bgcolor=ft.Colors.GREY_200, text_color=ft.Colors.BLACK, icon=None):
    controls = []

    if icon:
        controls.append(ft.Icon(icon, size=14, color=text_color))

    controls.append(ft.Text(text, color=text_color, size=12))

    return ft.Container(
        padding=8,
        bgcolor=bgcolor,
        border_radius=10,
        content=ft.Row(
            spacing=6,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=controls,
        ),
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
                    width=56,   # 오른쪽 아이콘 자리와 비슷하게 맞춤
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


def input_box(label=None, hint_text=None):
    return ft.TextField(
        width=350,
        height=50,
        border_radius=10,
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.GREY_400,
        hint_text=hint_text,
        label=label,
    )


def mid_box(text, on_click=None):
    return ft.Container(
        width=96,
        height=40,
        bgcolor=ft.Colors.YELLOW_600,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        on_click=on_click,
        content=ft.Text(
            text,
            size=14,
            weight=ft.FontWeight.W_600,
            color=ft.Colors.BLACK,
        ),
    )


def long_box(text, bgcolor=ft.Colors.WHITE, text_color=ft.Colors.GREY_700, on_click=None):
    return ft.Container(
        width=350,
        height=50,
        border=ft.border.all(1, ft.Colors.GREY_400),
        border_radius=10,
        padding=10,
        bgcolor=bgcolor,
        on_click=on_click,
        alignment=ft.Alignment(0, 0),
        content=ft.Text(
            text,
            size=14,
            weight=ft.FontWeight.W_500,
            color=text_color,
            text_align=ft.TextAlign.CENTER,
        ),
    )


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.TRANSPARENT
    page.appbar = None

    def close_tip(e=None):
        harim_bottom_tip_sheet.open = False
        page.update()

    # BottomSheet 정의
    harim_bottom_tip_sheet = ft.BottomSheet(
        barrier_color=ft.Colors.TRANSPARENT,
        size_constraints=ft.BoxConstraints(
            max_height=700,
            min_height=430,
        ),
        content=ft.Container(
            padding=20,
            bgcolor=ft.Colors.WHITE,
            content=ft.Column(
                tight=True,
                scroll=ft.ScrollMode.AUTO,   # ✅ 스크롤 추가
                controls=[
                    ft.Text("밥주기", size=25, weight="bold"),
                    ft.Text("오늘 츄츄에게 딱 알맞은 급여량은", size=20, weight="bold"),
                    ft.Container(
                                    height=100,
                                    bgcolor=ft.Colors.WHITE,
                                    alignment=ft.Alignment(0, 0),
                                    content=invisible_middle_box("bowl.png"),
                                ),
                    long_box("가장 맛있는 시간 30일, 어덜트 치킨"),
                    long_box("40g"),
                    long_box("메모(선택)"),
                    ft.Container(
                        height=60,
                        bgcolor=ft.Colors.WHITE,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Row(   # ✅ 여기 핵심
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10,   # 👉 박스 사이 간격
                            controls=[
                                micro_box("2026.03.19", bgcolor=ft.Colors.WHITE, icon=ft.Icons.CALENDAR_MONTH),  # ✅ 여기만 화이트
                                micro_box("오전 07:30", bgcolor=ft.Colors.WHITE, icon=ft.Icons.ACCESS_TIME),   # 👉 옆에 붙일 거
                            ],
                        ),
                    ),
                    ft.Container(height=20),
                    # ✅ 여기부터 수정: Container(content=Row(...)) 제거하고
                    # ✅ Row를 controls 안에 직접 넣음
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            mid_box("저장"),
                        ],
                    ),
                ],
            ),
        ),
    )

    def show_inital_tip(e=None):
        harim_bottom_tip_sheet.open = True
        page.update()

    page.overlay.append(harim_bottom_tip_sheet)
    show_inital_tip()

    def change_tab(index):
        print("선택된 탭:", index)

    pagelet = ft.Pagelet(
        expand=True,
        content=ft.Container(),
        bgcolor=ft.Colors.YELLOW,
    )

    pagelet.floating_action_button = ft.FloatingActionButton(
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
    )

    pagelet.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    pagelet.bottom_appbar = custom_bottom_appbar(
        selected_index=0,
    )

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
                            content=ft.Text(name, size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
                        ),
                        ft.Container(
                            margin=ft.margin.only(left=60),
                            content=ft.Text(weight, size=11, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
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

    pagelet.content = ft.Container(
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
                                        ["급여량: 43g", "음수량: 100ml", "산책: 30분"]
                                    )
                                ]),
                                menu_grid
                            ],
                        ),
                    ),
                ],
            ),
        ),
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