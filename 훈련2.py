import flet as ft

# 🔥 [추가] long_box 함수 (기존 Container 3개를 대체)
def long_box(text):
    return ft.Container(
        width=350,
        height=50,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=10,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(text, size=14, weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            ],
        ),
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
        padding=ft.padding.only(top=-180),  # 🔥 (기존 ft.Padding → ft.padding으로 수정 권장)
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                title_text,
                continue_cards,
                stop_line,
                long_box("Continue with Email"),
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