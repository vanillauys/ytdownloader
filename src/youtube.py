# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


from dataclasses import dataclass, asdict
from pytube import YouTube
from typing import Tuple


# ---------------------------------------------------------------------------- #
# --- YouTube Video Downloader ----------------------------------------------- #
# ---------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Stream:
    itag: int
    mime_type: str
    resolution: str
    fps: str
    vcodec: str
    acodec: str
    is_progressive: bool
    type: str
    filesize_mb: float


class Downloader():

    # ------------------------------------------------------------------------ #
    # --- Youtube Configuration ---------------------------------------------- #
    # ------------------------------------------------------------------------ #


    directory: str = 'videos/'

    def __init__(self, directory: str):
        self.directory = directory

    def __init__(self):
        self.directory = 'videos/'


    # ------------------------------------------------------------------------ #
    # --- Youtube Downloader ------------------------------------------------- #
    # ------------------------------------------------------------------------ #


    def downloads_list(self, url: str) -> Tuple[str, list[Stream]]:
        yt = YouTube(url)
        title = yt.title
        streams_list = yt.streams.filter(progressive=True, file_extension='mp4')
        streams = []
        for stream in streams_list:
            streams.append(self.__create_stream_object(stream))
        return title, streams

    def dowload_video(self, url: str, itag: int):
        yt = YouTube(url)
        yt.streams.get_by_itag(itag).download(self.directory)

    def __create_stream_object(self, stream) -> Stream:
        return Stream(
            stream.itag,
            stream.mime_type,
            stream.resolution,
            stream.fps,
            stream.codecs[0],
            stream.codecs[1],
            stream.is_progressive,
            stream.type,
            stream.filesize_mb
        )


# ---------------------------------------------------------------------------- #
# --- Main ------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


def main():
    #Nothing to do here
    pass


if __name__ == "__main__":
    main()
