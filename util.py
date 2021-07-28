import tempfile
import subprocess
# EXTM3U
# #EXTINF:123, Sample artist - Sample title
# https://cdn.twist.moe/anime/yakusokunoneverlands2/[SubsPlease] Yakusoku no Neverland S2 - 01 (1080p) [D1AA4F5C].mp4


def makePlaylist(animeList, file):
        file.write('#EXTM3U\n\n')
        for anime in animeList:
            title = f'{animeList.title} - Episode {anime.ep_no}'
            file.write('#EXTINF:123, {}'.format(title) + '\n' + 'ffmpeg://' + anime.source().stream_url +'\n')


def addAnimesToPlaylist(animeList, file):
    # tf.write('#EXTM3U\n\n')
    for anime in animeList:
        title = f'{animeList.title} - Episode {anime.ep_no}'
        file.write('#EXTINF:123, {}'.format(title) + '\n' + 'ffmpeg://' + anime.source().stream_url +'\n')
def addAnimeToMpvList(animeList, anime, is_before, ipcPath):
    title = f'{animeList.title} - Episode {anime.ep_no}'
    tfile = tempfile.NamedTemporaryFile(mode='a+', suffix='.m3u8')
    tfile.append('#EXTINF:123, {}'.format(title) + '\n' + 'ffmpeg://' + anime.source().stream_url +'\n')
    title
    echoString = '{ "command": ["loadfile", "append", "title={title}"'
    pipeString = '| socat - /tmp/' + ipcPath
    subprocess.Popen(["echo", echoString, pipeString]); # runs command (command line) that adds playlist (that has only one item) to current mpv internal playlist.
