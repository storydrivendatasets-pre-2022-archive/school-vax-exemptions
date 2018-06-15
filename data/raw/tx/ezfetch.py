"""
just a prototype!
"""
import yaml
import requests
from pathlib import Path

DEST_DIR = Path('.')
MANIFEST_PATH = Path('meta.yaml')

def get_manifest():
    return yaml.load(MANIFEST_PATH.read_text())

if __name__ == '__main__':
    manifest = get_manifest()
    for dname, props in manifest.items():
        dest_path = DEST_DIR.joinpath(dname)
        src_url = props['urls'].get('original')
        if src_url:
            print("Getting", src_url)
            # TX servers do not have a valid SSL cert
            # http://docs.python-requests.org/en/master/user/advanced/#ssl-cert-verification
            resp = requests.get(src_url, verify=False)
            if resp.status_code != 200:
                raise ValueError('Status code: {}'.format(resp.status_code))
            else:
                print("Saving to:", dest_path)
                with dest_path.open('wb') as w:
                    w.write(resp.content)
                    print("Saved {} bytes".format(len(resp.content)))
