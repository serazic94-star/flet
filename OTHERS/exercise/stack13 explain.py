import flet as ft
import flet_charts as fch   # 그래프를 그릴 때 사용하는 라이브러리


def main(page: ft.Page):
    # ---------------------------
    # 페이지 기본 설정
    # ---------------------------
    page.title = "My Page"                 # 브라우저 탭 제목
    page.bgcolor = ft.Colors.GREY_100      # 전체 배경색
    page.padding = 0                       # 바깥 기본 여백 제거

    # ---------------------------
    # 상태(state) 변수
    # ---------------------------
    # 사용자가 무엇을 선택했는지 기억하는 변수들
    selected_summary = None       # "섭취량", "음수량" 중 현재 선택된 카드
    selected_menu = None          # 메뉴 박스 중 현재 선택된 것
    selected_long_box = False     # "기록 요약" 박스 선택 여부

    # ---------------------------
    # 체중 기록용 샘플 데이터
    # ---------------------------
    # 형식: (날짜, 체중)
    # 나중에는 DB나 파일에서 불러오는 방식으로 바꿀 수 있음
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
    # 홈 화면이든 체중 화면이든 위쪽 바는 똑같이 쓰기 때문에 함수로 분리
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
    # 아래 메뉴바도 여러 화면에서 공통 사용
    def bottom_nav():
        return ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="HOME"),
                ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="LOG"),
                ft.NavigationBarDestination(icon=ft.Icons.STAR, label="SHOP"),
                ft.NavigationBarDestination(icon=ft.Icons.FAVORITE, label="AI"),
                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="MY PAGE"),
            ],
            selected_index=4,  # 현재 MY PAGE가 선택된 상태로 표시
        )

    # ---------------------------
    # 스낵바 메시지 표시 함수
    # ---------------------------
    # 화면 아래쪽에 잠깐 뜨는 알림 메시지
    def show_message(text):
        page.snack_bar = ft.SnackBar(ft.Text(text))
        page.snack_bar.open = True
        page.update()

    # ---------------------------
    # 툴팁 함수
    # ---------------------------
    # 마우스를 올렸을 때 뜨는 작은 설명 박스
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
    # 메뉴 중 "체중기록"을 눌렀을 때 실행
    def go_weight_page(e):
        render_weight_page()

    # ---------------------------
    # 홈 화면 렌더링 함수
    # ---------------------------
    # 홈 화면 전체를 다시 그리는 함수
    def render_home():
        nonlocal selected_summary, selected_menu, selected_long_box

        # 기존 화면 내용 지우기
        page.clean()

        # 공통 상단/하단 UI 넣기
        page.appbar = top_appbar()
        page.navigation_bar = bottom_nav()

        # ---------------------------
        # 프로필 오른쪽 작은 박스 공통 함수
        # ---------------------------
        # 예: 옥지 / 남아 / 3세
        def side_container(content_value, event=None):
            return ft.Container(
                width=130,
                height=34,
                border_radius=12,
                bgcolor=ft.Colors.WHITE,
                alignment=ft.Alignment(0, 0),
                ink=True,              # 클릭 시 잉크 효과
                on_click=event,        # 클릭 이벤트
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

        # ---------------------------
        # 클릭 시 메시지 출력
        # ---------------------------
        # 이름 / 성별 / 나이 박스를 눌렀을 때 어떤 게 눌렸는지 보여줌
        def click_print(e, label):
            show_message(f"{label} 클릭됨")

        # ---------------------------
        # 프로필 영역
        # ---------------------------
        # 왼쪽: 강아지 사진
        # 오른쪽: 이름 / 성별 / 나이
        profile_section = ft.Container(
            padding=ft.Padding.only(top=12, bottom=4),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12,
                controls=[
                    # 프로필 사진 영역
                    ft.Container(
                        margin=ft.Margin.only(right=6),
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=6,
                            controls=[
                                ft.Container(
                                    width=100,
                                    height=100,
                                    border_radius=50,   # 원형 모양
                                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                    bgcolor=ft.Colors.WHITE,
                                    content=ft.Image(
                                        src="dog.jpeg",   # assets 폴더 안의 이미지
                                        width=100,
                                        height=100,
                                        fit=ft.BoxFit.COVER,
                                    ),
                                )
                            ],
                        ),
                    ),
                    # 이름 / 성별 / 나이 영역
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

        # ---------------------------
        # 공통 클릭 박스 생성 함수
        # ---------------------------
        # summary 카드, menu 박스, 기록 요약 박스를
        # 하나의 공통 틀로 만들기 위한 함수
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

            # 마우스를 올리면 박스가 약간 커지고 그림자가 진해짐
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
        # summary 카드 선택 함수
        # ---------------------------
        # "섭취량" 또는 "음수량" 클릭 시 실행
        def select_summary(index, title):
            nonlocal selected_summary
            selected_summary = index
            render_home()                     # 상태 반영해서 홈 화면 다시 그림
            show_message(f"{title} 선택됨")

        # ---------------------------
        # 메뉴 선택 함수
        # ---------------------------
        def select_menu(title):
            nonlocal selected_menu
            selected_menu = title
            render_home()
            show_message(f"{title} 선택됨")

        # ---------------------------
        # 기록 요약 박스 선택 함수
        # ---------------------------
        def select_long_box():
            nonlocal selected_long_box
            selected_long_box = not selected_long_box
            render_home()
            show_message("기록 요약 선택됨")

        # ---------------------------
        # summary 카드 생성 함수
        # ---------------------------
        # "섭취량", "음수량" 박스를 만드는 함수
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

        # ---------------------------
        # 메뉴 박스 생성 함수
        # ---------------------------
        # 밥주기 / 물주기 / 체중기록 등 아이콘 메뉴용
        def menu_box(icon, title):
            is_selected = selected_menu == title

            # 체중기록만 눌렀을 때 다른 화면으로 이동
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

        # ---------------------------
        # 긴 박스 생성 함수
        # ---------------------------
        # "기록 요약" 박스를 만드는 함수
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

        # ---------------------------
        # 요약 카드 2개 묶기
        # ---------------------------
        summary_cards = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
            controls=[
                summary_card("섭취량", 0),
                summary_card("음수량", 1),
            ],
        )

        # ---------------------------
        # 메뉴 6개를 2줄로 배치
        # ---------------------------
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

        # ---------------------------
        # 기록 요약 박스 감싸기
        # ---------------------------
        long_box_holder = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[long_box_button()],
        )

        # ---------------------------
        # 홈 화면 전체 본문 조립
        # ---------------------------
        # 위에서 만든 프로필, 카드, 긴 박스, 메뉴를 한 화면으로 묶음
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

        # 실제 페이지에 추가
        page.add(body)
        page.update()

    # ---------------------------
    # 체중 그래프 생성 함수
    # ---------------------------
    def build_weight_chart():
        # 데이터가 없으면 안내 문구 표시
        if not weight_data:
            return ft.Text("기록이 없어서 그래프를 표시할 수 없습니다.")

        points = []         # 그래프 점들
        bottom_labels = []  # 아래쪽 x축 날짜 라벨들

        # weight_data를 그래프용 점과 날짜 라벨로 변환
        for i, (date_text, weight) in enumerate(weight_data):
            points.append(fch.LineChartDataPoint(i, weight))
            bottom_labels.append(
                fch.ChartAxisLabel(
                    value=i,
                    label=ft.Text(date_text, size=12, color=ft.Colors.BLACK),
                )
            )

        # 최소 체중 / 최대 체중 계산
        min_weight = min(weight for _, weight in weight_data)
        max_weight = max(weight for _, weight in weight_data)

        # 최소값과 최대값이 같으면 그래프가 납작해지므로 범위를 일부러 벌려줌
        if min_weight == max_weight:
            min_y = min_weight - 0.5
            max_y = max_weight + 0.5
        else:
            min_y = min_weight - 0.3
            max_y = max_weight + 0.3

        # 가운데 값 하나도 y축 라벨로 쓰기 위해 계산
        mid_weight = (min_y + max_y) / 2

        # 실제 선 그래프 반환
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
    # 체중 저장 함수
    # ---------------------------
    def save_weight(weight_input):
        try:
            # 입력값을 숫자로 변환
            value = float(weight_input.value)
        except:
            # 숫자가 아니면 에러 메시지
            show_message("체중은 숫자로 입력해줘. 예: 4.2")
            return

        # 날짜를 임시로 자동 생성
        # 현재는 단순히 데이터 개수에 따라 날짜를 늘리는 방식
        next_day = len(weight_data) + 1
        date_text = f"3/{9 + next_day}"

        # 새 체중 기록 추가
        weight_data.append((date_text, value))

        # 저장 메시지 띄우고 체중 화면 다시 그림
        show_message(f"{value}kg 저장됨")
        render_weight_page()

    # ---------------------------
    # 체중기록 화면 렌더링 함수
    # ---------------------------
    def render_weight_page():
        # 화면 초기화
        page.clean()
        page.appbar = top_appbar()
        page.navigation_bar = bottom_nav()

        # 체중 입력창
        weight_input = ft.TextField(
            label="체중 입력",
            hint_text="예: 4.2",
            width=220,
        )

        # 기록 목록 만들기
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

        # 체중기록 화면 전체 UI
        weight_page = ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    # 화면 제목
                    ft.Text(
                        "체중 기록 화면",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK,
                    ),

                    # 입력창 + 저장 버튼
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

                    # 그래프 카드
                    ft.Container(
                        bgcolor=ft.Colors.WHITE,
                        border_radius=16,
                        padding=20,
                        content=build_weight_chart(),
                    ),

                    # 기록 목록 카드
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

                    # 홈으로 돌아가는 버튼
                    ft.ElevatedButton(
                        "뒤로가기",
                        on_click=lambda e: render_home(),
                    ),
                ],
            ),
        )

        # 페이지에 추가
        page.add(weight_page)
        page.update()

    # ---------------------------
    # 앱 시작 시 처음 보여줄 화면
    # ---------------------------
    render_home()


# ---------------------------
# 프로그램 직접 실행 시 앱 시작
# ---------------------------
if __name__ == "__main__":
    import webbrowser
    import os

    # 환경변수 FLET_NO_BROWSER가 있으면 브라우저 자동 실행 막기
    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    # Flet 앱 실행
    ft.app(
        main,
        assets_dir="assets",              # 이미지 파일 등이 들어있는 폴더
        view=ft.AppView.WEB_BROWSER,      # 브라우저에서 실행
        port=34636,                       # 포트 번호
    )