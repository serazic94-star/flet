import flet as ft

# 🔥 [추가] long_box 함수 (기존 Container 3개를 대체)
def long_box(text, bgcolor = ft.Colors.WHITE, text_color=ft.Colors.BLACK):
    return ft.Container(
        width=350,
        height=50,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=10,
        bgcolor=bgcolor,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(text, size=14, weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
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
        hint_text = hint_text,
        label=label,  # 선택적으로 라벨도 넣을 수 있음
    )

def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Sign In / Sign Up"

    title_text = ft.Text(
        "Sign In / Sign Up",
        size=22,
        weight=ft.FontWeight.W_600,
        color=ft.Colors.BLACK,
    )

    continue_cards = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        controls=[
            # 🔥 [수정] 기존 Container 3개 → 함수로 변경
            long_box("Continue with Google"),
            long_box("Continue with Apple"),
            long_box("Continue with Kakao"),
        ],
    )

    stop_line = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        width=350,
        controls=[
            ft.Container(
                expand=True,
                height=1,
                bgcolor=ft.Colors.GREY_400,
            ),
            ft.Text("or", size=12),
            ft.Container(
                expand=True,
                height=1,
                bgcolor=ft.Colors.GREY_400,
            ),
        ],
    )

    body = ft.Container(
        padding=ft.padding.only(top=-150),  # 🔥 (기존 ft.Padding → ft.padding으로 수정 권장)
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Container(
                    width=float("inf"),  # 👉 전체 너비 차지
                    alignment=ft.Alignment(-1, 0),  # 👉 왼쪽 정렬  # 👈 왼쪽 이동
                    content=ft.Icon(ft.Icons.ARROW_BACK),
                ),
                title_text,
                continue_cards,
                stop_line,
                long_box("Continue with Email"),                   
                  ft.Container(
                  width=350,
                  alignment=ft.Alignment(-1, 0),
                  content=ft.Text("이메일"),
              ),
                input_box(hint_text="이메일 주소를 입력하세요"),
                long_box("Continue", bgcolor=ft.Colors.YELLOW)
            ],
        ),
    )

    page.add(body)


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