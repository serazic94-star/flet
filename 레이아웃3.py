import flet as ft

def section_gap(size=40):
    return ft.Container(height=size)

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

def long_box(text, bgcolor = ft.Colors.WHITE, text_color=ft.Colors.BLACK, on_click=None):
    return ft.Container(
        width=350,
        height=50,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=10,
        bgcolor=bgcolor,
        on_click=on_click,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(text, size=14, weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            ],
        ),
    )


def bottom_continue_button(on_click=None):
    return ft.Container(
        alignment=ft.Alignment(0, 1),
        padding=ft.padding.only(bottom=20),
        content=long_box(
            "Continue",
            bgcolor=ft.Colors.YELLOW,
            text_color=ft.Colors.BLACK,
            on_click=on_click,
        ),
    )

def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    body = ft.Container(
        padding=ft.padding.only(top=0),
        content=ft.Column(
            width=350,
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Container(
                    width=float("inf"),  # 👉 전체 너비 차지
                    alignment=ft.Alignment(-1, 0),  # 👉 왼쪽 정렬  # 👈 왼쪽 이동
                    content=ft.Icon(ft.Icons.ARROW_BACK),
                ),
                ft.Text("Welcome to 똑똑", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=20),
                ft.Text("똑똑🚪✊ 우리집 강아지가 마지막 한알을 먹기 전", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=10),
                ft.Text("문앞에 사료가 도착합니다", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=10),

                ft.Text("프로필을 완성하세요.", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=30),

                ft.Text("이메일", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
                input_box("example@gmail.com"),

                ft.Text("닉네임", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
                input_box("닉네임"),

                # section_gap(80),  #  👉 여기서 거리 조절

                bottom_continue_button()
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