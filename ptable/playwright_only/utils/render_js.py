from playwright.async_api import async_playwright


async def render(url):
    '''
    An async method which utilizes `playwright` to render the js of a given url.

    Args:
        url: Url of the site to be rendered by `playwright`.
    
    Returns:
        The "body" content of the HTML present got from the `url`. 
    '''
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_load_state("networkidle", timeout=60000)
        return await page.inner_html("body")


if __name__ == "__main__":
    import asyncio
    html = asyncio.run(render("https://pubchem.ncbi.nlm.nih.gov/ptable/"))
    print(html)