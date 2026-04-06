import flet as ft
import flet_charts as fch   # [추가] 그래프용 import


def main(page: ft.Page):
    page.title = "My Page"
    page.bgcolor = ft.Colors.GREY_100
    page.padding = 0

    selected_summary = None
    selected_menu = None
    selected_long_box = False

    # [추가] 체중 기록용 샘플 데이터
    # 나중에는 DB나 파일에서 불러오면 됨
    weight_data = [
        ("3/10", 4.1),
        ("3/11", 4.2),
        ("3/12", 4.0),
        ("3/13", 4.3),
        ("3/14", 4.25),
    ]

    # ---------------------------
    # 공통 상단 앱바
    # ---------------------------
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

    # ---------------------------
    # 공통 하단 네비게이션 바
    # ---------------------------
    def bottom_nav():
        return ft.NavigationBar(
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
    # 스낵바 메시지
    # ---------------------------
    def show_message(text):
        page.snack_bar = ft.SnackBar(ft.Text(text))
        page.snack_bar.open = True
        page.update()

    # ---------------------------
    # 툴팁
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
    # 체중기록 화면으로 이동
    # ---------------------------
    def go_weight_page(e):
        render_weight_page()

    # ---------------------------
    # 홈 화면 렌더링 함수
    # ---------------------------
    def render_home():
        nonlocal selected_summary, selected_menu, selected_long_box

        page.clean()
        page.appbar = top_appbar()
        page.navigation_bar = bottom_nav()

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
                            color=ft.Colors.BLACK,
                        ),
                    ],
                ),
            )

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

    # ---------------------------
    # [추가] 체중 그래프 만드는 함수
    # ---------------------------
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

        # [추가] 최소/최대가 같으면 그래프가 납작해지므로 범위 보정
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

    # ---------------------------
    # [추가] 체중 저장 함수
    # ---------------------------
    def save_weight(weight_input):
        try:
            value = float(weight_input.value)
        except:
            show_message("체중은 숫자로 입력해줘. 예: 4.2")
            return

        # [추가] 날짜는 일단 간단하게 자동 증가
        next_day = len(weight_data) + 1
        date_text = f"3/{9 + next_day}"

        weight_data.append((date_text, value))
        show_message(f"{value}kg 저장됨")
        render_weight_page()

    # ---------------------------
    # 체중기록 화면 렌더링 함수
    # ---------------------------
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

    render_home()


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