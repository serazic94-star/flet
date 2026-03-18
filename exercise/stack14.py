import flet as ft
import flet_charts as fch   # 체중 그래프를 그릴 때 쓰는 라이브러리


def main(page: ft.Page):
    # =========================================================
    # 1. 페이지 기본 설정
    # =========================================================
    # 앱이 처음 시작될 때 기본 화면 속성을 설정하는 부분
    # 여기서는 브라우저 탭 제목, 배경색, 바깥 여백을 정함
    page.title = "My Page"
    page.bgcolor = ft.Colors.GREY_100
    page.padding = 0

    # =========================================================
    # 2. 상태(state) 변수
    # =========================================================
    # 이 변수들은 "지금 사용자가 무엇을 선택했는지" 기억하는 용도
    # 화면을 다시 그릴 때 이 값을 보고 선택 상태를 유지함

    selected_summary = None
    # summary 카드 중 어떤 것이 선택됐는지 저장
    # 예: 0 = 섭취량, 1 = 음수량, None = 아직 선택 안 됨

    selected_menu = None
    # 메뉴 박스 중 어떤 메뉴가 선택됐는지 저장
    # 예: "밥주기", "물주기", "관찰기록" 등

    selected_long_box = False
    # "기록 요약" 박스가 선택된 상태인지 저장
    # True / False로 켜짐/꺼짐처럼 사용

    # =========================================================
    # 3. 샘플 데이터
    # =========================================================
    # 체중 기록 화면에서 사용할 임시 데이터
    # 지금은 직접 적어두지만 나중에는 DB/파일/API에서 가져올 수 있음
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
    # 홈 화면이든 체중 기록 화면이든 위쪽 바는 거의 같으므로
    # 함수로 따로 빼서 필요할 때마다 가져다 씀
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
    # 여러 화면 아래에 공통으로 붙는 메뉴 바
    # selected_index=4는 현재 MY PAGE가 선택된 것처럼 보이게 함
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
    # 사용자가 버튼을 눌렀을 때 잠깐 뜨는 메시지(스낵바)
    # 예: "체중 저장됨", "이름 클릭됨"
    def show_message(text):
        page.snack_bar = ft.SnackBar(ft.Text(text))
        page.snack_bar.open = True
        page.update()

    # =========================================================
    # 7. 툴팁 생성 함수
    # =========================================================
    # 마우스를 올렸을 때 작은 설명 박스가 뜨도록 만드는 함수
    # 박스마다 제목을 넣어서 재사용함
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
    # 8. 체중기록 화면으로 이동
    # =========================================================
    # "체중기록" 메뉴를 클릭했을 때 실행되는 함수
    # 실제로는 체중 기록 화면 전체를 그리는 render_weight_page()를 호출함
    def go_weight_page(e):
        render_weight_page()

    # =========================================================
    # 9. 홈 화면 전체를 그리는 함수
    # =========================================================
    # 이 함수가 실행되면 홈 화면을 처음부터 다시 그림
    # 즉, 카드 선택/메뉴 선택/뒤로가기 등을 할 때 자주 다시 호출됨
    def render_home():
        # nonlocal:
        # 바깥(main 함수 안)에 있는 상태변수를 여기서 수정하겠다는 뜻
        # 이게 있어야 selected_summary = index 같은 변경이 가능함
        nonlocal selected_summary, selected_menu, selected_long_box

        # 기존 화면 내용을 싹 지우고
        page.clean()

        # 공통 상단바/하단바를 다시 붙임
        page.appbar = top_appbar()
        page.navigation_bar = bottom_nav()

        # ---------------------------------------------------------
        # 프로필 오른쪽에 있는 작은 정보 박스 공통 함수
        # ---------------------------------------------------------
        # 이름 / 성별 / 나이 박스를 같은 스타일로 만들기 위해 사용
        # content_value에 글자 또는 Row 같은 컨트롤을 넣을 수 있음
        def side_container(content_value, event=None):
            return ft.Container(
                width=130,
                height=34,
                border_radius=12,
                bgcolor=ft.Colors.WHITE,
                alignment=ft.Alignment(0, 0),
                ink=True,              # 클릭 시 잉크 퍼지는 효과
                on_click=event,        # 눌렀을 때 실행할 함수
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

        # ---------------------------------------------------------
        # 프로필 박스 눌렀을 때 알림 띄우기
        # ---------------------------------------------------------
        # 이름/성별/나이 박스가 클릭됐는지 확인용
        def click_print(e, label):
            show_message(f"{label} 클릭됨")

        # ---------------------------------------------------------
        # 프로필 영역
        # ---------------------------------------------------------
        # 왼쪽 = 강아지 사진
        # 오른쪽 = 이름 / 성별 / 나이
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
                                    border_radius=50,   # 100x100의 절반 -> 원형
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
        # 클릭 가능한 박스의 공통 틀
        # ---------------------------------------------------------
        # summary 카드 / 메뉴 박스 / 기록 요약 박스를
        # 같은 방식으로 만들기 위해 만든 재사용 함수
        #
        # 이 함수 덕분에 박스 모양, 그림자, hover 효과를 한 곳에서 관리 가능
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

            # 마우스를 올리면 박스가 살짝 커지고 그림자가 진해짐
            # 데스크톱 UI 느낌을 주기 위한 hover 효과
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

                # 이미 만들어진 박스 모양을 즉시 다시 반영
                box.update()

            box.on_hover = handle_hover
            return box

        # ---------------------------------------------------------
        # summary 카드 선택 처리
        # ---------------------------------------------------------
        # "섭취량", "음수량" 중 하나를 누르면 여기로 옴
        # 상태값을 바꾸고 홈 화면을 다시 그림
        def select_summary(index, title):
            nonlocal selected_summary
            selected_summary = index
            render_home()
            show_message(f"{title} 선택됨")

        # ---------------------------------------------------------
        # 메뉴 선택 처리
        # ---------------------------------------------------------
        # 체중기록을 제외한 일반 메뉴 클릭 시 사용
        # 어떤 메뉴가 선택됐는지만 저장하고 홈 화면 다시 그림
        def select_menu(title):
            nonlocal selected_menu
            selected_menu = title
            render_home()
            show_message(f"{title} 선택됨")

        # ---------------------------------------------------------
        # 기록 요약 박스 토글 처리
        # ---------------------------------------------------------
        # False -> True / True -> False 로 바꾼 뒤
        # 다시 홈 화면을 그림
        def select_long_box():
            nonlocal selected_long_box
            selected_long_box = not selected_long_box
            render_home()
            show_message("기록 요약 선택됨")

        # ---------------------------------------------------------
        # summary 카드 1개 생성 함수
        # ---------------------------------------------------------
        # "섭취량", "음수량" 카드 모양을 만드는 함수
        # index를 비교해서 현재 선택된 카드인지 판단
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

        # ---------------------------------------------------------
        # 메뉴 박스 1개 생성 함수
        # ---------------------------------------------------------
        # 밥주기 / 물주기 / 약먹기 / 체중기록 같은 박스를 만드는 함수
        #
        # 여기서 중요한 점:
        # "체중기록"은 단순 선택이 아니라 다른 화면으로 이동
        # 그래서 click_handler가 다르게 들어감
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
        # 긴 박스("기록 요약") 생성 함수
        # ---------------------------------------------------------
        # 이 박스도 클릭 시 선택 상태를 토글함
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
        # 요약 카드 2개 묶기
        # ---------------------------------------------------------
        summary_cards = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
            controls=[
                summary_card("섭취량", 0),
                summary_card("음수량", 1),
            ],
        )

        # ---------------------------------------------------------
        # 메뉴 6개를 2줄로 배치
        # ---------------------------------------------------------
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

        # ---------------------------------------------------------
        # 기록 요약 박스를 감싸는 영역
        # ---------------------------------------------------------
        long_box_holder = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[long_box_button()],
        )

        # ---------------------------------------------------------
        # 홈 화면 전체 조립
        # ---------------------------------------------------------
        # 지금까지 만든 프로필 / 요약 카드 / 긴 박스 / 메뉴를
        # 세로로 쌓아서 홈 화면 본문 완성
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

        # 최종적으로 페이지에 홈 화면 추가
        page.add(body)
        page.update()

    # =========================================================
    # 10. 체중 그래프 생성 함수
    # =========================================================
    # weight_data를 읽어서 선 그래프로 바꿔주는 함수
    # render_weight_page() 안에서 이 함수를 불러 그래프를 화면에 넣음
    def build_weight_chart():
        # 데이터가 하나도 없으면 그래프 대신 안내 문구 표시
        if not weight_data:
            return ft.Text("기록이 없어서 그래프를 표시할 수 없습니다.")

        points = []
        # 실제 선 그래프에 찍을 점들

        bottom_labels = []
        # x축 아래쪽 날짜 라벨들

        # weight_data를 그래프용 데이터로 변환
        for i, (date_text, weight) in enumerate(weight_data):
            points.append(fch.LineChartDataPoint(i, weight))
            bottom_labels.append(
                fch.ChartAxisLabel(
                    value=i,
                    label=ft.Text(date_text, size=12, color=ft.Colors.BLACK),
                )
            )

        # y축 범위를 잡기 위해 최소/최대 체중 계산
        min_weight = min(weight for _, weight in weight_data)
        max_weight = max(weight for _, weight in weight_data)

        # 체중값이 전부 똑같으면 그래프가 일직선으로 납작해져 보이므로
        # 위아래 여유를 강제로 줌
        if min_weight == max_weight:
            min_y = min_weight - 0.5
            max_y = max_weight + 0.5
        else:
            # 체중 차이가 있을 때도 너무 딱 붙지 않게 여백을 추가
            min_y = min_weight - 0.3
            max_y = max_weight + 0.3

        # y축 가운데값도 라벨로 표시하기 위해 계산
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
    # 체중 입력창에 적은 값을 리스트(weight_data)에 추가하는 함수
    # 저장 후에는 체중 화면을 다시 그려서 그래프와 목록이 즉시 갱신되게 함
    def save_weight(weight_input):
        try:
            # TextField 값은 문자열이므로 숫자로 변환
            value = float(weight_input.value)
        except:
            # 숫자가 아니면 저장하지 않고 메시지 표시
            show_message("체중은 숫자로 입력해줘. 예: 4.2")
            return

        # 날짜는 지금 간단하게 자동 증가 방식으로 처리
        # 나중에는 실제 오늘 날짜를 넣도록 바꿀 수 있음
        next_day = len(weight_data) + 1
        date_text = f"3/{9 + next_day}"

        # 새 기록 추가
        weight_data.append((date_text, value))

        # 저장 성공 메시지 표시
        show_message(f"{value}kg 저장됨")

        # 저장 후 체중 화면을 다시 그림
        # 그래프/기록 목록이 바로 최신 상태로 갱신됨
        render_weight_page()

    # =========================================================
    # 12. 체중 기록 화면 전체를 그리는 함수
    # =========================================================
    # 이 함수가 실행되면 홈 화면 대신 체중 기록 화면이 나타남
    def render_weight_page():
        # 현재 화면을 지우고
        page.clean()

        # 공통 상단바/하단바 다시 붙임
        page.appbar = top_appbar()
        page.navigation_bar = bottom_nav()

        # 사용자가 체중을 입력할 칸
        weight_input = ft.TextField(
            label="체중 입력",
            hint_text="예: 4.2",
            width=220,
        )

        # 현재 저장된 체중 기록들을 글자 목록으로 보여주는 영역
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

        # 체중 기록 화면 전체 UI 조립
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
                    # 버튼 누르면 save_weight(weight_input) 실행
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
                    # build_weight_chart()가 실제 그래프를 만들어 넣어줌
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

                    # 다시 홈 화면으로 돌아가는 버튼
                    ft.ElevatedButton(
                        "뒤로가기",
                        on_click=lambda e: render_home(),
                    ),
                ],
            ),
        )

        # 페이지에 체중 화면 추가
        page.add(weight_page)
        page.update()

    # =========================================================
    # 13. 앱 시작 시 처음 보여줄 화면
    # =========================================================
    # 프로그램이 처음 켜지면 홈 화면부터 보이게 함
    render_home()


# =============================================================
# 14. 파이썬 파일을 직접 실행했을 때 앱 시작
# =============================================================
if __name__ == "__main__":
    import webbrowser
    import os

    # FLET_NO_BROWSER 환경변수가 있으면 브라우저 자동 실행 막기
    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    # Flet 앱 실행
    # main(page) 함수가 실제 시작점 역할을 함
    ft.app(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )