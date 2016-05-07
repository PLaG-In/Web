import metalTracker
CHAT_URL = 'http://www.metal-tracker.com/chat/'


def main():
    pf = {
        'lastID': '',
        'text': 'hello'
    }
    metalTracker.MetalTracker.connect(metalTracker.MetalTracker,CHAT_URL + '?ajax=true', CHAT_URL + 'index.php', pf)


if __name__ == "__main__":
    main()