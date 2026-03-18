import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE


    body = ft.Container( # 🔥 (기존 ft.Padding → ft.padding으로 수정 권장)
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                      ft.Container(
                            width=350,
                            alignment=ft.Alignment(-1, -1),
                            padding=ft.padding.only(top=80, left=10), 
                            content= ft.Text("Welcome to 똑똑", size=20),
                        ),
                      ft.Container(
                            width=250,
                            alignment=ft.Alignment(-1, -1),
                            content= ft.Text("똑똑🚪✊ 우리집 강아지가 마지막 한알을 먹기 전", size=10),
                        ),
                      ft.Container(
                            width=250,
                            alignment=ft.Alignment(-1, -1),
                            content= ft.Text("문앞에 사료가 도착합니다", size=10),
                        ),
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