import asyncio
from playwright.async_api import async_playwright
from selectolax.parser import HTMLParser

async def render(url, path_to_ss = "ss.png"):
    '''
    Renders the given url for you and gives the Html of the url.
    '''
    TIMEOUT = 120000
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url, timeout=TIMEOUT)
        
        await page.wait_for_load_state("domcontentloaded", timeout=TIMEOUT)
        last_height = page.evaluate("() => document.body.scrollHeight")
        scrolls = 0
        max_scrolls = 2
        while scrolls < max_scrolls:
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await asyncio.sleep(2)  

            new_height = await page.evaluate("() => document.body.scrollHeight")
            if new_height == last_height:
                break  
            last_height = new_height
            scrolls += 1
        
        await page.wait_for_selector("div.gASJ2lL_xmVNuZkWGvrWg", timeout=TIMEOUT)
        # await page.wait_for_load_state("networkidle")
        
        # await page.screenshot(path=path_to_ss, full_page=True)
        
        return await page.inner_html("body")

if __name__ == "__main__":
    html = asyncio.run(render("https://store.steampowered.com/specials"))
    tree = HTMLParser(html)
    nodes = tree.css("div.gASJ2lL_xmVNuZkWGvrWg")
    print(len(nodes))

    