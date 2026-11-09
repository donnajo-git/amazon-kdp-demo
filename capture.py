from playwright.sync_api import sync_playwright
from pathlib import Path
root=Path('/mnt/data/kdp-portfolio')
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for fname,out in [('confidence-hub-prototype.html','prototype-dashboard.png'),('bookshelf-preview.html','bookshelf-preview.png')]:
  page=browser.new_page(viewport={'width':1440,'height':900},device_scale_factor=1)
  page.goto('http://127.0.0.1:8765/'+fname,wait_until='load');page.wait_for_timeout(400)
  page.screenshot(path=str(root/'assets'/out),full_page=False)
  print(fname,page.title(),page.locator('body').inner_text()[:180])
  page.close()
 browser.close()
