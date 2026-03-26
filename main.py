import asyncio
import flet as ft
from home import home_view
# from log import log_view
# from shop import shop_view
from router import router

import webbrowser
import os


def main(page: ft.Page):

    async def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        await page.push_route(top_view.route)

    page.on_route_change = lambda e: router(page)
    page.on_view_pop = view_pop

    asyncio.create_task(page.push_route("/"))


if __name__ == "__main__":
    import webbrowser
    import os

    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )