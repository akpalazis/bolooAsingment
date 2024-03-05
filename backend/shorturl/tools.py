from flask import jsonify

from db import ShortURL, db


def short_url_exist(url):
    url_entries = ShortURL.query.filter(ShortURL.long_url == url).first()
    return True if url_entries else False


def fetch_short_url(url):
    short_url_entry = ShortURL.query.filter(ShortURL.long_url == url).first()
    return jsonify({"short_url": short_url_entry.id})


def generate_short_url(url):
    new_entry = ShortURL(
        long_url=url,
        user_id=None,
        hits=0,
        uniq_hits=0,
        ips=[],
    )

    # Add the new entry to the database session
    db.session.add(new_entry)

    # Commit the changes to the database
    db.session.commit()
    return jsonify({"short_url": new_entry.id})



