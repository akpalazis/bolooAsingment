from db import db, ShortURL


def convert_url(url):
    if url.find("http://") != 0 and url.find("https://") != 0:
        return "http://" + url


def long_url_exist(url_id):
    entries_with_url = ShortURL.query.filter(ShortURL.id == url_id).first()
    if entries_with_url:
        return True
    else:
        return False


def fetch_long_entry(url_id):
    entries_with_url = ShortURL.query.filter(ShortURL.id == url_id).first()
    return entries_with_url


def store_user_data(url_entry, ip):
    url_entry.hits += 1
    ips = set(url_entry.ips)
    ips.add(ip)
    url_entry.uniq_hits = len(ips)
    url_entry.ips = ips
    db.session.commit()
