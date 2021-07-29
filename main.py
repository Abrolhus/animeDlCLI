import click
from Crypto.Cipher import AES
import base64
from hashlib import md5
import warnings
import requests_cache
import requests
import logging
import subprocess
import tempfile
import mpv

from anime_downloader.sites import get_anime_class
import util

def logHandler(loglevel, component, message):
    # TODO: use style config for this loghandler. Instead of hardcoding hera
    if loglevel == 'error':
        colored_loglevel = click.style(loglevel, fg='red')
    elif loglevel == 'warn':
        colored_loglevel = click.style(loglevel, fg='yellow')
    click.echo('[{}] {}: {}'.format(colored_loglevel, component, message))

@click.command()
@click.argument('name', nargs=-1)
@click.option('-e', '--ep', default=1, help='episode no.')
@click.option('--provider', default='twist.moe', help='site to get episodes from')
@click.option('--autoplay', is_flag=True, help='autoplays next episode')
@click.option('--log-level', '--ll', default='error', type=click.Choice(["no", "fatal", "error", "warn", "info", "v", "debug", "trace"], case_sensitive=False))
def hello(name, ep, provider, autoplay, log_level):
    strName = " ".join(name)
    Anime = get_anime_class(provider)
    player = 'mpv'

    searchResults = Anime.search(strName)
    anime = Anime(searchResults[0].url)
    click.echo('anime: {}'.format(anime)
    episode = anime[ep-1]
    #click.echo('stream URL: {}'.format(episode.source().stream_url))
    #click.echo('referrer: {}'.format(episode.source().referer))
    if player == 'mpv':
        player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True, log_handler=logHandler, loglevel=log_level)
        title = f'{anime.title} - Episode {episode.ep_no}'
        url = 'ffmpeg://{}'.format(episode.source().stream_url)
        referrer = episode.source().referer
        player.loadfile(url, "append-play", title=title, referrer=referrer)
        #player.loadfile("../testeMpvJsonIpc/v2.mp4")

        for episode in anime[1:]:
            title = f'{anime.title} - Episode {episode.ep_no}'
            url = 'ffmpeg://{}'.format(episode.source().stream_url)
            referrer = episode.source().referer
            player.playlist_append(url, title=title, referrer=referrer)
        player.wait_for_property('idle-active')
    else:
        pass
        #p = subprocess.Popen([player, episode.source().stream_url])
        #p.wait()

if __name__ == "__main__":
    hello()

style = {
    errColor : ('red', None),
    warnColor : ('yellow', None)
}
