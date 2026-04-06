import flet as ft


def main(page: ft.Page):
    page.title = "My Page"
    page.bgcolor = ft.Colors.GREY_100
    page.padding = 0  # 페이지 바깥 기본 여백 제거

    # ---------------------------
    # 상태(state) 변수
    # ---------------------------
    # selected_summary:
    #   요약 카드 2개 중 현재 선택된 카드의 index를 저장
    #   0이면 "섭취량", 1이면 "음수량"
    selected_summary = 0

    # selected_menu:
    #   현재 선택된 메뉴 박스의 제목을 저장
    #   예: "밥주기", "물주기"
    selected_menu = None

    # selected_long_box:
    #   "기록 요약" 박스의 선택 여부를 저장
    #   True / False 로 토글됨
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
        selected_index=3,
        # 현재 선택된 탭 index
        # 0: HOME, 1: LOG, 2: SHOP, 3: AI, 4: MY PAGE
        # 지금은 2라서 사실상 SHOP이 선택된 상태
        # 만약 "MY PAGE"를 선택 상태로 보이게 하려면 4로 바꿔야 함
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
                    border_radius=50,  # 정사각형 100x100에서 반지름 50 → 원형
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                    # 이미지가 원 바깥으로 튀어나가지 않게 잘라줌
                    bgcolor=ft.Colors.WHITE,
                    content=ft.Image(
                        src="dog.jpeg",
                        width=100,
                        height=100,
                        fit=ft.BoxFit.COVER,
                        # 이미지를 영역에 꽉 채움
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
        # 클릭할 때 아래쪽에 잠깐 뜨는 메시지
        page.snack_bar = ft.SnackBar(ft.Text(text))
        page.snack_bar.open = True
        page.update()

    # ---------------------------
    # 툴팁 생성 함수
    # ---------------------------
    def create_tooltip(title):
        # 마우스를 올렸을 때 잠깐 뜨는 설명창
        return ft.Tooltip(
            message=title,
            bgcolor=ft.Colors.BLACK,
            text_style=ft.TextStyle(
                color=ft.Colors.WHITE,
                size=12,
            ),
            wait_duration=200,  # 0.2초 후 표시
        )

    # ---------------------------
    # 공통 인터랙티브 박스 생성 함수
    # ---------------------------
    # 이 함수가 이 코드의 핵심 중 하나
    # summary 카드, menu 박스, 기록 요약 박스를
    # 모두 같은 방식으로 클릭/호버/선택 스타일 처리함
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
        selected_bg=ft.Colors.BLUE_100,
        hover_bg=ft.Colors.BLUE_50,
    ):
        box = ft.Container(
            width=width,
            height=height,
            border_radius=border_radius,
            padding=padding,
            alignment=ft.Alignment(0, 0),
            bgcolor=selected_bg if is_selected else normal_bg,
            # 선택 상태면 selected_bg, 아니면 normal_bg
            tooltip=create_tooltip(title),
            ink=True,
            # 클릭 시 머티리얼 잉크 효과
            on_click=click_handler,
            animate=ft.Animation(140, ft.AnimationCurve.EASE_OUT),
            animate_scale=ft.Animation(140, ft.AnimationCurve.EASE_OUT),
            # 배경색/크기 변화 시 부드럽게 애니메이션
            shadow=ft.BoxShadow(
                blur_radius=12 if is_selected else 8,
                spread_radius=1,
                color=ft.Colors.BLACK26 if is_selected else ft.Colors.BLACK12,
            ),
            content=content,
        )

        # ---------------------------
        # hover(마우스 올림) 효과
        # ---------------------------
        def handle_hover(e):
            hovering = e.data == "true"

            if hovering:
                box.scale = 1.03  # 살짝 커짐
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
        # main() 안의 selected_summary 값을 바꾸기 위해 nonlocal 사용
        selected_summary = index
        refresh_ui()  # 상태 바뀐 뒤 UI 다시 생성
        show_message(f"{title} 선택됨")

    def select_menu(title):
        nonlocal selected_menu
        selected_menu = title
        refresh_ui()
        show_message(f"{title} 선택됨")

    def select_long_box():
        nonlocal selected_long_box
        selected_long_box = not selected_long_box
        # 클릭할 때마다 True/False 반전
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
            # lambda 안에 index/title를 고정해서 클릭 시 전달
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        title,
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900 if is_selected else ft.Colors.BLACK,
                        # 선택되면 파란 글씨, 아니면 검정
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
            width=86,
            height=86,
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
                        color=ft.Colors.BLUE_900 if is_selected else ft.Colors.BLACK,
                    ),
                    ft.Text(
                        title,
                        size=10,
                        weight=ft.FontWeight.BOLD if is_selected else ft.FontWeight.NORMAL,
                        color=ft.Colors.BLUE_900 if is_selected else ft.Colors.BLACK,
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
            height=68,
            is_selected=is_selected,
            click_handler=lambda e: select_long_box(),
            content=ft.Text(
                "기록 요약",
                size=18,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900 if is_selected else ft.Colors.BLACK,
            ),
        )

    # ---------------------------
    # 비어 있는 UI 틀 먼저 생성
    # ---------------------------
    # 여기서는 controls=[] 로 비워두고
    # 아래 refresh_ui()에서 실제 내용을 채워 넣음
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
    # 상태(selected_summary, selected_menu, selected_long_box)에 따라
    # 현재 화면에 보일 컨트롤들을 새로 만들어 넣음
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

    # 페이지에 body 추가
    page.add(body)

    # 최초 1회 UI 생성
    # 이걸 호출해야 controls=[] 상태였던 곳들이 실제 버튼으로 채워짐
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