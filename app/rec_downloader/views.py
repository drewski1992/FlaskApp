"""
    app.rec_downloader.views
    ~~~~~~~~~~~~~~~~~~~~~~~~

    The purpose of this module is to retrieve information from the
    database, and statically populate the templates with the information
    from the Recording table.

    When a recording is clicked on in the template, the user is routed
    to 'rec_downloader.download', with the ID of the chosen recording passed
    as an arguement.
"""

# Pyhton2.7 Imports
import time

# flask imports
from flask import render_template

# app imports
from app.models import Recording

# Downloader package imports
from . import rec_downloader_bp


@rec_downloader_bp.route('/')
def list():
    """
        rec_downloader.list
        ~~~~~~~~~~~~~~~~~~~

        Provides a template statically populated with recordings.
        User clicks on a table's entry to initiate a download sequence
        for that given recording.
    """
    recs = Recording.query.all()
    rec_ids = []
    rec_names = []
    rec_labels = []
    rec_sizes = []
    rec_starts = []
    rec_ends = []
    if recs is not None:
        for rec in recs:
            rec_ids.append(rec.rec_id)
            rec_names.append(rec.rec_name)
            rec_labels.append(rec.label)
            rec_sizes.append(rec.rec_size)
            rec_starts.append(time.ctime(rec.start_time/1000000))
            rec_ends.append(time.ctime(rec.end_time/1000000))
    return render_template("rec_downloader/rec_download.html", rec_ids=rec_ids,
                rec_names=rec_names, rec_labels=rec_labels, rec_sizes=rec_sizes,
                rec_starts=rec_starts, rec_ends=rec_ends)


@rec_downloader_bp.route('/download')
def download():
    """
        rec_downloader.download
        ~~~~~~~~~~~~~~~~~~~~~~~

        Provides a template, and an intutive interface for the user to
        download a recording.
    """
    return "0"