"""
    app.ctr_panel.view
    ~~~~~~~~~~~~~~~~~~

    The purpose of this module is to retrieve information from the
    database, and statically populate the templates with the information
    from the Configuration, Recording, Events, and ServerStatus tables.

    Displaying the server time and status requires manipulting the DOM
    dynamically. AJAX is used to ping the server for the time and status
    every second.
"""

# Python2.7 imports
import time

# flask imports
from flask import render_template, jsonify

# app imports
from app.models import EventTag, ServerStatus, Recording, CurrentConfiguration, Configuration

# current package imports
from .import ctr_panel_bp


@ctr_panel_bp.route('/', methods=['GET'])
def control_panel():
    """
        ctr_panel.control_panel
        ~~~~~~~~~~~~~~~~~~~~~~~

        Template's Recording, and Configuration data is populated statically.
        Information such as the server time, and status is populated dynamically.
    """
    recs = Recording.query.all()
    # Use the last 4 recordings in the database, if there
    # are less than 4 recs, send them all.
    rec_ids = []
    rec_names = []
    rec_labels = []
    rec_sizes = []
    rec_ends = []
    rec_starts = []
    if len(recs) > 4:
        for i in range(-4, 0):
            rec_ids.append(recs[i].rec_id)
            rec_names.append(recs[i].rec_name)
            rec_labels.append(recs[i].label)
            rec_sizes.append(recs[i].rec_size)
            rec_ends.append(time.ctime(recs[i].end_time/1000000))
            rec_starts.append(time.ctime(recs[i].start_time/1000000))
    elif recs is not None:
        for rec in recs:
            rec_ids.append(rec.rec_id)
            rec_names.append(rec.rec_name)
            rec_labels.append(rec.label)
            rec_sizes.append(rec.rec_size)
            rec_ends.append(time.ctime(rec.end_time/1000000))
            rec_starts.append(time.ctime(rec.start_time/1000000))
        rec_ids.reverse()
        rec_names.reverse()
        rec_labels.reverse()
        rec_starts.reverse()
        rec_ends.reverse()
        rec_sizes.reverse()

    # Get Event Tags for Recordings
    tags = []
    for rec_id in rec_ids:
        rec_tags = EventTag.query.filter_by(record_id=rec_id).all()
        if rec_tags is not None:
            for tag in rec_tags:
                tags.append(tag)
    tag_ids = []
    tag_descriptions = []
    tag_times = []
    tag_record_ids = []
    for tag in tags:
        tag_ids.append(tag.tag_id)
        tag_descriptions.append(tag.description)
        tag_times.append(time.ctime(tag.tag_time/1000000))
        tag_record_ids.append(tag.record_id)

    tag_record_names = []
    for tag_record_id in tag_record_ids:
        rec = Recording.query.filter_by(rec_id=tag_record_id).first()
        tag_record_names.append(rec.rec_name)



    # Get the Current Configuration
    current_config_foreign = CurrentConfiguration.query.first()
    c_config_name = []
    c_config_id = []
    c_config_date = []
    if current_config_foreign is not None:
        current_config_id = current_config_foreign.config_id
        current_config = Configuration.query.filter_by(config_id=current_config_id).first()
        if current_config is not None:
            c_config_date.append(time.ctime(current_config.config_time/1000000))
            c_config_id.append(current_config.config_id)
            c_config_name.append(current_config.config_name)

    return render_template('ctr_panel/control_panel.html', rec_ids=rec_ids, rec_names=rec_names,
        rec_labels=rec_labels, rec_sizes=rec_sizes, rec_ends=rec_ends,
        rec_starts=rec_starts, tag_ids=tag_ids, tag_record_names=tag_record_names,
        tag_descriptions=tag_descriptions, tag_times=tag_times, 
        tag_record_ids=tag_record_ids, c_config_name=c_config_name,
        c_config_id=c_config_id, c_config_date=c_config_date)

