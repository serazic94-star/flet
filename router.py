import flet as ft
from home import home_view
# from log import log_view
# from shop import shop_view


def router(page):
    page.views.clear()

    if page.route == "/":
        page.views.append(home_view(page))

    # elif page.route == "/log":
    #     page.views.append(log_view(page))

    # elif page.route == "/shop":
    #     page.views.append(shop_view(page))
    else:
        page.views.append(
            ft.View(
                route=page.route,
                controls=[ft.Text("페이지 없음", color=ft.Colors.BLACK)]
            )
        )

    page.update()