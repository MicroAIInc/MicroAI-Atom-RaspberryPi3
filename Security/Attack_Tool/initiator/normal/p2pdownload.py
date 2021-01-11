# Install this dependency
# sudo apt-get install -y python3-libtorrent
# Usage: python3 p2pdownload.py
import subprocess
import time
import libtorrent as lt

import os
import sys
sys.path.append('..')
from cfg import cfg

try:
    import libtorrent as lt

except:
    print("packages not found.. installing....")
    os.system("sudo apt-get install -y python3-libtorrent")


def main():

    ses = lt.session()
    ses.listen_on(6881, 6891)
    params = {
        'save_path': '/tmp',
        'storage_mode': lt.storage_mode_t(2),
        'paused': False,
        'auto_managed': True,
        'duplicate_is_error': True}
    link = "magnet:?xt=urn:btih:37e77490bc4f285dbfa837514715a20bd405a502&dn=Spider-Man+Far+from+Home+%282019%29+%5BWEBRip%5D+%5B1080p%5D+English&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Fzer0day.ch%3A1337&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969"
    handle = lt.add_magnet_uri(ses, link, params)
    ses.start_dht()

    print('downloading metadata...')
    while (not handle.has_metadata()):
        time.sleep(1)
    print('got metadata, starting torrent download...')

    timeout = time.time() + cfg.p2pdownload_timer  # 10 secs from now

    while (handle.status().state != lt.torrent_status.seeding):
        s = handle.status()
        state_str = ['queued', 'checking', 'downloading metadata',
                     'downloading', 'finished', 'seeding', 'allocating']
        print('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' %
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
               s.num_peers, state_str[s.state]))
        if time.time() > timeout:
            break
        time.sleep(2)


if __name__ == '__main__':
    main()
