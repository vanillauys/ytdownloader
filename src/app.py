# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


from youtube import Downloader, Stream
from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import typer


# ---------------------------------------------------------------------------- #
# --- Configuration ---------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


app = typer.Typer()
console = Console()
downloader = Downloader()


# ---------------------------------------------------------------------------- #
# --- Helper Functions ------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


def print_streams(streams: list[Stream]):
    table = Table("Item", "Resolution", "FPS", "VCodec", "ACoded", "Type", "Size (MB)")
    for index, stream in enumerate(streams, start=1):
        table.add_row(
            str(index),
            stream.resolution,
            str(stream.fps),
            stream.vcodec,
            stream.acodec,
            stream.type,
            str(stream.filesize_mb)
        )
    console.print(table)


# ---------------------------------------------------------------------------- #
# --- Commands --------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


@app.command()
def download(url: str):
    title, streams = downloader.downloads_list(url)
    print("[bold green]Title:[/bold green]")
    print(title)
    print_streams(streams)
    item = Prompt.ask("Which item do you want to download?")
    item = int(item) - 1
    downloader.dowload_video(url, streams[item].itag)
    print("[bold green] Successfully downloaded! [/bold green]")

    
# ---------------------------------------------------------------------------- #
# --- Main ------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    app()
