from sty import Style, RgbFg, fg

fg.orange = Style(RgbFg(255, 150, 50))
fg.yelloww = Style(RgbFg(255, 255, 0))

MESSAGES = {"ERROR": f"{fg.red}[ERROR] {{}}{fg.rs}",
            "WARNING": f"{fg.orange}[WARNING] {{}}{fg.rs}",
            "INFO": f"{fg.yelloww}[INFO] {{}}{fg.rs}",
            "SYSTEM": f"{fg.cyan}[SYSTEM] {{}}{fg.rs}"}

def log(type, text):
    print(MESSAGES[type].format(text))
