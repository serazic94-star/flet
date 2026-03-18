import flet as ft

def main(page: ft.Page):
    page.title = "My Page"
    page.bgcolor = ft.Colors.GREY_100

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

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="HOME"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="LOG"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="MY PAGE"),
        ],
        selected_index=2,
    )

    profile_section = ft.Container(
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6,
            controls=[
                ft.Container(
                    width=100,
                    height=100,
                    border_radius=50,
                    clip_behavior=ft.ClipBehavior.HARD_EDGE, # 이미지가 컨테이너 밖으로 튀어나가지 못하게 자르는 역할
                    bgcolor=ft.Colors.WHITE,
                    content=ft.Image( # 강아지 사진
                        src="dog.jpeg",
                        width=100,
                        height=100,
                        fit="cover",
                    ),
                )
            ],
        ),
        padding=ft.Padding.only(top=12, bottom=4),
    )

    summary_cards = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=12,  # ⭐ 수정: 16 -> 12
        controls=[
            ft.Container(
                width=145,  # ⭐ 수정: 160 -> 145
                height=90,  # ⭐ 수정: 100 -> 90
                bgcolor=ft.Colors.WHITE,
                border_radius=20,
                padding=12,  # ⭐ 수정: 15 -> 12
                shadow=ft.BoxShadow(
                    blur_radius=8,
                    spread_radius=1,
                    color=ft.Colors.BLACK12,
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Text("내 반려동물", size=12, color=ft.Colors.GREY_700),  # ⭐ 수정
                        ft.Text("2마리", size=20, weight=ft.FontWeight.BOLD),  # ⭐ 수정
                    ],
                ),
            ),
            ft.Container(
                width=145,  # ⭐ 수정: 160 -> 145
                height=90,  # ⭐ 수정: 100 -> 90
                bgcolor=ft.Colors.WHITE,
                border_radius=20,
                padding=12,  # ⭐ 수정: 15 -> 12
                shadow=ft.BoxShadow(
                    blur_radius=8,
                    spread_radius=1,
                    color=ft.Colors.BLACK12,
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Text("구독 상태", size=12, color=ft.Colors.GREY_700),  # ⭐ 수정
                        ft.Text("이용 중", size=20, weight=ft.FontWeight.BOLD),  # ⭐ 수정
                    ],
                ),
            ),
        ],
    )

    long_box = ft.Container(
        width=320,
        height=68,
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        padding=12,
        shadow=ft.BoxShadow(
            blur_radius=8,
            spread_radius=1,
            color=ft.Colors.BLACK12,
        ),
        alignment=ft.Alignment(0, 0),
        content=ft.Text(
            "기록 요약",
            size=18,
            weight=ft.FontWeight.BOLD,
        ),
    )

    # =========================
    # 카드 재사용 함수
    # =========================
    def action_card(icon, label):
        return ft.Container(
            width=95,   # ⭐ 수정: 110 -> 95
            height=95,  # ⭐ 수정: 110 -> 95
            bgcolor=ft.Colors.WHITE,
            border_radius=20,
            alignment=ft.Alignment(0, 0),
            shadow=ft.BoxShadow(
                blur_radius=8,
                spread_radius=1,
                color=ft.Colors.BLACK12,
            ),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=6,  # ⭐ 수정: 8 -> 6
                controls=[
                    ft.Icon(icon, size=26),  # ⭐ 수정: 30 -> 26
                    ft.Text(label, size=11),  # ⭐ 수정: 12 -> 11
                ],
            ),
        )

    # =========================
    # 6개 기능 카드 (2x3)
    # =========================
    action_grid = ft.Column(
        spacing=12,  # ⭐ 수정: 16 -> 12
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=12,  # ⭐ 수정: 16 -> 12
                controls=[
                    action_card(ft.Icons.RESTAURANT, "밥주기"),
                    action_card(ft.Icons.WATER, "물주기"),
                    action_card(ft.Icons.MEDICAL_SERVICES, "약먹기"),
                ],
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=12,  # ⭐ 수정: 16 -> 12
                controls=[
                    action_card(ft.Icons.PETS, "대소변기록"),
                    action_card(ft.Icons.MONITOR_WEIGHT, "체중기록"),
                    action_card(ft.Icons.EDIT, "관찰기록"),
                ],
            ),
        ],
    )

    # =========================
    # 본문 구성
    # =========================
    body = ft.Container(
        padding=ft.padding.only(bottom=20),  # ⭐ 추가: 하단 잘림 완화용 여백
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=14,  # ⭐ 수정: 20 -> 14
            controls=[
                profile_section,
                summary_cards,
                long_box,
                action_grid,
            ],
        ),
    )

    page.add(body)


# =============================================================
# 파이썬 파일을 직접 실행했을 때 앱 시작
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