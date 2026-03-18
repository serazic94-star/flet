import flet as ft

def main(page: ft.Page):
      page.vertical_alignment = ft.MainAxisAlignment.CENTER # 👉 없으면 위로 올라감
      page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # 👉 없으면 왼쪽으로 붙어버림
      page.title = "Signin/up"

      summary_cards = ft.Column(
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          alignment=ft.MainAxisAlignment.CENTER,
          spacing=16,
          controls=[
              ft.Container(
                  width=350, # 👉 가로 길이: 값을 크게 하면 옆으로 길쭉한 버튼이 됨
                  height=50, # 👉 세로 길이: 값을 작게 하면 납작한 버튼 느낌
                  bgcolor=ft.Colors.WHITE,
                  border_radius=0,
                  padding=10,
                  content=ft.Column(
                      alignment=ft.MainAxisAlignment.CENTER,
                      horizontal_alignment=ft.CrossAxisAlignment.START,
                      controls=[
                          ft.Text("Continue with Google", size=13, color=ft.Colors.GREY_700),
                      ]
                  ),
              ),
              ft.Container(
                  width=350, # 👉 가로 길이: 값을 크게 하면 옆으로 길쭉한 버튼이 됨
                  height=50, # 👉 세로 길이: 값을 작게 하면 납작한 버튼 느낌
                  bgcolor=ft.Colors.WHITE,
                  border_radius=0,
                  padding=10,
                  content=ft.Column(
                      alignment=ft.MainAxisAlignment.CENTER,
                      horizontal_alignment=ft.CrossAxisAlignment.START,
                      controls=[
                          ft.Text("Continue with Google", size=13, color=ft.Colors.GREY_700),
                      ]
                  ),
              ),
                ft.Container(
                            width=350, # 👉 가로 길이: 값을 크게 하면 옆으로 길쭉한 버튼이 됨
                            height=50, # 👉 세로 길이: 값을 작게 하면 납작한 버튼 느낌
                            bgcolor=ft.Colors.WHITE,
                            border_radius=0,
                            padding=10,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                controls=[
                                    ft.Text("Continue with Google", size=13, color=ft.Colors.GREY_700),
                                ]
                            ),
                        ),
                      ]  # ✅ 이거 꼭 있어야 함
                  )
      
      stop_line = ft.Row(
          alignment=ft.MainAxisAlignment.CENTER,
          width=350,  # 👈 이거 추가하면 summary_cards랑 맞춰짐
          controls=[
              ft.Container(
                  expand=True,
                  height=1,
                  bgcolor=ft.Colors.GREY_400,
              ),
              ft.Text("OR", size=12),
              ft.Container(
                  expand=True,
                  height=1,
                  bgcolor=ft.Colors.GREY_400,
              ),
          ],
      )

      body = ft.Container(
              padding=ft.Padding.only(top=-180),
                    content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    controls=[
                      ft.Text("Sign In / Sign Up", size=20),  # 👈 그냥 추가하면 됨
                      summary_cards, 
                      stop_line
                    ],
                )
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