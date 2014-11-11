"""
    app.rec_config.views
    ~~~~~~~~~~~~~~~~~~~~

    The purpose of this module is to statically populate the templates
    with information from Configuration tables in the database.

    Supplies routing and templates for editing or creating a configuration.
    There is no dynamic DOM changes in this blueprint.
"""

# Python2.7 imports
import time

# flask imports
from flask import render_template, request, redirect, url_for

# app imports
from app import db
from app.models import Configuration, CurrentConfiguration

# current package imports
from . import rec_config_bp
from .forms import ConfigurationNewForm


@rec_config_bp.route('/')
def config():
    """
        rec_config.config
        ~~~~~~~~~~~~~~~~~

        Provides a list of all the configurations, statically populated
        on the template.

        By clicking on a table entry in the browser, the user is routed to
        a configuration edit page.

        By clicking on the new configuration button the user is routed to
        a page where they can create a new config. 

    """
    configs = Configuration.query.all()
    current_config = CurrentConfiguration.query.first()
    names = []
    dates = []
    ids = []
    current_id = None
    if configs is not None and current_config is not None:
        current_id = current_config.config_id
        for config in configs:
            names.append(config.config_name)
            dates.append(time.ctime(config.config_time/1000000))
            ids.append(config.config_id)

    return render_template("rec_config/rec_config.html", names=names,
                            dates=dates, ids=ids, current_id=current_id)


@rec_config_bp.route('/new', methods=['GET', 'POST'])
def new():
    """
        rec_config.new
        ~~~~~~~~~~~~~~

        A Configuration form is passed to the template statically where
        the user can enter fields for a new config. Not the 'pythonic way' of
        handeling repetitive data, but my method is simple to understand.
    """
    error = None
    print "rec_config.new: incoming request"
    if request.method == 'POST':
        form = ConfigurationNewForm(request.form)
        config_test = Configuration.query.filter_by(config_name=form.config_name.data).first()
        if config_test is None:
            kwargs = {}
            kwargs['config_name'] = form.config_name.data
            kwargs['config_time'] = time.time()*1000000

            # SFP Cage 1
            if form.enabled_1a.data:
                kwargs['ip_1a'] = form.ip_1a.data
                kwargs['port_1a'] = form.port_1a.data

            if form.enabled_1b.data:
                kwargs['ip_1b'] = form.ip_1b.data
                kwargs['port_1b'] = form.port_1b.data

            if form.enabled_1c.data:
                kwargs['ip_1c'] = form.ip_1c.data
                kwargs['port_1c'] = form.port_1c.data

            if form.enabled_1d.data:
                kwargs['ip_1d'] = form.ip_1d.data
                kwargs['port_1d'] = form.port_1d.data


            # SFP Cage 2
            if form.enabled_2a.data:
                kwargs['ip_2a'] = form.ip_2a.data
                kwargs['port_2a'] = form.port_2a.data

            if form.enabled_1b.data:
                kwargs['ip_2b'] = form.ip_2b.data
                kwargs['port_2b'] = form.port_2b.data

            if form.enabled_2c.data:
                kwargs['ip_2c'] = form.ip_2c.data
                kwargs['port_2c'] = form.port_2c.data

            if form.enabled_1d.data:
                kwargs['ip_2d'] = form.ip_2d.data
                kwargs['port_2d'] = form.port_2d.data


            # SFP Cage 3
            if form.enabled_3a.data:
                kwargs['ip_3a'] = form.ip_3a.data
                kwargs['port_3a'] = form.port_3a.data

            if form.enabled_3b.data:
                kwargs['ip_3b'] = form.ip_3b.data
                kwargs['port_3b'] = form.port_3b.data

            if form.enabled_3c.data:
                kwargs['ip_3c'] = form.ip_3c.data
                kwargs['port_3c'] = form.port_3c.data

            if form.enabled_3d.data:
                kwargs['ip_3d'] = form.ip_3d.data
                kwargs['port_3d'] = form.port_3d.data


            # SFP Cage 3
            if form.enabled_4a.data:
                kwargs['ip_4a'] = form.ip_4a.data
                kwargs['port_4a'] = form.port_4a.data

            if form.enabled_4b.data:
                kwargs['ip_4b'] = form.ip_4b.data
                kwargs['port_4b'] = form.port_4b.data

            if form.enabled_4c.data:
                kwargs['ip_4c'] = form.ip_4c.data
                kwargs['port_4c'] = form.port_4c.data

            if form.enabled_4d.data:
                kwargs['ip_4d'] = form.ip_4d.data
                kwargs['port_4d'] = form.port_4d.data

            config = Configuration(**kwargs)

            db.session.add(config)
            db.session.commit()
            return redirect(url_for('rec_config.config'))
        else:
            error = "Configuration Name already exsists"
    return render_template("rec_config/config_new.html", form=ConfigurationNewForm(),
        error=error)


@rec_config_bp.route('/edit')
def edit():
    """
        rec_config.edit
        ~~~~~~~~~~~~~~~

        
    """
    return render_template("rec_config/config_edit.html")
