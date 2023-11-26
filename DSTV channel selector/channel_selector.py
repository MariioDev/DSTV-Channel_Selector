import webbrowser
from rich.console import Console
from rich.text import Text
from rich.table import Table

console = Console()

def mainProgram():
    channels = Table(title="DSTV Channels")

    channels.add_column("code")
    channels.add_column("name")
    channels.add_column("category")

    channels.add_row("100", "Dish TV", "promo")
    channels.add_row("101", "MNet", "others")
    channels.add_row("103", "1Magic")
    channels.add_row("104", "MNet 1", "movies")
    channels.add_row("106", "MNet 2", "movies")
    channels.add_row("107", "MNet 3", "movies")
    channels.add_row("108", "MNet 4", "movies")
    channels.add_row("161", "Mzansi Magic", "others")
    channels.add_row("162", "Zambezi Magic", "others")

    console.print(channels)

    mainText = Text("Channel wanted: ")
    mainText.stylize("bold white")
    channelWanted = input(mainText)

    if channelWanted == "101":
        webbrowser.open_new_tab("https://dstv.stream/livetv/play/eab73dde-155e-4515-a706-6d1324f9084b")
    if channelWanted == "103":
        webbrowser.open_new_tab("https://dstv.stream/livetv/play/2a094aeb-1f47-44c5-abfe-056ad928db8c")
    if channelWanted == "104":
        webbrowser.open_new_tab("https://dstv.stream/livetv/play/d7197942-ef3b-4533-a7ed-1d26f41b9d46")
    if channelWanted == "106":
        webbrowser.open_new_tab("https://dstv.stream/livetv/play/a4ec39ad-9b0f-44cb-bc4b-672d0a005405")
    if channelWanted == "107":
        webbrowser.open_new_tab("https://dstv.stream/livetv/play/85ddeeb9-6508-4270-a9b9-cfa247b7021e")
    if channelWanted == "108":
        webbrowser.open_new_tab("https://dstv.stream/livetv/play/a0e986c2-9734-480f-981b-1f7c18852728")

mainProgram()
