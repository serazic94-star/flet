import flet as ft


def main(page: ft.Page):
    page.title = "My Page"
    page.bgcolor = ft.Colors.GREY_100
    page.padding = 0  # 페이지 바깥 기본 여백 제거

    # ---------------------------
    # 상태(state) 변수
    # ---------------------------
    # 처음에는 아무것도 선택되지 않게 None으로 변경
    selected_summary = None
    selected_menu = None
    selected_long_box = False

    # ---------------------------
    # 상단 앱바
    # ---------------------------
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

    # ---------------------------
    # 하단 네비게이션 바
    # ---------------------------
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="HOME"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="LOG"),
            ft.NavigationBarDestination(icon=ft.Icons.STAR, label="SHOP"),
            ft.NavigationBarDestination(icon=ft.Icons.FAVORITE, label="AI"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="MY PAGE"),
        ],
        selected_index=4,
    )

    # ---------------------------
    # 프로필 영역
    # ---------------------------
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
                        fit=ft.BoxFit.COVER,
                    ),
                )
            ],
        ),
        padding=ft.Padding.only(top=12, bottom=4),
    )

    # ---------------------------
    # 스낵바 메시지 함수
    # ---------------------------
    def show_message(text):
        page.snack_bar = ft.SnackBar(ft.Text(text))
        page.snack_bar.open = True
        page.update()

    # ---------------------------
    # 툴팁 생성 함수
    # ---------------------------
    def create_tooltip(title):
        return ft.Tooltip(
            message=title,
            bgcolor=ft.Colors.BLACK,
            text_style=ft.TextStyle(
                color=ft.Colors.WHITE,
                size=12,
            ),
            wait_duration=200,
        )

    # ---------------------------
    # 공통 인터랙티브 박스 생성 함수
    # ---------------------------
    def make_interactive_box(
        title,
        width,
        height,
        content,
        is_selected,
        click_handler,
        border_radius=20,
        padding=12,
        normal_bg=ft.Colors.WHITE,
        selected_bg=ft.Colors.WHITE,   # 파란 배경 제거
        hover_bg=ft.Colors.WHITE,      # hover 시에도 파란색 제거
    ):
        box = ft.Container(
            width=width,
            height=height,
            border_radius=border_radius,
            padding=padding,
            alignment=ft.Alignment(0, 0),
            bgcolor=selected_bg if is_selected else normal_bg,
            tooltip=create_tooltip(title),
            ink=True,
            on_click=click_handler,
            animate=ft.Animation(140, ft.AnimationCurve.EASE_OUT),
            animate_scale=ft.Animation(140, ft.AnimationCurve.EASE_OUT),
            shadow=ft.BoxShadow(
                blur_radius=12 if is_selected else 8,
                spread_radius=1,
                color=ft.Colors.BLACK26 if is_selected else ft.Colors.BLACK12,
            ),
            content=content,
        )

        def handle_hover(e):
            hovering = e.data == "true"

            if hovering:
                box.scale = 1.03
                box.bgcolor = selected_bg if is_selected else hover_bg
                box.shadow = ft.BoxShadow(
                    blur_radius=16,
                    spread_radius=1,
                    color=ft.Colors.BLACK26,
                )
            else:
                box.scale = 1.0
                box.bgcolor = selected_bg if is_selected else normal_bg
                box.shadow = ft.BoxShadow(
                    blur_radius=12 if is_selected else 8,
                    spread_radius=1,
                    color=ft.Colors.BLACK26 if is_selected else ft.Colors.BLACK12,
                )

            box.update()

        box.on_hover = handle_hover
        return box

    # ---------------------------
    # 선택 처리 함수들
    # ---------------------------
    def select_summary(index, title):
        nonlocal selected_summary
        selected_summary = index
        refresh_ui()
        show_message(f"{title} 선택됨")

    def select_menu(title):
        nonlocal selected_menu
        selected_menu = title
        refresh_ui()
        show_message(f"{title} 선택됨")

    def select_long_box():
        nonlocal selected_long_box
        selected_long_box = not selected_long_box
        refresh_ui()
        show_message("기록 요약 선택됨")

    # ---------------------------
    # 요약 카드 생성 함수
    # ---------------------------
    def summary_card(title, index):
        is_selected = selected_summary == index

        return make_interactive_box(
            title=title,
            width=150,
            height=90,
            is_selected=is_selected,
            click_handler=lambda e, i=index, t=title: select_summary(i, t),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        title,
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK,   # 파란 글씨 제거
                    ),
                ],
            ),
        )

    # ---------------------------
    # 메뉴 박스 생성 함수
    # ---------------------------
    def menu_box(icon, title):
        is_selected = selected_menu == title

        return make_interactive_box(
            title=title,
            width=96,  # 대소변기록 5글자 
            height=96, # 박스 키우기
            border_radius=16,
            padding=10,
            is_selected=is_selected,
            click_handler=lambda e, t=title: select_menu(t),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5,
                controls=[
                    ft.Icon(
                        icon,
                        size=24,
                        color=ft.Colors.BLACK,   # 파란 아이콘 제거
                    ),
                    ft.Text(
                        title,
                        size=10,
                        weight=ft.FontWeight.BOLD if is_selected else ft.FontWeight.NORMAL,
                        color=ft.Colors.BLACK,   # 파란 글씨 제거
                    ),
                ],
            ),
        )

    # ---------------------------
    # 긴 박스(기록 요약) 생성 함수
    # ---------------------------
    def long_box_button():
        is_selected = selected_long_box

        return make_interactive_box(
            title="기록 요약",
            width=320,
            height=78, # 박스 공간 확보
            is_selected=is_selected,
            click_handler=lambda e: select_long_box(),
            content=ft.Text(
                "기록 요약",
                size=18,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK,   # 파란 글씨 제거
            ),
        )

    # ---------------------------
    # 비어 있는 UI 틀 먼저 생성
    # ---------------------------
    summary_cards = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=12,
        controls=[],
    )

    menu_grid = ft.Column(
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[],
    )

    long_box_holder = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[],
    )

    # ---------------------------
    # UI 다시 그리는 함수
    # ---------------------------
    def refresh_ui():
        summary_cards.controls = [
            summary_card("섭취량", 0),
            summary_card("음수량", 1),
        ]

        long_box_holder.controls = [
            long_box_button()
        ]

        menu_grid.controls = [
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
        ]

        page.update()

    # ---------------------------
    # 본문(body)
    # ---------------------------
    body = ft.Container(
        expand=True,
        padding=ft.Padding.symmetric(horizontal=16, vertical=8),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=14,
            controls=[
                profile_section,
                summary_cards,
                long_box_holder,
                menu_grid,
            ],
        ),
    )

    page.add(body)
    refresh_ui()


if __name__ == "__main__":
    import webbrowser
    import os

    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.app(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )