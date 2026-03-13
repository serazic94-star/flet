import flet as ft
import flet_charts as fch   # 체중 그래프를 그릴 때 쓰는 라이브러리


def main(page: ft.Page):
    # =========================================================
    # 1. 페이지 기본 설정
    # =========================================================
    page.title = "My Page"
    page.bgcolor = ft.Colors.GREY_100
    page.padding = 0

    # =========================================================
    # 2. 상태(state) 변수
    # =========================================================
    selected_summary = None
    # 0 = 섭취량, 1 = 음수량, None = 아직 선택 안 됨

    selected_menu = None
    # 메뉴 박스 중 어떤 메뉴가 선택됐는지 저장

    selected_long_box = False
    # "기록 요약" 박스 선택 상태

    # =========================================================
    # 3. 샘플 데이터
    # =========================================================
    weight_data = [
        ("3/10", 4.1),
        ("3/11", 4.2),
        ("3/12", 4.0),
        ("3/13", 4.3),
        ("3/14", 4.25),
    ]

    # =========================================================
    # 4. 공통 상단바
    # =========================================================
    def top_appbar():
        return ft.AppBar(
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

    # =========================================================
    # 5. 공통 하단 네비게이션 바
    # =========================================================
    def bottom_nav():
        return ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="HOME"),
                ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="LOG"),
                ft.NavigationBarDestination(icon=ft.Icons.STAR, label="SHOP"),
                ft.NavigationBarDestination(icon=ft.Icons.FAVORITE, label="AI"),
                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="MY PAGE"),
            ],
            selected_index=2,
        )

    # =========================================================
    # 6. 화면 아래쪽 알림 메시지 함수
    # =========================================================
    def show_message(text):
        page.snack_bar = ft.SnackBar(ft.Text(text))
        page.snack_bar.open = True
        page.update()

    # =========================================================
    # 7. 툴팁 생성 함수
    # =========================================================
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

    # =========================================================
    # 8. 화면 이동 함수
    # =========================================================
    def go_weight_page(e):
        render_weight_page()

    def go_water_calc_page(e):
        render_water_calc_page()

    # =========================================================
    # 9. 홈 화면 전체를 그리는 함수
    # =========================================================
    def render_home():
        nonlocal selected_summary, selected_menu, selected_long_box

        page.clean()
        page.appbar = top_appbar()
        page.navigation_bar = bottom_nav()

        # ---------------------------------------------------------
        # 프로필 오른쪽 작은 정보 박스
        # ---------------------------------------------------------
        def side_container(content_value, event=None):
            return ft.Container(
                width=130,
                height=34,
                border_radius=12,
                bgcolor=ft.Colors.WHITE,
                alignment=ft.Alignment(0, 0),
                ink=True,
                on_click=event,
                shadow=ft.BoxShadow(
                    blur_radius=6,
                    spread_radius=1,
                    color=ft.Colors.BLACK12,
                ),
                content=(
                    content_value
                    if isinstance(content_value, ft.Control)
                    else ft.Text(
                        content_value,
                        size=14,
                        color=ft.Colors.BLACK,
                        text_align=ft.TextAlign.CENTER,
                    )
                ),
            )

        def click_print(e, label):
            show_message(f"{label} 클릭됨")

        # ---------------------------------------------------------
        # 프로필 영역
        # ---------------------------------------------------------
        profile_section = ft.Container(
            padding=ft.Padding.only(top=12, bottom=4),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12,
                controls=[
                    ft.Container(
                        margin=ft.Margin.only(right=6),
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
                    ),
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=8,
                        controls=[
                            side_container("옥지", event=lambda e: click_print(e, "이름")),
                            side_container(
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=4,
                                    controls=[
                                        ft.Icon(
                                            ft.Icons.MALE,
                                            size=16,
                                            color=ft.Colors.BLUE,
                                        ),
                                        ft.Text(
                                            "남아",
                                            size=14,
                                            color=ft.Colors.BLACK,
                                            text_align=ft.TextAlign.CENTER,
                                        ),
                                    ],
                                ),
                                event=lambda e: click_print(e, "성별"),
                            ),
                            side_container("3세", event=lambda e: click_print(e, "나이")),
                        ],
                    ),
                ],
            ),
        )

        # ---------------------------------------------------------
        # 클릭 가능한 박스 공통 함수
        # ---------------------------------------------------------
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
            selected_bg=ft.Colors.WHITE,
            hover_bg=ft.Colors.WHITE,
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

        # ---------------------------------------------------------
        # 선택 처리
        # ---------------------------------------------------------
        def select_summary(index, title):
            nonlocal selected_summary
            selected_summary = index
            render_home()
            show_message(f"{title} 선택됨")

        def select_menu(title):
            nonlocal selected_menu
            selected_menu = title
            render_home()
            show_message(f"{title} 선택됨")

        def select_long_box():
            nonlocal selected_long_box
            selected_long_box = not selected_long_box
            render_home()
            show_message("기록 요약 선택됨")

        # ---------------------------------------------------------
        # summary 카드 생성
        # ---------------------------------------------------------
        def summary_card(title, index):
            is_selected = selected_summary == index

            if title == "음수량":
                click_handler = go_water_calc_page
            else:
                click_handler = lambda e, i=index, t=title: select_summary(i, t)

            return make_interactive_box(
                title=title,
                width=150,
                height=90,
                is_selected=is_selected,
                click_handler=click_handler,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            title,
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLACK,
                        ),
                    ],
                ),
            )

        # ---------------------------------------------------------
        # 메뉴 박스 생성
        # ---------------------------------------------------------
        def menu_box(icon, title):
            is_selected = selected_menu == title

            if title == "체중기록":
                click_handler = go_weight_page
            else:
                click_handler = lambda e, t=title: select_menu(t)

            return make_interactive_box(
                title=title,
                width=96,
                height=96,
                border_radius=16,
                padding=10,
                is_selected=is_selected,
                click_handler=click_handler,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                    controls=[
                        ft.Icon(icon, size=24, color=ft.Colors.BLACK),
                        ft.Text(
                            title,
                            size=10,
                            weight=ft.FontWeight.BOLD if is_selected else ft.FontWeight.NORMAL,
                            color=ft.Colors.BLACK,
                        ),
                    ],
                ),
            )

        # ---------------------------------------------------------
        # 기록 요약 박스
        # ---------------------------------------------------------
        def long_box_button():
            is_selected = selected_long_box

            return make_interactive_box(
                title="기록 요약",
                width=320,
                height=78,
                is_selected=is_selected,
                click_handler=lambda e: select_long_box(),
                content=ft.Text(
                    "기록 요약",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK,
                ),
            )

        # ---------------------------------------------------------
        # 홈 화면 배치
        # ---------------------------------------------------------
        summary_cards = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
            controls=[
                summary_card("섭취량", 0),
                summary_card("음수량", 1),
            ],
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

        long_box_holder = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[long_box_button()],
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
                    long_box_holder,
                    menu_grid,
                ],
            ),
        )

        page.add(body)
        page.update()

    # =========================================================
    # 10. 체중 그래프 생성 함수
    # =========================================================
    def build_weight_chart():
        if not weight_data:
            return ft.Text("기록이 없어서 그래프를 표시할 수 없습니다.")

        points = []
        bottom_labels = []

        for i, (date_text, weight) in enumerate(weight_data):
            points.append(fch.LineChartDataPoint(i, weight))
            bottom_labels.append(
                fch.ChartAxisLabel(
                    value=i,
                    label=ft.Text(date_text, size=12, color=ft.Colors.BLACK),
                )
            )

        min_weight = min(weight for _, weight in weight_data)
        max_weight = max(weight for _, weight in weight_data)

        if min_weight == max_weight:
            min_y = min_weight - 0.5
            max_y = max_weight + 0.5
        else:
            min_y = min_weight - 0.3
            max_y = max_weight + 0.3

        mid_weight = (min_y + max_y) / 2

        return fch.LineChart(
            data_series=[
                fch.LineChartData(
                    points=points,
                    stroke_width=4,
                    color=ft.Colors.CYAN,
                    curved=True,
                    rounded_stroke_cap=True,
                )
            ],
            min_x=0,
            max_x=len(weight_data) - 1,
            min_y=min_y,
            max_y=max_y,
            border=ft.Border.all(2, ft.Colors.BLACK12),
            horizontal_grid_lines=fch.ChartGridLines(
                interval=0.2,
                color=ft.Colors.BLACK12,
                width=1,
            ),
            vertical_grid_lines=fch.ChartGridLines(
                interval=1,
                color=ft.Colors.BLACK12,
                width=1,
            ),
            left_axis=fch.ChartAxis(
                label_size=50,
                labels=[
                    fch.ChartAxisLabel(
                        value=min_y,
                        label=ft.Text(f"{min_y:.1f}kg", size=11),
                    ),
                    fch.ChartAxisLabel(
                        value=mid_weight,
                        label=ft.Text(f"{mid_weight:.1f}kg", size=11),
                    ),
                    fch.ChartAxisLabel(
                        value=max_y,
                        label=ft.Text(f"{max_y:.1f}kg", size=11),
                    ),
                ],
            ),
            bottom_axis=fch.ChartAxis(
                labels=bottom_labels,
                label_size=35,
            ),
            tooltip=fch.LineChartTooltip(
                bgcolor=ft.Colors.BLUE_GREY,
            ),
            interactive=True,
            width=700,
            height=300,
        )

    # =========================================================
    # 11. 체중 저장 함수
    # =========================================================
    def save_weight(weight_input):
        try:
            value = float(weight_input.value)
        except:
            show_message("체중은 숫자로 입력해줘. 예: 4.2")
            return

        next_day = len(weight_data) + 1
        date_text = f"3/{9 + next_day}"

        weight_data.append((date_text, value))
        show_message(f"{value}kg 저장됨")
        render_weight_page()

    # =========================================================
    # 12. 음수량 계산기 화면
    # =========================================================
    def render_water_calc_page():
        page.clean()
        page.appbar = top_appbar()
        page.navigation_bar = bottom_nav()

        weight_input = ft.TextField(
            label="몸무게 입력 (kg)",
            hint_text="예: 3",
            width=280,  # [수정] 입력칸을 조금 넓혀서 답답하지 않게 조정
            text_align=ft.TextAlign.CENTER,
        )

        result_text = ft.Text(
            "",
            size=18,  # [수정] 결과 글씨가 너무 커서 박스가 커 보이지 않게 약간 축소
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE,
            text_align=ft.TextAlign.CENTER,
        )

        def calculate_water(e):
            try:
                weight = float(weight_input.value)
                water_amount = weight * 50
                result_text.value = (
                    f"{weight:.1f}kg 강아지 > 하루 {water_amount:.0f}ml 권장"
                )
            except:
                result_text.value = "몸무게를 숫자로 입력해줘. 예: 3 또는 3.5"

            page.update()

        water_page = ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0),  # 중앙 정렬 유지
            padding=ft.Padding.symmetric(horizontal=16, vertical=16),  # [수정] 바깥 여백 최소화
            content=ft.Container(
                width=420,  # [수정] 흰 박스 너비 축소 (기존 500 -> 420)
                padding=22,  # [수정] 안쪽 여백 축소 (기존 30 -> 22)
                border_radius=20,
                bgcolor=ft.Colors.WHITE,
                shadow=ft.BoxShadow(
                    blur_radius=10,
                    spread_radius=1,
                    color=ft.Colors.BLACK12,
                ),
                content=ft.Column(
                    # [수정] 컨텐츠 높이만큼만 차지하게 해서 박스가 과하게 커 보이지 않게 함
                    tight=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=14,  # [수정] 요소 간격도 조금 줄임
                    controls=[
                        ft.Text(
                            "하루 적정 음수량 = 몸무게(kg) x 50ml",
                            size=18,  # [수정] 제목 크기 소폭 축소
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLACK,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Text(
                            "ex) 몸무게 3kg 강아지 > 하루 150ml 권장",
                            size=13,
                            color=ft.Colors.BLACK54,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        weight_input,
                        ft.ElevatedButton(
                            "계산하기",
                            on_click=calculate_water,
                        ),
                        result_text,
                        ft.ElevatedButton(
                            "뒤로가기",
                            on_click=lambda e: render_home(),
                        ),
                    ],
                ),
            ),
        )

        page.add(water_page)
        page.update()

    # =========================================================
    # 13. 체중 기록 화면 전체를 그리는 함수
    # =========================================================
    def render_weight_page():
        page.clean()
        page.appbar = top_appbar()
        page.navigation_bar = bottom_nav()

        weight_input = ft.TextField(
            label="체중 입력",
            hint_text="예: 4.2",
            width=220,
        )

        record_list = ft.Column(
            spacing=6,
            controls=[
                ft.Text(
                    f"{date_text} : {weight:.2f}kg",
                    size=14,
                    color=ft.Colors.BLACK,
                )
                for date_text, weight in weight_data
            ],
        )

        weight_page = ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    ft.Text(
                        "체중 기록 화면",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK,
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            weight_input,
                            ft.ElevatedButton(
                                "저장",
                                on_click=lambda e: save_weight(weight_input),
                            ),
                        ],
                    ),
                    ft.Container(
                        bgcolor=ft.Colors.WHITE,
                        border_radius=16,
                        padding=20,
                        content=build_weight_chart(),
                    ),
                    ft.Container(
                        width=500,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=16,
                        padding=20,
                        content=ft.Column(
                            spacing=10,
                            controls=[
                                ft.Text(
                                    "기록 목록",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLACK,
                                ),
                                record_list,
                            ],
                        ),
                    ),
                    ft.ElevatedButton(
                        "뒤로가기",
                        on_click=lambda e: render_home(),
                    ),
                ],
            ),
        )

        page.add(weight_page)
        page.update()

    # =========================================================
    # 14. 앱 시작 시 처음 보여줄 화면
    # =========================================================
    render_home()


# =============================================================
# 15. 파이썬 파일을 직접 실행했을 때 앱 시작
# =============================================================
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