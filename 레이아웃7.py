import flet as ft

def arrow_back(on_click=None):
      return ft.Container(
        width=float("inf"),  # 👉 전체 너비 차지
        alignment=ft.Alignment(-1, 0),  # 👉 왼쪽 정렬  # 👈 왼쪽 이동
        on_click=on_click,
        content=ft.Icon(ft.Icons.ARROW_BACK),
        )

def about_dog():
    return ft.Column(
        spacing=0,
        controls=[
            ft.Text("About your Dog", size=30),
            ft.Text("반려동물의 기본 정보를 입력하세요", size=15),
        ],
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
    page.scroll = ft.ScrollMode.AUTO
    page.title = "For Dog4"

    body = ft.Container(
                      padding=ft.padding.only(top=0), # 🔥 (1) 전체 레이아웃을 아래로 내림 음수 제거
                      content=ft.Column(
                          width=350, # 🔥 (2) Column 자체의 너비를 고정
                          spacing=12, 
                          horizontal_alignment=ft.CrossAxisAlignment.START, # center를 start로 바꿈
                          scroll=ft.ScrollMode.AUTO,
                          controls=[
                              arrow_back(),
                              ft.Container(
                                  margin=ft.margin.only(top=50),
                                  content=about_dog(),
                              ),
                              ft.Text("알레르기"),
                              input_box("반려동물의 알레르기를 적어주세요"),

                              ft.Text("질병"),
                              input_box("반려동물의 질병을 적어주세요"),

                              bottom_continue_button(),
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